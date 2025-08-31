# 🚀 Quick Railway Deployment Guide

## ✅ Your Railway PostgreSQL is Ready!

**Database URL:** `postgresql://postgres:erLUuZNgBeMWXVZhKdmuKWEdrvQjUaeP@turntable.proxy.rlwy.net:34996/railway`

## 🔧 Step 1: Test Database Connection

```bash
cd backend
python test_railway_db.py
```

This will verify your PostgreSQL connection is working.

## 🗄️ Step 2: Initialize Database

```bash
python init_postgresql_db.py
```

This creates all tables and sample data.

## 🚀 Step 3: Deploy to Railway

### Option A: Railway CLI (Recommended)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway link
railway up
```

### Option B: GitHub Integration

1. Push your code to GitHub
2. In Railway dashboard → "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository

## ⚙️ Step 4: Set Environment Variables

In Railway dashboard → Variables tab, add:

```bash
DATABASE_URL=postgresql://postgres:erLUuZNgBeMWXVZhKdmuKWEdrvQjUaeP@turntable.proxy.rlwy.net:34996/railway?sslmode=require
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
DB_SSL_MODE=require
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
```

## 🧪 Step 5: Test Your Deployment

After deployment, test these endpoints:

```bash
# Health check
curl https://your-app.up.railway.app/api/health

# Root endpoint
curl https://your-app.up.railway.app/

# API test
curl https://your-app.up.railway.app/api/test
```

## 🔑 Sample Login Credentials

After database initialization:

- **Admin:** admin@hrms.com / admin123
- **Manager:** manager@hrms.com / manager123  
- **Employee:** employee@hrms.com / employee123

## 📱 Update Flutter App

Update your Flutter app's API base URL to:
```dart
const String baseUrl = 'https://your-app-name.up.railway.app';
```

## 🚨 Troubleshooting

### Database Connection Issues
```bash
# Test connection
python test_railway_db.py

# Check logs
railway logs
```

### Common Problems
1. **SSL Error**: Ensure `?sslmode=require` is in DATABASE_URL
2. **Connection Failed**: Check Railway PostgreSQL service status
3. **Deployment Failed**: Verify environment variables

## 🎯 What You Get

- ✅ **PostgreSQL Database**: Connected and ready
- ✅ **SSL Security**: Encrypted connections
- ✅ **Sample Data**: 3 users with different roles
- ✅ **Complete HRMS**: Users, employees, attendance, leave, payroll
- ✅ **Production Ready**: Optimized for Railway

---

**Your HRMS backend is ready for Railway deployment! 🎉**
