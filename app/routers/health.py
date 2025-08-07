from fastapi import APIRouter
from datetime import datetime
import time

router = APIRouter(prefix="/health", tags=["health"])

# Store start time for uptime calculation
start_time = time.time()

@router.get("/")
async def health_check():
    """Basic health check endpoint"""
    uptime = time.time() - start_time
    
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "uptime": uptime
    } 