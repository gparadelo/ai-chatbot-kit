# AI Chatbot Kit

A simple AI chatbot with FastAPI backend and Streamlit frontend.

## Project Structure

ai-chatbot-kit/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api/                       # API Layer - FastAPI, database, configuration
│   │   │   ├── __init__.py
│   │   │   ├── core/                  # Configuration and settings
│   │   │   │   ├── __init__.py
│   │   │   │   └── config.py
│   │   │   ├── models/                # Pydantic data models
│   │   │   │   ├── __init__.py
│   │   │   │   └── chat.py
│   │   │   ├── routers/               # FastAPI route handlers
│   │   │   │   ├── __init__.py
│   │   │   │   ├── chat.py
│   │   │   │   └── health.py
│   │   │   ├── services/              # Business logic services
│   │   │   │   ├── __init__.py
│   │   │   │   └── chat_service.py
│   │   │   └── database.py            # Database operations
│   │   ├── ai/                        # AI Layer - CrewAI, agents, tasks, tools
│   │   │   ├── __init__.py
│   │   │   ├── crew/                  # CrewAI crew definitions
│   │   │   │   ├── config/            # Agent and task configurations
│   │   │   │   │   ├── agents.yaml
│   │   │   │   │   └── tasks.yaml
│   │   │   │   ├── crew.py            # Main crew implementation
│   │   │   │   └── main.py            # Crew initialization
│   │   │   └── tools/                 # AI tools and utilities
│   │   │       └── __init__.py
│   ├── Dockerfile
│   ├── main.py                        # FastAPI application entry point
│   ├── requirements.txt
│   └── STRUCTURE.md                   # Backend architecture documentation
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


## Features

- **FastAPI Backend**: Production-ready API with automatic documentation
- **Streamlit Frontend**: Beautiful chat interface with conversation history  
- **Multiple AI Models**: Support for OpenAI GPT and Anthropic Claude models
- **CrewAI Framework**: Easily extensible with agents and tools
- **Railway Deployment**: One-click deployment with private networking
- **API-First Design**: Use our frontend or build your own
- **Smart Configuration**: Automatic validation and error handling

## Limitations & What This Kit Doesn't Include

This is a **starter kit** designed to get you up and running quickly with a functional AI chatbot. Some use cases will require more development than others, depending on number of users, features required, security concerns, etc. Here are some things we left out to keep it simple and easy to expand:

### Performance & Scale Limitations
❌ **Rate limiting** - No request throttling or limits  
❌ **Database pooling** - No connection pooling for database operations  
❌ **Caching layer** - No Redis or in-memory caching  
❌ **Load balancing** - Single instance deployment only  
❌ **Horizontal scaling** - Not designed for multiple backend instances  

### Security & Authentication
❌ **User authentication** - No user login or session management  
❌ **API key management** - No user-specific API key handling  
❌ **Request validation** - Basic validation only  
❌ **Rate limiting per user** - No individual user quotas  

### Monitoring & Observability
❌ **Monitoring/metrics** - No performance or usage metrics collection  
❌ **Logging aggregation** - Basic console logging only  
❌ **Performance profiling** - No APM tools  
❌ **Health check alerts** - Basic health endpoint only  

### Testing & Quality
❌ **Extensive testing** - Limited test coverage  
❌ **Code coverage** - No test coverage requirements  
❌ **Integration tests** - Manual testing recommended  
❌ **Performance tests** - No load testing included  

### Production Features
❌ **Backup strategies** - No automated database backups  
❌ **CDN integration** - No static asset optimization  
❌ **Database migrations** - No schema versioning  
❌ **Environment-specific configs** - Single config approach  

While many use cases won't need most of these features, please keep in mind these limitations.

## Architecture Benefits

The backend has been reorganized with **clear separation of concerns**:

- **API Layer** (`app/api/`): FastAPI routers, database, configuration, and business logic
- **AI Layer** (`app/ai/`): CrewAI crews, agents, tasks, and tools

This structure provides:
- **Maintainability**: Easier to modify one layer without affecting the other
- **Testing**: Can test API logic independently from AI logic  
- **Scalability**: Can scale AI services separately from API services
- **Reusability**: AI components can be reused in different contexts
- **Organization**: Logical grouping makes the codebase easier to navigate

## Prerequisites

Before running this project, ensure you have the following installed on your system:

### Required Software
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)

### Optional Software (Not Needed: In case you want to run the code locally without Docker)
- **Python**: [Install Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually comes with Python)
- Install libraries in `requirements.txt` files.

### LLM Connection
- Get your OpenAI API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
- 


### Setup
1. Copy the `env.example` file and rename it to `.env`:
   Using the terminal:
   ```bash
   cp env.example .env
   ```

2. Update `.env` with your API keys:
   ```
   # Set at least one API key to enable AI functionality
   OPENAI_API_KEY=your_actual_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Note: Model selection is configured in backend/app/crew/config/agents.yaml
   ```

3. Start both services (frontend and backend):
   ```bash
   docker-compose up --build
   ```
   After the project has been built, you can restart it with:
   ```bash
   docker-compose up
   ```

4. Access the application:
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000

## Railway Deployment

This project is configured for Railway's **private networking**, keeping your backend secure and internal.

You can choose to follow the step-by-step tutorial which will use Railway to deploy the project. If you want to use another hosting service, please feel free to do so. 

### How to deploy the project: 

#### Deploy Backend
1. Create a new Railway service named `backend`
2. Connect to this repository
3. Set the **Source Directory** to `backend`
4. Add required environment variables:
   - `OPENAI_API_KEY=your_actual_openai_api_key_here` (if using OpenAI)
   - `ANTHROPIC_API_KEY=your_anthropic_api_key_here` (if using Anthropic)
   - `HOST=::` (required for Railway's IPv6 networking)
   - **Note**: Model selection is configured per agent in `backend/app/crew/config/agents.yaml`
5. Railway will automatically detect the Dockerfile
6. Create a new Railway volume attatched to `backend` mounted on `/data`

#### Deploy Frontend
1. Create another Railway service named `frontend` in the same project
2. Connect to this repository
3. Set the **Source Directory** to `frontend`
4. Add environment variable: `API_URL=http://${{backend.RAILWAY_PRIVATE_DOMAIN}}:8000`
5. Add a public domain for the frontend (this is the only public service)

## API Endpoints

- `GET /api/health/` - Health check
- `POST /api/chat/` - Chat endpoint (use `message` and `thread_id` query parameters)

## Using Only the Backend

Want to use your own frontend? Check out [backend/API_USAGE.md](backend/API_USAGE.md) for:
- How to enable CORS for your domain
- Complete API documentation
- Integration examples in JavaScript, Python, and cURL
- Security best practices
