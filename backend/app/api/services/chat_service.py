"""
Chat service for handling conversation context and AI interactions
"""
from ..database import get_recent_messages
import logging

logger = logging.getLogger(__name__)

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
