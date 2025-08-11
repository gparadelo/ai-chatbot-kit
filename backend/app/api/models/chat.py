from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str
    thread_id: Optional[str] = None

class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str
    thread_id: str
