#!/usr/bin/env python3
"""
Environment Setup Script for Railway PostgreSQL
This script helps you set up the environment variables for your Railway deployment
"""

import os
from pathlib import Path

def create_env_file():
    """Create .env file with Railway PostgreSQL configuration"""
    
    # Your Railway PostgreSQL connection string
    railway_db_url = "postgresql://postgres:erLUuZNgBeMWXVZhKdmuKWEdrvQjUaeP@turntable.proxy.rlwy.net:34996/railway?sslmode=require"
    
    env_content = f"""# Railway PostgreSQL Configuration
DATABASE_URL={railway_db_url}

# JWT Configuration
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database Configuration
DB_SSL_MODE=require
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20

# Railway Configuration
PORT=8000
"""
    
    # Create .env file
    env_file = Path(".env")
    with open(env_file, "w") as f:
        f.write(env_content)
    
    print(f"✅ Created .env file with Railway PostgreSQL configuration")
    print(f"📁 File location: {env_file.absolute()}")
    return True

def show_railway_variables():
    """Show the environment variables you need to set in Railway dashboard"""
    
    print("\n🔧 Environment Variables for Railway Dashboard:")
    print("=" * 50)
    print("Go to Railway Dashboard → Your Project → Variables tab")
    print("Add these variables:")
    print()
    
    variables = {
        "DATABASE_URL": "postgresql://postgres:erLUuZNgBeMWXVZhKdmuKWEdrvQjUaeP@turntable.proxy.rlwy.net:34996/railway?sslmode=require",
        "JWT_SECRET": "your-super-secret-jwt-key-change-this-in-production",
        "JWT_ALGORITHM": "HS256",
        "ACCESS_TOKEN_EXPIRE_MINUTES": "30",
        "DB_SSL_MODE": "require",
        "DB_POOL_SIZE": "10",
        "DB_MAX_OVERFLOW": "20"
    }
    
    for key, value in variables.items():
        print(f"{key}={value}")
    
    print("\n💡 Tips:")
    print("- Change JWT_SECRET to a strong, unique secret")
    print("- DATABASE_URL is already configured with SSL")
    print("- These variables will be automatically used by your app")

def main():
    """Main setup function"""
    print("🚀 Railway PostgreSQL Environment Setup")
    print("=" * 40)
    
    # Create .env file for local development
    if create_env_file():
        print("\n✅ Local environment configured successfully!")
    
    # Show Railway dashboard variables
    show_railway_variables()
    
    print("\n📋 Next Steps:")
    print("1. Test your database connection: python test_railway_db.py")
    print("2. Initialize database: python init_postgresql_db.py")
    print("3. Deploy to Railway: railway up")
    print("4. Set environment variables in Railway dashboard")
    
    print("\n🎉 Your Railway PostgreSQL connection is ready!")

if __name__ == "__main__":
    main()
