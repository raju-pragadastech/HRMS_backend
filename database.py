from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_database_url():
    """Get database URL with proper configuration for Railway PostgreSQL"""
    db_url = settings.DATABASE_URL
    
    if db_url.startswith("postgresql://"):
        logger.info("Using PostgreSQL database from Railway")
        
        # Add SSL mode if not present
        if "sslmode" not in db_url:
            if "?" in db_url:
                db_url += "&sslmode=require"
            else:
                db_url += "?sslmode=require"
        
        logger.info(f"PostgreSQL URL configured with SSL: {db_url}")
        return db_url
    else:
        logger.info("Using SQLite database for local development")
        return db_url

def get_engine_config():
    """Get engine configuration for Railway PostgreSQL"""
    db_url = get_database_url()
    
    if db_url.startswith("postgresql://"):
        # Railway PostgreSQL specific configuration
        return {
            "pool_pre_ping": True,      # Verify connection before use
            "pool_recycle": 300,        # Recycle connections every 5 minutes
            "pool_size": settings.DB_POOL_SIZE,            # Connection pool size
            "max_overflow": settings.DB_MAX_OVERFLOW,         # Maximum overflow connections
            "echo": False,              # Set to True for SQL query logging
            "connect_args": {
                "sslmode": settings.DB_SSL_MODE,   # Require SSL connection
                "connect_timeout": 10,  # Connection timeout
                "application_name": "hrms_backend"  # Application identifier
            }
        }
    else:
        # SQLite configuration
        return {
            "echo": False
        }

# Create engine with appropriate configuration
engine = create_engine(
    get_database_url(),
    **get_engine_config()
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

def test_connection():
    """Test database connection"""
    try:
        with engine.connect() as conn:
            if engine.dialect.name == "postgresql":
                result = conn.execute("SELECT version()")
                version = result.fetchone()[0]
                logger.info(f"PostgreSQL connection successful: {version}")
            else:
                result = conn.execute("SELECT 1")
                logger.info("SQLite connection successful")
            return True
    except Exception as e:
        logger.error(f"Database connection test failed: {e}")
        return False
