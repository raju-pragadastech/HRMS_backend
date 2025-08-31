#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import User
from auth import get_password_hash
from crud import get_user_by_email

def create_test_user():
    db = SessionLocal()
    try:
        # Check if test user already exists
        existing_user = get_user_by_email(db, "admin@hrms.com")
        if existing_user:
            print("✅ Test user already exists!")
            print(f"Email: admin@hrms.com")
            print(f"Employee ID: {existing_user.employee_id}")
            print(f"Password: admin123")
            return
        
        # Create test user
        test_user = User(
            email="admin@hrms.com",
            employee_id="EMP001",
            hashed_password=get_password_hash("admin123"),
            role="admin",
            is_active=True
        )
        
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
        
        print("✅ Test user created successfully!")
        print(f"Email: admin@hrms.com")
        print(f"Employee ID: EMP001")
        print(f"Password: admin123")
        print(f"Role: admin")
        
    except Exception as e:
        print(f"❌ Error creating test user: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Creating test user for HRMS application...")
    create_test_user()
