#!/usr/bin/env python3
"""
Startup script for the AI Chatbot Kit FastAPI application
"""

import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    print(f"Starting {settings.api_title} v{settings.api_version}")
    print(f"Server will be available at http://{settings.host}:{settings.port}")
    print(f"API Documentation: http://{settings.host}:{settings.port}/docs")
    print(f"Health Check: http://{settings.host}:{settings.port}/health")
    print("-" * 50)
    
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.lower()
    ) 