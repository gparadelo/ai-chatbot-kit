from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Application settings"""
    
    # API Configuration
    api_title: str = "AI Chatbot Kit API"
    api_description: str = "A modern FastAPI backend for AI chatbot applications"
    api_version: str = "1.0.0"
    debug: bool = False
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    
    # AI Model API Keys
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    
    # CORS Configuration
    cors_origins_str: str = ""
    cors_allow_methods: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    cors_allow_headers: List[str] = ["*"]
    cors_allow_credentials: bool = True
    
    @property
    def cors_origins(self) -> List[str]:
        """Parse CORS_ORIGINS from comma-separated string"""
        if not self.cors_origins_str:
            return []
        return [origin.strip() for origin in self.cors_origins_str.split(',') if origin.strip()]
    
    def validate_api_config(self) -> None:
        """Validate API configuration and report available models"""
        openai_available = bool(self.openai_api_key)
        anthropic_available = bool(self.anthropic_api_key)
        
        if not openai_available and not anthropic_available:
            raise ValueError("No API keys configured. Please set either OPENAI_API_KEY or ANTHROPIC_API_KEY")
        
        # Print status of available models
        print("🔑 API Key Status:")
        print(f"   OpenAI: {'✅' if openai_available else '❌'}")
        print(f"   Anthropic: {'✅' if anthropic_available else '❌'}")
        
        if openai_available:
            print(f"   OpenAI Key: {self.openai_api_key[:20]}...")
        if anthropic_available:
            print(f"   Anthropic Key: {self.anthropic_api_key[:20]}...")
    
    # Logging Configuration
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Rate Limiting Configuration
    rate_limit_enabled: bool = False
    rate_limit_requests_per_minute: int = 10
    rate_limit_burst_capacity: int = 20
    
    class Config:
        env_file = [".env", "../.env"]  # Try current dir first, then parent dir
        case_sensitive = False

# Create global settings instance
settings = Settings()

def get_settings() -> Settings:
    """Get application settings"""
    return settings 