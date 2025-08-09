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
│   ├── constants.py
│   └── schemas.py
├── docker-compose.yml
├── env.example
├── README.md
└── run.py


## Local Development

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

This project is configured for Railway's **private networking**, keeping your backend secure and internal.

### Prerequisites
- Get your OpenAI API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
- Ensure you have sufficient credits in your OpenAI account

### Deploy Backend
1. Create a new Railway service named `backend`
2. Connect to this repository
3. Set the **Source Directory** to `backend`
4. Add required environment variables:
   - `OPENAI_API_KEY=your_actual_openai_api_key_here`
   - `HOST=::` (required for Railway's IPv6 networking)
   - `DEBUG=false` (optional)
   - `AI_PROVIDER=openai` (optional)
5. Railway will automatically detect the Dockerfile

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
