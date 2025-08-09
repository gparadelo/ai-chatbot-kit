# AI Chatbot Kit

A simple AI chatbot with FastAPI backend and Streamlit frontend.

## Project Structure

ai-chatbot-kit/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── chat.py
│   │   │   ├── health.py
│   │   │   └── agents.py              # 🆕 New agents router
│   │   ├── services/                  # 🆕 Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── chat_service.py
│   │   │   └── agent_service.py
│   │   ├── agents/                    # 🆕 CrewAI agents organization
│   │   │   ├── __init__.py
│   │   │   ├── base/                  # Base classes and utilities
│   │   │   │   ├── __init__.py
│   │   │   │   ├── agent_base.py
│   │   │   │   └── crew_base.py
│   │   │   ├── crews/                 # Crew definitions
│   │   │   │   ├── __init__.py
│   │   │   │   ├── research_crew.py
│   │   │   │   ├── content_crew.py
│   │   │   │   └── analysis_crew.py
│   │   │   ├── agents/                # Individual agent definitions
│   │   │   │   ├── __init__.py
│   │   │   │   ├── researcher.py
│   │   │   │   ├── writer.py
│   │   │   │   ├── analyst.py
│   │   │   │   └── reviewer.py
│   │   │   ├── tools/                 # Custom tools for agents
│   │   │   │   ├── __init__.py
│   │   │   │   ├── web_search.py
│   │   │   │   ├── file_processor.py
│   │   │   │   └── api_tools.py
│   │   │   └── tasks/                 # Task definitions
│   │   │       ├── __init__.py
│   │   │       ├── research_tasks.py
│   │   │       ├── content_tasks.py
│   │   │       └── analysis_tasks.py
│   │   ├── models/                    # 🆕 Pydantic models
│   │   │   ├── __init__.py
│   │   │   ├── chat.py
│   │   │   ├── agent.py
│   │   │   └── crew.py
│   │   └── utils/                     # 🆕 Utility functions
│   │       ├── __init__.py
│   │       ├── logging.py
│   │       └── exceptions.py
│   ├── Dockerfile
│   ├── main.py
│   ├── README.md
│   └── requirements.txt               # Update with CrewAI dependencies
├── frontend/
│   ├── pages/                         # 🆕 Multiple Streamlit pages
│   │   ├── 1_💬_Chat.py
│   │   ├── 2_🤖_Agents.py
│   │   └── 3_📊_Results.py
│   ├── components/                    # 🆕 Reusable UI components
│   │   ├── __init__.py
│   │   ├── chat_interface.py
│   │   └── agent_interface.py
│   ├── frontend.py
│   ├── Dockerfile
│   ├── README.md
│   └── requirements.txt
├── shared/                            # 🆕 Shared utilities between frontend/backend
│   ├── __init__.py
│   ├── chat_core.py                   # Single source of truth for chat logic
│   └── crews/
│       ├── __init__.py
│       ├── agent.yaml
│       ├── tasks.yaml
│       └── crew_ai.py
├── docker-compose.yml
├── env.example
├── README.md
└── run.py


## Local Development

- docker-compose spins up two services, but both import the shared core.
- Streamlit can run without API if `API_URL` is unset and `shared/` is available.

### Setup
1. Copy the environment file:
   ```bash
   cp env.example .env
   ```

2. Update `.env` with your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_actual_openai_api_key_here
   ```

3. Start both services:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000

## Railway Deployment

This project is configured for Railway's private networking, keeping your backend secure and internal.

- Backend and frontend Dockerfiles now COPY `shared/` so both can use the same logic.
- Streamlit can call the API (recommended) or run in direct-core mode if `API_URL` is not set.

## API Endpoints

- `GET /api/health/` - Health check
- `POST /api/chat/` - Chat endpoint (use `message` query parameter) 
