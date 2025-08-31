#!/usr/bin/env python3

import sys
import traceback

def test_imports():
    try:
        print("Testing imports...")
        from main import app
        print("✓ Main app import successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        traceback.print_exc()
        return False

def test_server_start():
    try:
        print("Testing server startup...")
        import uvicorn
        from main import app
        
        # Try to start server for a few seconds
        import threading
        import time
        
        def start_server():
            uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
        
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        
        # Wait a bit for server to start
        time.sleep(3)
        
        # Test connection
        import requests
        response = requests.get("http://localhost:8000/", timeout=5)
        print(f"✓ Server responding: {response.status_code}")
        print(f"✓ Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"✗ Server test failed: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=== Server Test ===")
    
    if not test_imports():
        sys.exit(1)
    
    if not test_server_start():
        sys.exit(1)
    
    print("✓ All tests passed!")
