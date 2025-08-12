# AI Chatbot Kit

A simple AI chatbot with FastAPI backend and Streamlit frontend.

## Project Structure

```
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
│   │   └── __init__.py
│   ├── data/                          # Data storage directory
│   ├── Dockerfile
│   ├── main.py                        # FastAPI application entry point
│   ├── requirements.txt
│   └── API_USAGE.md                   # Backend API documentation
├── frontend/
│   ├── frontend.py                    # Streamlit frontend application
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── env.example
├── RAILWAY_DEPLOYMENT_GUIDE.md        # Railway deployment instructions
└── README.md
```

## Features

- **FastAPI Backend**: Production-ready API with automatic documentation
- **Streamlit Frontend**: Beautiful chat interface with conversation history  
- **Multiple AI Models**: Support for OpenAI GPT and Anthropic Claude models
- **CrewAI Framework**: Easily extensible with agents and tools
- **Railway Deployment**: One-click deployment with private networking
- **API-First Design**: Use our frontend or build your own
- **Smart Configuration**: Automatic validation and error handling

## Architecture

The backend has been organized with **clear separation of concerns**:

- **API Layer** (`app/api/`): FastAPI routers, database, configuration, and business logic
- **AI Layer** (`app/ai/`): CrewAI crews, agents, tasks, and tools

The frontend contains a simple StreamLit implementation that uses the backend API.

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

## Using Only the Backend

Want to use your own frontend? Check out [backend/API_USAGE.md](backend/API_USAGE.md) for:
- How to enable CORS for your domain
- Complete API documentation
- Integration examples in JavaScript, Python, and cURL
- Security best practices

### Running the Crew Directly

To test the CrewAI crew independently without the full API:
```bash
cd backend/app/ai/crew
python main.py
```

This will start an interactive CLI chat session using the crew configuration.

## Limitations & What This Kit Doesn't Include

This is a **starter kit** designed to get you up and running quickly with a functional AI chatbot. Some use cases will require more development than others, depending on number of users, features required, security concerns, etc. Here are some things left out to keep it simple and easy to expand:

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

## Next Steps & Customization Ideas

Once you have the basic AI chatbot running, here are some ideas to enhance and customize your application:

### Adding New AI Agents
**How to start**: Create new agent classes in `backend/app/crew/agents/` following the existing pattern. Define role, goal, and backstory in YAML config files.
- **Documentation**: [CrewAI Agents Guide](https://docs.crewai.com/how-to/agents/)

### Integrating External Tools
**How to start**: Add tools to empower agents with capabilities ranging from web searching and data analysis to collaboration and delegating tasks among coworkers.
- **Documentation**: [CrewAI Tools Guide](https://docs.crewai.com/en/concepts/tools)

### Customizing Prompts & Responses
**How to start**: Edit the `backend/app/crew/config/agents.yaml` file to modify agent personalities, or update task descriptions in `tasks.yaml`.
- **Documentation**: [CrewAI Tasks Guide](https://docs.crewai.com/en/concepts/tasks)
- **Prompt Engineering**: [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

### API Extensions
**How to start**: Add new endpoints in `backend/app/routers/` and implement the business logic in `backend/app/services/`. 
- **Documentation**: [FastAPI Docs](https://fastapi.tiangolo.com/)

### 💡 Advanced AI Features
**How to start**: Implement memory systems using vector databases like ChromaDB, and create multi-agent workflows by chaining multiple agents together.
- **Documentation**: [CrewAI Memory](https://docs.crewai.com/en/concepts/memory), [ChromaDB Guide](https://docs.trychroma.com/)
