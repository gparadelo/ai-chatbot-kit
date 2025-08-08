# Frontend

Streamlit frontend for the AI Chatbot Kit.

## Local Development

```bash
cd frontend
docker build -t frontend .
docker run -p 8501:8501 -e API_URL=http://localhost:8000/api/chat/ frontend
```

## Railway Deployment

Deploy this directory as a Railway service. Railway will automatically detect the Dockerfile.

## Environment Variables

- `API_URL` - URL of the backend API (required)
- `DEBUG` - Enable debug mode (optional)
