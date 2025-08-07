# AI Chatbot Kit - FastAPI Backend

A simple, scalable FastAPI backend for AI chatbot applications with basic chat functionality and health monitoring.

## Features

- 🚀 **FastAPI** - High-performance, modern Python web framework
- 💬 **Chat Endpoint** - Send messages and get mocked responses
- 📊 **Health Monitoring** - Simple health check
- 📝 **Auto Documentation** - Interactive API docs with Swagger UI
- 🐳 **Docker Ready** - Containerization support

## Quick Start

### Prerequisites

- Python 3.8+
- pip or poetry

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-chatbot-kit
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables (optional)**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- **Interactive API Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## API Endpoints

### Chat Endpoints

- `POST /chat?message=your_message` - Send a message and get mocked response

### Health Endpoints

- `GET /health/` - Health check

## Configuration

The application uses environment variables for configuration. Copy `env.example` to `.env` and modify as needed:

```bash
# API Configuration
DEBUG=false
HOST=0.0.0.0
PORT=8000

# CORS Configuration
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]

# Logging
LOG_LEVEL=INFO
```

## Project Structure

```
ai-chatbot-kit/
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py          # Configuration management
│   └── routers/
│       ├── __init__.py
│       ├── chat.py            # Chat endpoint
│       └── health.py          # Health check endpoint
├── main.py                    # Application entry point
├── run.py                     # Startup script
├── requirements.txt           # Python dependencies
├── env.example               # Environment variables template
├── Dockerfile                # Container configuration
├── docker-compose.yml        # Multi-service setup
├── .gitignore               # Git exclusions
└── README.md                # This file
```

## Development

### Running in Development Mode

```bash
python run.py
```

The server will run with auto-reload enabled.

### Running with Uvicorn

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Docker Support

### Build and Run with Docker

```bash
# Build the image
docker build -t ai-chatbot-kit .

# Run the container
docker run -p 8000:8000 ai-chatbot-kit
```

### Docker Compose

```bash
docker-compose up -d
```

## Example Usage

### Send a chat message:
```bash
curl -X POST "http://localhost:8000/chat?message=Hello%20world"
```

Response:
```json
{
  "response": "Mock response to: Hello world",
  "timestamp": "2024-01-01T12:00:00"
}
```

### Health check:
```bash
curl "http://localhost:8000/health"
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "version": "1.0.0",
  "uptime": 123.45
}
```

## Extending the Application

### Adding Real AI Integration

1. Create an AI service module in `app/core/`
2. Update the chat endpoint to use your AI service
3. Add configuration for your AI provider

### Adding New Endpoints

1. Create a new router in `app/routers/`
2. Define your endpoints using FastAPI decorators
3. Include the router in `main.py`

### Adding Conversation Management

1. Add database models for conversations
2. Create conversation management endpoints
3. Update the chat endpoint to store conversation history

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue on GitHub or contact the development team. 