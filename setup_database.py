from database import engine, SessionLocal
from models import Base
from crud import create_user
from schemas import UserCreate

def setup_database():
    """Create database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Error creating database tables: {e}")

def create_test_user():
    """Create a test user for login testing"""
    db = SessionLocal()
    try:
        # Check if test user already exists
        from crud import get_user_by_email
        existing_user = get_user_by_email(db, "test@example.com")
        if existing_user:
            print("Test user already exists!")
            print("You can login with:")
            print("Email/Employee ID: test@example.com or EMP001")
            print("Password: password123")
            return
        
        # Create a test user
        test_user = UserCreate(
            email="test@example.com",
            employee_id="EMP001",
            password="password123",
            role="employee"
        )
        
        user = create_user(db, test_user)
        print(f"Test user created: {user.email} (Employee ID: {user.employee_id})")
        print("You can login with:")
        print("Email/Employee ID: test@example.com or EMP001")
        print("Password: password123")
        
    except Exception as e:
        print(f"Error creating test user: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Setting up HRMS database...")
    setup_database()
    print("\nCreating test user...")
    create_test_user()
    print("\nSetup complete!")
