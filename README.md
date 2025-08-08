# AI Chatbot Kit

A simple AI chatbot with FastAPI backend and Streamlit frontend.

## Project Structure

```
ai-chatbot-kit/
├── backend/          # FastAPI backend service
├── frontend/         # Streamlit frontend service
└── docker-compose.yml # Local development setup
```

## Local Development

```bash
# Start both services
docker-compose up --build

# Access the application
# Frontend: http://localhost:8501
# Backend API: http://localhost:8000
```

## Railway Deployment

### Deploy Backend
1. Create a new Railway service
2. Connect to this repository
3. Set the **Source Directory** to `backend`
4. Railway will automatically detect the Dockerfile

### Deploy Frontend
1. Create another Railway service in the same project
2. Connect to this repository
3. Set the **Source Directory** to `frontend`
4. Set environment variable: `API_URL=https://your-backend-service.railway.app/api/chat/`

## API Endpoints

- `GET /api/health` - Health check
- `POST /api/chat/` - Chat endpoint (use `message` query parameter) 
