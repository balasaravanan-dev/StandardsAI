"""
StandardsAI - One-Click Demo Launcher
Starts both backend and frontend for video presentation
"""

import subprocess
import sys
import time
import os
import webbrowser
from pathlib import Path

# Paths
ROOT = Path(__file__).parent
BACKEND_DIR = ROOT / "backend"
FRONTEND_DIR = ROOT / "frontend"

def check_dependencies():
    """Check if required packages are installed."""
    required = ["fastapi", "uvicorn", "streamlit", "requests"]
    missing = []

    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"Missing packages: {', '.join(missing)}")
        print("Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install"] + missing, check=True)
        print("Done!")

    return True

def start_backend():
    """Start the FastAPI backend."""
    print("Starting backend server...")
    os.chdir(BACKEND_DIR)

    # Start uvicorn in a subprocess
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    # Wait for startup
    time.sleep(3)

    if process.poll() is None:
        print("Backend started on http://localhost:8000")
        return process
    else:
        print("Failed to start backend!")
        return None

def start_frontend():
    """Start the Streamlit frontend."""
    print("Starting frontend...")
    os.chdir(FRONTEND_DIR)

    # Start streamlit in a subprocess
    process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    # Wait for startup
    time.sleep(3)

    if process.poll() is None:
        print("Frontend started on http://localhost:8501")
        return process
    else:
        print("Failed to start frontend!")
        return None

def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║           STANDARDSAI - DEMO LAUNCHER                     ║
    ║   AI-Powered Indian Standards Recommendation Engine       ║
    ║                                                           ║
    ║   SIH 2024 | Problem ID: 26108                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    # Check dependencies
    print("[1/4] Checking dependencies...")
    check_dependencies()

    # Start backend
    print("\n[2/4] Starting backend...")
    backend = start_backend()

    if not backend:
        print("ERROR: Could not start backend. Exiting.")
        return

    # Start frontend
    print("\n[3/4] Starting frontend...")
    os.chdir(ROOT)
    frontend = start_frontend()

    if not frontend:
        print("ERROR: Could not start frontend.")
        backend.terminate()
        return

    # Open browser
    print("\n[4/4] Opening browser...")
    time.sleep(2)
    webbrowser.open("http://localhost:8501")

    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                    DEMO RUNNING                           ║
    ╠═══════════════════════════════════════════════════════════╣
    ║   Frontend: http://localhost:8501                         ║
    ║   Backend:  http://localhost:8000                         ║
    ║   API Docs: http://localhost:8000/docs                    ║
    ╠═══════════════════════════════════════════════════════════╣
    ║   Press Ctrl+C to stop                                    ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    try:
        # Keep running
        while True:
            time.sleep(1)
            # Check if processes are still running
            if backend.poll() is not None:
                print("Backend stopped unexpectedly!")
                break
            if frontend.poll() is not None:
                print("Frontend stopped unexpectedly!")
                break
    except KeyboardInterrupt:
        print("\n\nShutting down...")
    finally:
        backend.terminate()
        frontend.terminate()
        print("Demo stopped.")

if __name__ == "__main__":
    main()
