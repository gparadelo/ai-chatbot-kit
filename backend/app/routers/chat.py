from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from shared.chat_core import generate_chat_response

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
async def chat(message: str):
    """Send a message and get AI response from CrewAI"""
    try:
        ai_response = generate_chat_response(message)
        return ChatResponse(response=str(ai_response))
    except Exception as e:
        fallback_response = (
            f"🤖 AI Assistant: I received your message '{message}'. "
            f"There was an issue connecting to the AI service: {str(e)}"
        )
        return ChatResponse(response=fallback_response) 