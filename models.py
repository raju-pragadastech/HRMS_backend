from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Numeric, Date, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    employee_id = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)  # "employee", "hr", "manager"
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship with Employee
    employee = relationship("Employee", back_populates="user", uselist=False, cascade="all, delete-orphan")
    
    # PostgreSQL specific indexes
    __table_args__ = (
        Index('idx_users_email_lower', func.lower(email)),
        Index('idx_users_role', role),
        Index('idx_users_created_at', created_at),
    )

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    department = Column(String(100))
    position = Column(String(100))
    hire_date = Column(Date)
    salary = Column(Numeric(10, 2))  # 10 digits total, 2 decimal places
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationship with User
    user = relationship("User", back_populates="employee")
    
    # PostgreSQL specific indexes
    __table_args__ = (
        Index('idx_employees_name', first_name, last_name),
        Index('idx_employees_department', department),
        Index('idx_employees_position', position),
        Index('idx_employees_hire_date', hire_date),
    )

# Additional HRMS tables for PostgreSQL
class Attendance(Base):
    __tablename__ = "attendance"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    check_in = Column(DateTime(timezone=True))
    check_out = Column(DateTime(timezone=True))
    status = Column(String(20), default="present")  # present, absent, late, half-day
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    employee = relationship("Employee")
    
    # PostgreSQL specific indexes
    __table_args__ = (
        Index('idx_attendance_employee_date', employee_id, date),
        Index('idx_attendance_date', date),
        Index('idx_attendance_status', status),
    )

class Leave(Base):
    __tablename__ = "leaves"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    leave_type = Column(String(50), nullable=False)  # sick, casual, annual, maternity
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    days_requested = Column(Integer, nullable=False)
    reason = Column(Text)
    status = Column(String(20), default="pending")  # pending, approved, rejected
    approved_by = Column(Integer, ForeignKey("users.id"))
    approved_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    employee = relationship("Employee")
    approver = relationship("User")
    
    # PostgreSQL specific indexes
    __table_args__ = (
        Index('idx_leaves_employee', employee_id),
        Index('idx_leaves_dates', start_date, end_date),
        Index('idx_leaves_status', status),
        Index('idx_leaves_type', leave_type),
    )

class Payroll(Base):
    __tablename__ = "payroll"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    month = Column(Integer, nullable=False)  # 1-12
    year = Column(Integer, nullable=False)
    basic_salary = Column(Numeric(10, 2), nullable=False)
    allowances = Column(Numeric(10, 2), default=0)
    deductions = Column(Numeric(10, 2), default=0)
    net_salary = Column(Numeric(10, 2), nullable=False)
    payment_date = Column(Date)
    status = Column(String(20), default="pending")  # pending, paid
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    employee = relationship("Employee")
    
    # PostgreSQL specific indexes
    __table_args__ = (
        Index('idx_payroll_employee_month_year', employee_id, month, year),
        Index('idx_payroll_month_year', month, year),
        Index('idx_payroll_status', status),
    )
