# Using the Backend with Your Own Frontend

This backend is designed to work seamlessly with your own frontend while maintaining security.

## Configuration

### Environment Variables

The backend uses these key environment variables:

#### AI Model Configuration
- `OPENAI_API_KEY`: API key for OpenAI models (GPT-4, GPT-3.5-turbo, etc.)
- `ANTHROPIC_API_KEY`: API key for Anthropic models (Claude-3, etc.)
- **Note**: Model selection is configured in `backend/app/crew/config/agents.yaml`

#### CORS Configuration
- `CORS_ORIGINS_STR`: Comma-separated list of allowed frontend domains

## Default Behavior (Recommended)

By default, **CORS is disabled** for security. This is perfect for:
- Railway private networking (your frontend connects via private connection)
- Internal company tools
- Secure deployments

## Enable CORS for Custom Frontend

If you want to use your own frontend that connects directly to the backend:

### 1. Set Environment Variable

Add this to your `.env` file:

```bash
# Allow specific frontend domains
CORS_ORIGINS_STR=https://myapp.com,https://app.mycompany.com

# Or for local development
CORS_ORIGINS_STR=http://localhost:3000,http://localhost:5173
```

### 2. Restart the Backend

The backend will automatically enable CORS for your specified domains.

## API Endpoints

### Chat
- **POST** `/api/chat/`
- **Body**: `{"message": "Hello", "thread_id": "optional-uuid"}`
- **Response**: `{"response": "AI response", "thread_id": "uuid"}`

### Thread History
- **GET** `/api/chat/thread/{thread_id}/history`
- **Response**: `{"thread_id": "uuid", "messages": [...], "total_messages": 5}`

- **DELETE** `/api/chat/thread/{thread_id}`
- **Response**: `{"success": true, "deleted_messages": 5, "thread_id": "uuid"}`

### Health Check
- **GET** `/api/health/`
- **Response**: `{"status": "healthy", "timestamp": "..."}`

## Example Frontend Integration

### JavaScript/Fetch
```javascript
const response = await fetch('https://your-backend.com/api/chat/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'Hello AI!',
    thread_id: 'optional-thread-id'
  })
});

const data = await response.json();
console.log(data.response);
```

### Python/Requests
```python
import requests

response = requests.post('https://your-backend.com/api/chat/', json={
    'message': 'Hello AI!',
    'thread_id': 'optional-thread-id'
})

data = response.json()
print(data['response'])
```

### cURL
```bash
curl -X POST "https://your-backend.com/api/chat/" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello AI!", "thread_id": "optional-thread-id"}'
```

## Security Notes

- **Never use `CORS_ORIGINS=*`** in production
- Only allow domains you trust
- Consider adding authentication for production use
- The backend validates all inputs and handles errors gracefully

## Need Help?

Check the API documentation at `/docs` when your backend is running!
