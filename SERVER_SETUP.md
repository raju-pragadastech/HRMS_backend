# HRMS Backend Server Setup

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Server

**Option A: Using Python directly**
```bash
python main.py
```

**Option B: Using the batch file (Windows)**
```bash
start_server.bat
```

**Option C: Using uvicorn directly**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Verify Server is Running

The server should start and show:
```
INFO:     Started server process [XXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 4. Test the Server

Open your browser or use curl to test:
- Main endpoint: http://localhost:8000/
- Test endpoint: http://localhost:8000/api/test
- API docs: http://localhost:8000/docs

## Troubleshooting

### Server Won't Start
1. Check if port 8000 is already in use:
   ```bash
   netstat -an | findstr :8000
   ```

2. Kill any process using port 8000:
   ```bash
   taskkill /F /PID <process_id>
   ```

### Connection Issues
1. Make sure the server is running on `0.0.0.0:8000`
2. Check firewall settings
3. For Flutter app, ensure you're using the correct URL:
   - Android Emulator: `http://10.0.2.2:8000`
   - iOS Simulator: `http://localhost:8000`
   - Physical Device: `http://<your-computer-ip>:8000`

### Database Issues
If you get database errors, run:
```bash
python setup_database.py
```

## API Endpoints

- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `GET /api/users/me` - Get current user profile
- `GET /api/employees/me` - Get employee profile
- `POST /api/employees` - Create employee profile

## Development

For development with auto-reload:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
