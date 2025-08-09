"""
SQLite database for conversation thread persistence
"""
import sqlite3
import os
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json

logger = logging.getLogger(__name__)

DATABASE_PATH = "./data/conversations.db"

def init_database():
    """Initialize the SQLite database with conversation threads table"""
    try:
        # Ensure directory exists
        db_dir = os.path.dirname(DATABASE_PATH)
        os.makedirs(db_dir, exist_ok=True)
        logger.info(f"Database directory: {db_dir}")
        
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Create conversation_threads table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversation_threads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                thread_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create indexes separately
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_thread_id ON conversation_threads(thread_id)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_timestamp ON conversation_threads(timestamp)
        """)
        
        conn.commit()
        
        # Verify table was created
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='conversation_threads'")
        table_exists = cursor.fetchone()
        
        conn.close()
        
        if table_exists:
            logger.info(f"Database initialized successfully at {DATABASE_PATH}")
            return True
        else:
            logger.error("Table 'conversation_threads' was not created")
            return False
        
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        return False

def add_message(thread_id: str, role: str, content: str) -> bool:
    """Add a message to the conversation thread"""
    try:
        # Ensure database exists
        if not os.path.exists(DATABASE_PATH):
            init_database()
        
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        timestamp = datetime.now()
        
        cursor.execute("""
            INSERT INTO conversation_threads (thread_id, role, content, timestamp)
            VALUES (?, ?, ?, ?)
        """, (thread_id, role, content, timestamp))
        
        conn.commit()
        conn.close()
        
        logger.debug(f"Added {role} message to thread {thread_id}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to add message to thread {thread_id}: {e}")
        return False

def get_recent_messages(thread_id: str, limit: int = 5) -> List[Dict[str, str]]:
    """Get the most recent messages from a conversation thread"""
    try:
        # Ensure database exists
        if not os.path.exists(DATABASE_PATH):
            init_database()
        
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Get recent messages, ordered by timestamp desc, then reverse for chronological order
        cursor.execute("""
            SELECT role, content, timestamp FROM conversation_threads
            WHERE thread_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        """, (thread_id, limit * 2))  # Get more in case we need to pair user/assistant
        
        rows = cursor.fetchall()
        conn.close()
        
        # Reverse to get chronological order
        messages = []
        for role, content, timestamp in reversed(rows):
            messages.append({
                "role": role,
                "content": content,
                "timestamp": timestamp
            })
        
        # Return only the requested limit
        return messages[-limit:] if len(messages) > limit else messages
        
    except Exception as e:
        logger.error(f"Failed to get recent messages for thread {thread_id}: {e}")
        return []

def cleanup_expired_threads():
    """Remove conversation threads older than 1 month"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Calculate cutoff date (1 month ago)
        cutoff_date = datetime.now() - timedelta(days=30)
        
        cursor.execute("""
            DELETE FROM conversation_threads
            WHERE timestamp < ?
        """, (cutoff_date,))
        
        deleted_count = cursor.rowcount
        conn.commit()
        conn.close()
        
        if deleted_count > 0:
            logger.info(f"Cleaned up {deleted_count} expired messages")
        
        return deleted_count
        
    except Exception as e:
        logger.error(f"Failed to cleanup expired threads: {e}")
        return 0

def get_thread_stats(thread_id: str) -> Dict[str, int]:
    """Get statistics for a conversation thread"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                COUNT(*) as total_messages,
                COUNT(CASE WHEN role = 'user' THEN 1 END) as user_messages,
                COUNT(CASE WHEN role = 'assistant' THEN 1 END) as assistant_messages,
                MIN(timestamp) as first_message,
                MAX(timestamp) as last_message
            FROM conversation_threads
            WHERE thread_id = ?
        """, (thread_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                "total_messages": row[0],
                "user_messages": row[1], 
                "assistant_messages": row[2],
                "first_message": row[3],
                "last_message": row[4]
            }
        else:
            return {
                "total_messages": 0,
                "user_messages": 0,
                "assistant_messages": 0,
                "first_message": None,
                "last_message": None
            }
            
    except Exception as e:
        logger.error(f"Failed to get thread stats for {thread_id}: {e}")
        return {}

# Initialize database on module import
try:
    init_database()
    logger.info("Database module initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize database module: {e}")
