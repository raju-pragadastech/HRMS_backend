# HRMS Backend API

This directory contains the FastAPI backend API for the HRMS application with PostgreSQL database.

## Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: JWT tokens
- **ORM**: SQLAlchemy

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install PostgreSQL
Make sure PostgreSQL is installed and running on your system.

### 3. Configure Database
Update the database connection in `config.py` or create a `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost:5432/hrms_db
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
```

### 4. Setup Database
```bash
python setup_database.py
```

### 5. Run the Server
```bash
python start_server.py
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## API Endpoints (To be implemented)

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/first-time-signin` - First-time sign-in with role
- `POST /api/auth/logout` - User logout

### Employee Management
- `GET /api/employees` - Get all employees
- `GET /api/employees/:id` - Get employee by ID
- `PUT /api/employees/:id` - Update employee
- `POST /api/employees` - Create new employee

### Attendance
- `POST /api/attendance/clock-in` - Clock in
- `POST /api/attendance/clock-out` - Clock out
- `GET /api/attendance/:employeeId` - Get attendance history

### Leave Management
- `GET /api/leaves` - Get leave requests
- `POST /api/leaves` - Create leave request
- `PUT /api/leaves/:id/approve` - Approve leave
- `PUT /api/leaves/:id/reject` - Reject leave

### Performance
- `GET /api/performance/goals` - Get performance goals
- `POST /api/performance/goals` - Create performance goal
- `GET /api/performance/appraisals` - Get appraisals

### Payslips
- `GET /api/payslips` - Get payslips
- `GET /api/payslips/:id/download` - Download payslip

## Database Schema (To be designed)

### Tables
- users
- employees
- attendance
- leaves
- performance_goals
- appraisals
- payslips
- departments
- roles

## Setup Instructions

1. Choose your preferred backend technology
2. Set up the project structure
3. Install dependencies
4. Configure database connection
5. Implement API endpoints
6. Add authentication middleware
7. Test the API endpoints

## Environment Variables

Create a `.env` file with:
```
DATABASE_URL=your_database_connection_string
JWT_SECRET=your_jwt_secret
PORT=3000
NODE_ENV=development
```
