# Conversation Thread Persistence

## Overview
Simple and efficient conversation threading using SQLite for production deployment on Railway.

## Features

### 1. Thread-Based Conversations
- **Thread ID**: Each conversation has a unique thread identifier
- **Persistence**: Conversations survive application restarts  
- **TTL**: Automatic cleanup after 1 month
- **Production Ready**: SQLite database with Railway volume persistence

### 2. Context-Aware Responses
- **Last 5 Conversations**: Automatically includes recent conversation history
- **Intelligent Prompting**: LLM receives full context to maintain conversation continuity
- **Seamless Experience**: Users experience natural conversation flow

### 3. Database Schema
```sql
CREATE TABLE conversation_threads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    thread_id TEXT NOT NULL,
    role TEXT NOT NULL,  -- 'user' or 'assistant'
    content TEXT NOT NULL,
    timestamp DATETIME NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## API Endpoints

### Chat with Thread Persistence
```http
POST /api/chat/
Content-Type: application/json

{
  "message": "Hello, how are you?",
  "thread_id": "optional-thread-id"  // Auto-generated if not provided
}
```

**Response:**
```json
{
  "response": "AI response with full conversation context",
  "thread_id": "uuid-thread-identifier"
}
```

### Get Thread History
```http
GET /api/chat/thread/{thread_id}/history
```

### Delete Thread
```http
DELETE /api/chat/thread/{thread_id}
```

## Context Prompting System

The system automatically builds context-aware prompts:

```
MEMORY CONTEXT: Below are the last conversations between the user and assistant:

CONVERSATION 1:
User: What's the weather like?
Assistant: I'd be happy to help with weather information...

CONVERSATION 2:
User: Thanks, what about tomorrow?
Assistant: For tomorrow's forecast...

CURRENT USER QUERY: Will it rain this weekend?

INSTRUCTION: Before responding to the current query, analyze the conversation history above to identify:
- Relevant context from previous discussions
- User preferences and patterns
- Ongoing topics or unresolved questions
- Any referenced information from past conversations

Then, reformulate your understanding of the current query to incorporate all relevant context from the conversation history. Frame your response as if you have full awareness of the entire conversation thread, ensuring continuity and personalized assistance.

Respond to the current query with this integrated context in mind.
```

## Railway Deployment

### Volume Setup
1. Create a Railway volume in your backend service
2. Mount path: `/app/data`
3. Size: 1GB (recommended for conversation storage)

### Database Location
- **File**: `/app/data/conversations.db`
- **Automatic Creation**: Database and tables created on first run
- **Backup**: Volume ensures persistence across deployments

## Automatic Cleanup

### TTL Management
- **Cleanup Trigger**: Runs on each chat request (simple approach)
- **Retention**: 30 days from message timestamp
- **Performance**: Minimal impact, runs in background

### Production Considerations
For high-traffic production environments, consider:
- Background cleanup task (cron job)
- Database indexing optimization
- Conversation archiving for long-term storage

## Usage Examples

### Start New Conversation
```bash
curl -X POST "http://localhost:8000/api/chat/" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, I need help with Python"}'
```

### Continue Existing Conversation
```bash
curl -X POST "http://localhost:8000/api/chat/" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Can you show me an example?",
    "thread_id": "existing-thread-uuid"
  }'
```

### View Conversation History
```bash
curl "http://localhost:8000/api/chat/thread/existing-thread-uuid/history"
```

## Benefits

### User Experience
- **Natural Conversations**: No need to repeat context
- **Seamless Flow**: Pick up where you left off
- **Intelligent Responses**: AI understands conversation continuity

### Technical Advantages  
- **Simple Implementation**: No complex vector databases
- **Fast Performance**: Direct SQLite queries
- **Railway Compatible**: Works perfectly with volume persistence
- **Production Ready**: Handles restarts and scaling

### Development Benefits
- **Easy Debugging**: View conversation history directly
- **Simple Maintenance**: Standard SQL operations
- **Flexible**: Easy to extend with additional features

## Future Enhancements
- WebSocket support for real-time conversations
- Conversation search and filtering
- Export conversation history
- Conversation analytics and insights
