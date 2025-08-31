import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Railway PostgreSQL connection
    # Railway provides DATABASE_URL in format: postgresql://username:password@host:port/database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./hrms.db")
    
    # Fallback to SQLite if no DATABASE_URL (for local development)
    if not DATABASE_URL or DATABASE_URL.startswith("sqlite"):
        DATABASE_URL = "sqlite:///./hrms.db"
    
    # JWT Configuration
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-super-secret-jwt-key-change-this-in-production")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Database Configuration
    DB_SSL_MODE: str = os.getenv("DB_SSL_MODE", "require")
    DB_POOL_SIZE: int = int(os.getenv("DB_POOL_SIZE", "10"))
    DB_MAX_OVERFLOW: int = int(os.getenv("DB_MAX_OVERFLOW", "20"))

settings = Settings()
