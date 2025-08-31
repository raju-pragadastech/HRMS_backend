#!/usr/bin/env python3
"""
Test Railway PostgreSQL Connection
Run this to verify your database connection is working
"""

import os
import logging
from sqlalchemy import create_engine, text

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_railway_postgresql():
    """Test Railway PostgreSQL connection"""
    
    # Your Railway PostgreSQL connection string
    DATABASE_URL = "postgresql://postgres:erLUuZNgBeMWXVZhKdmuKWEdrvQjUaeP@turntable.proxy.rlwy.net:34996/railway?sslmode=require"
    
    logger.info("Testing Railway PostgreSQL connection...")
    logger.info(f"Database URL: {DATABASE_URL}")
    
    try:
        # Create engine with SSL configuration
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            pool_recycle=300,
            pool_size=5,
            max_overflow=10,
            echo=False,
            connect_args={
                "sslmode": "require",
                "connect_timeout": 10,
                "application_name": "hrms_backend_test"
            }
        )
        
        # Test connection
        with engine.connect() as conn:
            logger.info("✅ Successfully connected to Railway PostgreSQL!")
            
            # Test basic query
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            logger.info(f"PostgreSQL Version: {version}")
            
            # Test database name
            result = conn.execute(text("SELECT current_database()"))
            db_name = result.fetchone()[0]
            logger.info(f"Connected to database: {db_name}")
            
            # Test user
            result = conn.execute(text("SELECT current_user"))
            user = result.fetchone()[0]
            logger.info(f"Connected as user: {user}")
            
            # Test if we can create tables (read-only test)
            result = conn.execute(text("SELECT 1 as test"))
            test_value = result.fetchone()[0]
            logger.info(f"Query test successful: {test_value}")
            
            logger.info("🎉 All database tests passed!")
            return True
            
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        logger.error("Please check:")
        logger.error("1. Your Railway PostgreSQL service is running")
        logger.error("2. The connection string is correct")
        logger.error("3. SSL is properly configured")
        return False

def test_environment_setup():
    """Test if environment is properly configured"""
    logger.info("Testing environment setup...")
    
    # Check if we can import required modules
    try:
        from config import settings
        logger.info("✅ Config imported successfully")
        
        from database import test_connection
        logger.info("✅ Database module imported successfully")
        
        return True
    except Exception as e:
        logger.error(f"❌ Environment setup failed: {e}")
        return False

def main():
    """Main test function"""
    logger.info("🚀 Starting Railway PostgreSQL Connection Test...")
    
    # Test environment setup
    if not test_environment_setup():
        logger.error("Environment setup failed. Please check your dependencies.")
        return False
    
    # Test direct database connection
    if test_railway_postgresql():
        logger.info("\n🎉 SUCCESS: Your Railway PostgreSQL connection is working!")
        logger.info("\n📋 Next steps:")
        logger.info("1. Set DATABASE_URL in your environment variables")
        logger.info("2. Run: python init_postgresql_db.py")
        logger.info("3. Deploy to Railway with: railway up")
        return True
    else:
        logger.error("\n❌ FAILED: Railway PostgreSQL connection test failed")
        logger.error("Please check your connection string and Railway service status")
        return False

if __name__ == "__main__":
    main()
