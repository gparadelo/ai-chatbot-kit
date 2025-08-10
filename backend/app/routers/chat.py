from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..crew.crew import CrewaiConversationalChatbotCrew
from ..database import add_message, get_recent_messages, cleanup_expired_threads
from typing import Optional
import logging
import uuid

logger = logging.getLogger(__name__)

# Initialize CrewAI once (not per request)
crew = None
try:
    crew = CrewaiConversationalChatbotCrew()
    logger.info("CrewAI initialized successfully")
except Exception as e:
    logger.error(f"CrewAI initialization failed: {e}")
    logger.error("Please check your API keys and model configuration")
    crew = None

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str
    thread_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    thread_id: str

def build_context_prompt(thread_id: str, current_message: str) -> str:
    """Build the context-aware prompt with conversation history"""
    
    # Get recent messages from the thread
    recent_messages = get_recent_messages(thread_id, limit=5)
    
    if not recent_messages:
        # No conversation history, just return the current message
        return current_message
    
    # Build the context prompt
    context_prompt = "MEMORY CONTEXT: Below are the last conversations between the user and assistant:\n\n"
    
    # Group messages into conversations (user + assistant pairs)
    conversations = []
    current_conversation = []
    
    for msg in recent_messages:
        current_conversation.append(f"{msg['role'].title()}: {msg['content']}")
        
        # When we hit an assistant message, complete the conversation
        if msg['role'] == 'assistant':
            conversations.append("\n".join(current_conversation))
            current_conversation = []
    
    # Add any remaining messages as incomplete conversation
    if current_conversation:
        conversations.append("\n".join(current_conversation))
    
    # Add numbered conversations to the prompt
    for i, conversation in enumerate(conversations[-5:], 1):  # Last 5 conversations
        context_prompt += f"MESSAGE {i}:\n{conversation}\n\n"
    
    # Add current query and instructions
    context_prompt += f"CURRENT USER QUERY: {current_message}"

    return context_prompt

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a message and get AI response with conversation thread persistence"""
    try:
        # Extract message and thread_id from request
        message = request.message
        thread_id = request.thread_id
        
        # Generate thread_id if not provided
        if not thread_id:
            thread_id = str(uuid.uuid4())
            logger.info(f"Generated new thread_id: {thread_id}")
        
        # Cleanup expired threads periodically
        try:
            cleanup_expired_threads()
        except Exception as e:
            logger.warning(f"Cleanup failed: {e}")
        
        # Use pre-initialized CrewAI chatbot
        if not crew:
            raise HTTPException(
                status_code=500, 
                detail="AI service not available. Please check your API configuration and restart the service."
            )
        
        # Build context-aware prompt with conversation history
        enhanced_message = build_context_prompt(thread_id, message)
        
        inputs = {
            "user_message": enhanced_message,
        }
        
        # Store the user message in database
        add_message(thread_id, "user", message)
        
        # Get response from CrewAI with ChatGPT
        ai_response = crew.crew().kickoff(inputs=inputs)
        response_text = str(ai_response)
        
        # Store the assistant response in database
        add_message(thread_id, "assistant", response_text)
        
        logger.info(f"Completed conversation in thread: {thread_id}")
        
        return ChatResponse(response=response_text, thread_id=thread_id)
    
    except Exception as e:
        # Fallback response for any errors
        fallback_response = f"AI Assistant: I received your message '{message}'. There was an issue connecting to the AI service: {str(e)}"
        
        # Still try to store messages even on error
        if thread_id:
            try:
                add_message(thread_id, "user", message)
                add_message(thread_id, "assistant", fallback_response)
            except Exception as db_e:
                logger.warning(f"Failed to store fallback conversation: {db_e}")
        else:
            thread_id = str(uuid.uuid4())
        
        return ChatResponse(response=fallback_response, thread_id=thread_id)


@router.get("/thread/{thread_id}/history")
async def get_thread_history(thread_id: str):
    """Get conversation history for a specific thread"""
    try:
        messages = get_recent_messages(thread_id, limit=50)  # Get more for history view
        return {
            "thread_id": thread_id,
            "messages": messages,
            "total_messages": len(messages)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve thread history: {str(e)}")


@router.delete("/thread/{thread_id}")
async def delete_thread(thread_id: str):
    """Delete a conversation thread"""
    try:
        from ..database import sqlite3, DATABASE_PATH
        
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM conversation_threads WHERE thread_id = ?", (thread_id,))
        deleted_count = cursor.rowcount
        
        conn.commit()
        conn.close()
        
        return {
            "success": True,
            "deleted_messages": deleted_count,
            "thread_id": thread_id
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete thread: {str(e)}")