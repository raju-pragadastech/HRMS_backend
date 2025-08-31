#!/usr/bin/env python3
"""
Railway Deployment Script for HRMS with PostgreSQL SSL
This script handles the deployment process on Railway with PostgreSQL
"""

import os
import logging
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_railway_cli():
    """Check if Railway CLI is installed"""
    try:
        result = subprocess.run(['railway', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info(f"Railway CLI found: {result.stdout.strip()}")
            return True
        else:
            logger.error("Railway CLI not working properly")
            return False
    except FileNotFoundError:
        logger.error("Railway CLI not found. Please install it first.")
        return False

def check_git_repo():
    """Check if we're in a git repository"""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info("Git repository found")
            return True
        else:
            logger.error("Not a git repository")
            return False
    except FileNotFoundError:
        logger.error("Git not found")
        return False

def check_railway_project():
    """Check if Railway project is linked"""
    try:
        result = subprocess.run(['railway', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info("Railway project is linked")
            return True
        else:
            logger.info("Railway project not linked")
            return False
    except Exception as e:
        logger.error(f"Error checking Railway status: {e}")
        return False

def link_railway_project():
    """Link to Railway project"""
    try:
        logger.info("Linking to Railway project...")
        result = subprocess.run(['railway', 'link'], input='\n', text=True, capture_output=True)
        if result.returncode == 0:
            logger.info("Successfully linked to Railway project")
            return True
        else:
            logger.error(f"Failed to link Railway project: {result.stderr}")
            return False
    except Exception as e:
        logger.error(f"Error linking Railway project: {e}")
        return False

def deploy_to_railway():
    """Deploy to Railway"""
    try:
        logger.info("Deploying to Railway...")
        result = subprocess.run(['railway', 'up'], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info("Successfully deployed to Railway")
            logger.info("Deployment output:")
            logger.info(result.stdout)
            return True
        else:
            logger.error(f"Deployment failed: {result.stderr}")
            return False
    except Exception as e:
        logger.error(f"Error deploying to Railway: {e}")
        return False

def check_environment_variables():
    """Check required environment variables"""
    required_vars = ['DATABASE_URL', 'JWT_SECRET']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        logger.warning(f"Missing environment variables: {missing_vars}")
        logger.info("Please set these in Railway dashboard → Variables tab")
        return False
    
    logger.info("All required environment variables are set")
    return True

def show_railway_url():
    """Show Railway deployment URL"""
    try:
        result = subprocess.run(['railway', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info("Railway deployment status:")
            logger.info(result.stdout)
        else:
            logger.error("Could not get Railway status")
    except Exception as e:
        logger.error(f"Error getting Railway status: {e}")

def main():
    """Main deployment function"""
    logger.info("🚀 Starting Railway deployment for HRMS with PostgreSQL...")
    
    # Check prerequisites
    if not check_git_repo():
        logger.error("Please run this script from a git repository")
        sys.exit(1)
    
    if not check_railway_cli():
        logger.error("Please install Railway CLI first: npm install -g @railway/cli")
        sys.exit(1)
    
    # Check if project is linked
    if not check_railway_project():
        logger.info("Linking to Railway project...")
        if not link_railway_project():
            logger.error("Failed to link Railway project")
            sys.exit(1)
    
    # Check environment variables
    if not check_environment_variables():
        logger.warning("Some environment variables are missing")
        logger.info("You can set them in Railway dashboard or continue with deployment")
        response = input("Continue with deployment? (y/N): ")
        if response.lower() != 'y':
            logger.info("Deployment cancelled")
            sys.exit(0)
    
    # Deploy
    if deploy_to_railway():
        logger.info("✅ Deployment successful!")
        show_railway_url()
        
        logger.info("\n📋 Next steps:")
        logger.info("1. Check your Railway dashboard for the deployment URL")
        logger.info("2. Test the health endpoint: /api/health")
        logger.info("3. Initialize PostgreSQL database with: python init_postgresql_db.py")
        logger.info("4. Update your Flutter app with the new API URL")
        
    else:
        logger.error("❌ Deployment failed!")
        logger.info("Check the error messages above and try again")
        sys.exit(1)

if __name__ == "__main__":
    main()
