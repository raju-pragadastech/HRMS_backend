# HRMS Backend API

A FastAPI-based Human Resource Management System backend with PostgreSQL database support, designed for Railway deployment.

## 🚀 Features

- **User Management**: Authentication, authorization, and role-based access control
- **Employee Management**: Complete employee profiles and information
- **Attendance Tracking**: Check-in/out and status management
- **Leave Management**: Leave requests and approval workflow
- **Payroll System**: Salary calculations and payment tracking
- **PostgreSQL Database**: Production-ready with SSL encryption
- **Railway Deployment**: Optimized for Railway cloud platform

## 🏗️ Architecture

- **Framework**: FastAPI with Python 3.8+
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with secure password hashing
- **API Documentation**: Auto-generated with OpenAPI/Swagger
- **CORS**: Configured for cross-origin requests
- **SSL**: Secure database connections with Railway PostgreSQL

## 📁 Project Structure

```
backend/
├── main.py                 # FastAPI application entry point
├── config.py              # Configuration and environment variables
├── database.py            # Database connection and session management
├── models.py              # SQLAlchemy database models
├── schemas.py             # Pydantic data validation schemas
├── auth.py                # JWT authentication and password hashing
├── crud.py                # Database CRUD operations
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment configuration
├── railway.toml          # Railway-specific configuration
├── deploy_railway.py     # Automated deployment script
├── init_postgresql_db.py # Database initialization script
└── README.md             # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database (local or Railway)
- Railway account (for deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd backend
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   # Create .env file
   DATABASE_URL=postgresql://username:password@localhost:5432/hrms
   JWT_SECRET=your-secret-key
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

   The API will be available at `http://localhost:8000`

## 🚀 Railway Deployment

### Quick Deploy

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Deploy to Railway**
   ```bash
   cd backend
   railway login
   railway link
   railway up
   ```

### Environment Variables

Set these in Railway dashboard → Variables tab:

```bash
DATABASE_URL=postgresql://username:password@host:port/database?sslmode=require
JWT_SECRET=your-production-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Database Setup

After deployment, initialize your PostgreSQL database:

```bash
railway shell
python init_postgresql_db.py
```

## 📚 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### Users
- `GET /api/users/me` - Get current user profile

### Employees
- `GET /api/employees/me` - Get current employee profile
- `POST /api/employees` - Create employee profile

### Health & Testing
- `GET /` - Root endpoint with status
- `GET /api/health` - Health check with database status
- `GET /api/test` - API test endpoint

## 🗄️ Database Models

### Core Tables
- **users**: User accounts and authentication
- **employees**: Employee profiles and information
- **attendance**: Daily attendance records
- **leaves**: Leave requests and approvals
- **payroll**: Salary and payment information

### Key Features
- **Foreign Key Relationships**: Proper referential integrity
- **Indexes**: Performance-optimized database queries
- **Data Types**: PostgreSQL-specific optimizations
- **Cascade Deletes**: Automatic cleanup of related data

## 🔐 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: bcrypt password encryption
- **Role-Based Access**: User roles (employee, manager, hr)
- **SSL Encryption**: Secure database connections
- **CORS Protection**: Configurable cross-origin policies

## 📊 Performance Features

- **Connection Pooling**: Optimized database connections
- **Database Indexes**: Fast query performance
- **Lazy Loading**: Efficient relationship loading
- **Query Optimization**: Optimized SQL queries

## 🧪 Testing

### Health Check
```bash
curl https://your-app.up.railway.app/api/health
```

### API Test
```bash
curl https://your-app.up.railway.app/api/test
```

### Database Connection
```bash
curl https://your-app.up.railway.app/
```

## 🚨 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check `DATABASE_URL` format
   - Ensure SSL mode is set: `?sslmode=require`
   - Verify Railway PostgreSQL service status

2. **Deployment Issues**
   - Check Railway logs: `railway logs`
   - Verify environment variables
   - Check `requirements.txt` dependencies

3. **SSL Issues**
   - Ensure `sslmode=require` in connection string
   - Check Railway PostgreSQL SSL configuration

### Debug Commands

```bash
# Check Railway status
railway status

# View deployment logs
railway logs

# Test database connection
python init_postgresql_db.py

# Redeploy if needed
railway up
```

## 📱 Flutter Integration

After deployment, update your Flutter app:

```dart
// Update API base URL
const String baseUrl = 'https://your-app-name.up.railway.app';

// Test connection
final response = await http.get(Uri.parse('$baseUrl/api/health'));
```

## 🔄 Development Workflow

1. **Local Development**: Use SQLite for development
2. **Testing**: Test with local PostgreSQL
3. **Deployment**: Deploy to Railway with PostgreSQL
4. **Database**: Initialize with sample data
5. **Integration**: Update Flutter app with new API URL

## 📋 Dependencies

### Core Dependencies
- `fastapi` - Web framework
- `uvicorn[standard]` - ASGI server
- `sqlalchemy` - Database ORM
- `psycopg2-binary` - PostgreSQL adapter
- `python-jose[cryptography]` - JWT handling
- `passlib[bcrypt]` - Password hashing

### Development Dependencies
- `python-dotenv` - Environment variable management
- `alembic` - Database migrations (future use)

## 📄 License

This project is part of the HRMS system. See the main project license for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check the troubleshooting section
- Review Railway deployment logs
- Check environment variable configuration
- Verify database connection settings

---

**Happy Coding! 🎉**
