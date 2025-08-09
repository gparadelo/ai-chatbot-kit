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

This project is configured for Railway's **private networking**, keeping your backend secure and internal.

### Deploy Backend
1. Create a new Railway service named `backend`
2. Connect to this repository
3. Set the **Source Directory** to `backend`
4. Railway will automatically detect the Dockerfile

### Deploy Frontend
1. Create another Railway service named `frontend` in the same project
2. Connect to this repository
3. Set the **Source Directory** to `frontend`
4. Add environment variable: `API_URL=http://${{backend.RAILWAY_PRIVATE_DOMAIN}}:8000`
5. Add a public domain for the frontend (this is the only public service)

### Private Network Benefits
- Backend is completely private (no public access)
- Internal communication via Railway's private network
- Faster performance and enhanced security
- Automatic environment variable templating

## API Endpoints

- `GET /api/health/` - Health check
- `POST /api/chat/` - Chat endpoint (use `message` query parameter) 
