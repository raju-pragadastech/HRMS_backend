from sqlalchemy.orm import Session
from models import User, Employee
from schemas import UserCreate, EmployeeCreate
from auth import get_password_hash, verify_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_employee_id(db: Session, employee_id: str):
    return db.query(User).filter(User.employee_id == employee_id).first()

def get_user_by_email_or_employee_id(db: Session, email_or_employee_id: str):
    # Try to find by email first
    user = get_user_by_email(db, email_or_employee_id)
    if user:
        return user
    # If not found by email, try employee_id
    return get_user_by_employee_id(db, email_or_employee_id)

def authenticate_user(db: Session, email_or_employee_id: str, password: str):
    user = get_user_by_email_or_employee_id(db, email_or_employee_id)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        employee_id=user.employee_id,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_employee(db: Session, employee: EmployeeCreate, user_id: int):
    db_employee = Employee(
        **employee.dict(),
        user_id=user_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee_by_user_id(db: Session, user_id: int):
    return db.query(Employee).filter(Employee.user_id == user_id).first()
