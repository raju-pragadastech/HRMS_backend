import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Using SQLite for now - can be changed to PostgreSQL later
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./hrms.db")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-super-secret-jwt-key-change-this-in-production")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

settings = Settings()
