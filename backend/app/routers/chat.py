from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..crew.crew import CrewaiConversationalChatbotCrew

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
async def chat(message: str):
    """Send a message and get AI response from CrewAI with ChatGPT"""
    try:
        # Initialize the CrewAI chatbot
        crew = CrewaiConversationalChatbotCrew()
        
        # Prepare inputs for the crew
        inputs = {
            "user_message": message,
        }
        
        # Get response from CrewAI with ChatGPT
        ai_response = crew.crew().kickoff(inputs=inputs)
        
        return ChatResponse(response=str(ai_response))
    
    except Exception as e:
        # Fallback response for any errors
        fallback_response = f"🤖 AI Assistant: I received your message '{message}'. There was an issue connecting to the AI service: {str(e)}"
        return ChatResponse(response=fallback_response) 