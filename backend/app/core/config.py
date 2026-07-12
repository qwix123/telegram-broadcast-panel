from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Telegram
    api_id: int = int(os.getenv("API_ID", "0"))
    api_hash: str = os.getenv("API_HASH", "")
    
    # Proxy
    proxy_enabled: bool = os.getenv("PROXY_ENABLED", "false").lower() == "true"
    proxy_type: str = os.getenv("PROXY_TYPE", "http")
    proxy_server: Optional[str] = os.getenv("PROXY_SERVER")
    proxy_port: Optional[int] = os.getenv("PROXY_PORT")
    proxy_username: Optional[str] = os.getenv("PROXY_USERNAME")
    proxy_password: Optional[str] = os.getenv("PROXY_PASSWORD")
    
    # Database
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    database_echo: bool = os.getenv("DATABASE_ECHO", "false").lower() == "true"
    
    # Backend
    backend_host: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    backend_port: int = int(os.getenv("BACKEND_PORT", "8000"))
    backend_debug: bool = os.getenv("BACKEND_DEBUG", "false").lower() == "true"
    
    # Security
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()