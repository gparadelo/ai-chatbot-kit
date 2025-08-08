# Backend API

FastAPI backend service for the AI Chatbot Kit.

## Local Development

```bash
cd backend
docker build -t backend .
docker run -p 8000:8000 backend
```

## Railway Deployment

Deploy this directory as a Railway service. Railway will automatically detect the Dockerfile.

## API Endpoints

- `GET /api/health` - Health check
- `POST /api/chat/` - Chat endpoint (use `message` query parameter)
