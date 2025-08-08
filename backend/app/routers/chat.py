from fastapi import APIRouter, HTTPException
from typing import Optional
from datetime import datetime

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/")
async def chat(message: str):
    """Send a message and get mocked AI response"""
    try:
        # Mock AI response
        ai_response = f"Mock response to: {message}"
        
        return {
            "response": ai_response,
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 