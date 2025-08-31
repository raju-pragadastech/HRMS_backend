#!/usr/bin/env python3
"""
PostgreSQL Database Initialization Script for HRMS
Run this after setting up your PostgreSQL database on Railway
"""

import os
import logging
from datetime import datetime, date
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import settings
from models import Base, User, Employee, Attendance, Leave, Payroll
from crud import create_user, create_employee
from auth import get_password_hash

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_postgresql_database():
    """Initialize PostgreSQL database with tables and sample data"""
    try:
        # Use Railway PostgreSQL connection
        railway_db_url = "postgresql://postgres:erLUuZNgBeMWXVZhKdmuKWEdrvQjUaeP@turntable.proxy.rlwy.net:34996/railway?sslmode=require"
        
        # Create engine for PostgreSQL
        engine = create_engine(
            railway_db_url,
            pool_pre_ping=True,
            pool_recycle=300,
            echo=True  # Set to False in production
        )
        
        # Test connection
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            logger.info(f"PostgreSQL connection successful: {version}")
            
            # Test database name
            result = conn.execute(text("SELECT current_database()"))
            db_name = result.fetchone()[0]
            logger.info(f"Connected to database: {db_name}")
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("PostgreSQL tables created successfully")
        
        # Create session
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        try:
            # Check if data already exists
            existing_users = db.query(User).count()
            if existing_users > 0:
                logger.info("Database already contains data, skipping initialization")
                return True
            
            # Create sample users
            sample_users = [
                {
                    "email": "admin@hrms.com",
                    "employee_id": "EMP001",
                    "password": "admin123",
                    "role": "hr"
                },
                {
                    "email": "manager@hrms.com",
                    "employee_id": "EMP002",
                    "password": "manager123",
                    "role": "manager"
                },
                {
                    "email": "employee@hrms.com",
                    "employee_id": "EMP003",
                    "password": "employee123",
                    "role": "employee"
                }
            ]
            
            created_users = []
            for user_data in sample_users:
                # Create user
                user_create = {
                    "email": user_data["email"],
                    "employee_id": user_data["employee_id"],
                    "hashed_password": get_password_hash(user_data["password"]),
                    "role": user_data["role"]
                }
                
                user = create_user(db=db, user=user_create)
                created_users.append(user)
                logger.info(f"Created user: {user.email} with role: {user.role}")
            
            # Create sample employees
            sample_employees = [
                {
                    "user_id": created_users[0].id,
                    "first_name": "Admin",
                    "last_name": "User",
                    "phone": "+1234567890",
                    "address": "123 Admin Street, City, State",
                    "department": "Human Resources",
                    "position": "HR Manager",
                    "hire_date": date(2023, 1, 15),
                    "salary": 75000.00
                },
                {
                    "user_id": created_users[1].id,
                    "first_name": "John",
                    "last_name": "Manager",
                    "phone": "+1234567891",
                    "address": "456 Manager Ave, City, State",
                    "department": "Engineering",
                    "position": "Engineering Manager",
                    "hire_date": date(2023, 2, 20),
                    "salary": 85000.00
                },
                {
                    "user_id": created_users[2].id,
                    "first_name": "Jane",
                    "last_name": "Employee",
                    "phone": "+1234567892",
                    "address": "789 Employee Blvd, City, State",
                    "department": "Engineering",
                    "position": "Software Developer",
                    "hire_date": date(2023, 3, 10),
                    "salary": 65000.00
                }
            ]
            
            for emp_data in sample_employees:
                employee = create_employee(db=db, employee=emp_data, user_id=emp_data["user_id"])
                logger.info(f"Created employee: {employee.first_name} {employee.last_name}")
            
            # Create sample attendance records
            sample_attendance = [
                {
                    "employee_id": 1,
                    "date": date.today(),
                    "check_in": datetime.now().replace(hour=9, minute=0, second=0, microsecond=0),
                    "check_out": datetime.now().replace(hour=17, minute=0, second=0, microsecond=0),
                    "status": "present"
                },
                {
                    "employee_id": 2,
                    "date": date.today(),
                    "check_in": datetime.now().replace(hour=8, minute=30, second=0, microsecond=0),
                    "check_out": datetime.now().replace(hour=17, minute=30, second=0, microsecond=0),
                    "status": "present"
                }
            ]
            
            for att_data in sample_attendance:
                attendance = Attendance(**att_data)
                db.add(attendance)
                logger.info(f"Created attendance record for employee {att_data['employee_id']}")
            
            # Create sample leave request
            sample_leave = Leave(
                employee_id=3,
                leave_type="annual",
                start_date=date(2024, 2, 1),
                end_date=date(2024, 2, 3),
                days_requested=3,
                reason="Family vacation",
                status="pending"
            )
            db.add(sample_leave)
            logger.info("Created sample leave request")
            
            # Create sample payroll record
            sample_payroll = Payroll(
                employee_id=1,
                month=1,
                year=2024,
                basic_salary=75000.00,
                allowances=5000.00,
                deductions=2000.00,
                net_salary=78000.00,
                status="paid"
            )
            db.add(sample_payroll)
            logger.info("Created sample payroll record")
            
            # Commit all changes
            db.commit()
            logger.info("Sample data created successfully")
            
            return True
            
        except Exception as e:
            db.rollback()
            logger.error(f"Error creating sample data: {e}")
            raise
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"PostgreSQL initialization failed: {e}")
        return False

def main():
    """Main initialization function"""
    logger.info("Starting PostgreSQL database initialization for HRMS on Railway...")
    
    # Initialize database
    if init_postgresql_database():
        logger.info("PostgreSQL database initialization completed successfully!")
        logger.info("Sample data created:")
        logger.info("- 3 users (admin, manager, employee)")
        logger.info("- 3 employee profiles")
        logger.info("- Sample attendance records")
        logger.info("- Sample leave request")
        logger.info("- Sample payroll record")
        
        logger.info("\n🔑 Login Credentials:")
        logger.info("Admin: admin@hrms.com / admin123")
        logger.info("Manager: manager@hrms.com / manager123")
        logger.info("Employee: employee@hrms.com / employee123")
        
        return True
    else:
        logger.error("PostgreSQL database initialization failed.")
        return False

if __name__ == "__main__":
    main()
