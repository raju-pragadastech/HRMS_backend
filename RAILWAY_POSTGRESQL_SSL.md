# Railway PostgreSQL SSL Setup Guide for HRMS

## 🚀 Quick Setup for Railway PostgreSQL with SSL

### 1. **Railway PostgreSQL Template**
You're using: `ghcr.io/railwayapp-templates/postgres-ssl:17`

This template provides:
- ✅ PostgreSQL 17 with SSL encryption
- ✅ Automatic SSL certificate management
- ✅ Connection pooling optimization
- ✅ Railway-native integration

### 2. **Environment Variables Setup**

In your Railway dashboard → Variables tab, set these:

```bash
# PostgreSQL Connection (Railway will provide this)
DATABASE_URL=postgresql://username:password@host:port/database?sslmode=require

# JWT Configuration
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# PostgreSQL SSL Configuration
POSTGRES_SSL_MODE=require
POSTGRES_SSL_CERT=/etc/ssl/certs/ca-certificates.crt
```

### 3. **Get PostgreSQL Connection String**

1. Go to your PostgreSQL service in Railway
2. Click "Connect" tab
3. Copy the "Postgres Connection URL"
4. **Important**: Add `?sslmode=require` if not present

**Format:**
```
postgresql://username:password@host:port/database?sslmode=require
```

## 🔧 **Deployment Steps**

### **Option 1: Railway CLI (Recommended)**

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Navigate to your backend folder
cd backend

# Link to Railway project
railway link

# Deploy
railway up
```

### **Option 2: GitHub Integration**

1. Push your code to GitHub
2. In Railway dashboard → "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will auto-detect and deploy

### **Option 3: Manual Deployment Script**

```bash
cd backend
python deploy_railway.py
```

## 🗄️ **Database Initialization**

After deployment, initialize your PostgreSQL database:

```bash
# SSH into Railway (if needed)
railway shell

# Initialize database with sample data
python init_postgresql_db.py
```

**Sample data created:**
- 3 users (admin, manager, employee)
- 3 employee profiles
- Sample attendance records
- Sample leave requests
- Sample payroll records

## 🔐 **SSL Configuration Details**

### **Automatic SSL Handling**
Your `database.py` automatically:
- Adds `sslmode=require` to connection string
- Configures SSL certificates
- Sets up secure connection pooling

### **Connection Parameters**
```python
connect_args = {
    "sslmode": "require",           # Require SSL
    "connect_timeout": 10,          # Connection timeout
    "application_name": "hrms_backend"  # App identifier
}
```

## 📱 **Test Your Deployment**

### **1. Health Check**
```bash
curl https://your-app.up.railway.app/api/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "database": "connected",
  "message": "HRMS Backend is running successfully on Railway"
}
```

### **2. Root Endpoint**
```bash
curl https://your-app.up.railway.app/
```

**Expected Response:**
```json
{
  "message": "Hello from HRMS Backend on Railway!",
  "status": "success",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### **3. Database Test**
```bash
curl https://your-app.up.railway.app/api/test
```

## 🚨 **Troubleshooting**

### **Common SSL Issues:**

1. **SSL Connection Failed**
   ```bash
   # Check DATABASE_URL format
   echo $DATABASE_URL
   
   # Ensure sslmode=require is present
   # postgresql://user:pass@host:port/db?sslmode=require
   ```

2. **Certificate Issues**
   ```bash
   # Railway handles certificates automatically
   # Check if POSTGRES_SSL_CERT is set
   echo $POSTGRES_SSL_CERT
   ```

3. **Connection Timeout**
   ```bash
   # Check Railway PostgreSQL service status
   # Verify DATABASE_URL is correct
   # Test connection manually
   ```

### **Database Connection Issues:**

```bash
# Test PostgreSQL connection
python migrate_to_postgresql.py

# Check logs in Railway dashboard
# Verify environment variables
```

### **Deployment Issues:**

```bash
# Check Railway status
railway status

# View deployment logs
railway logs

# Redeploy if needed
railway up
```

## 📊 **Performance Optimization**

### **Connection Pooling**
- **Pool Size**: 10 connections
- **Max Overflow**: 20 connections
- **Recycle Time**: 5 minutes
- **Pre-ping**: Enabled for connection verification

### **PostgreSQL Indexes**
- Email indexes (case-insensitive)
- Role-based indexes
- Date-based indexes
- Composite indexes for common queries

## 🔄 **Update Flutter App**

After successful deployment, update your Flutter app:

```dart
// In your API service
const String baseUrl = 'https://your-app-name.up.railway.app';

// Test endpoints
final response = await http.get(Uri.parse('$baseUrl/api/health'));
```

## 📋 **Complete Setup Checklist**

- [ ] Railway PostgreSQL service created
- [ ] Environment variables set in Railway
- [ ] Backend code pushed to GitHub
- [ ] Railway project linked
- [ ] Deployment successful
- [ ] Health endpoint responding
- [ ] Database initialized with sample data
- [ ] Flutter app updated with new API URL
- [ ] All endpoints tested

## 🎯 **Next Steps**

1. ✅ **PostgreSQL Setup**: Complete
2. ✅ **SSL Configuration**: Complete
3. ✅ **Deployment Scripts**: Complete
4. **Monitor Performance**: Check Railway metrics
5. **Scale if Needed**: Upgrade Railway plan
6. **Custom Domain**: Set up custom domain (optional)

---

**Your HRMS backend is now ready for production on Railway with PostgreSQL SSL! 🎉🗄️🔐**
