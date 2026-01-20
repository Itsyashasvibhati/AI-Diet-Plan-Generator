#!/usr/bin/env python3
"""
Quick Start Script - Get AI-NutriCare running in 5 minutes
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    print(f"\n{'='*70}")
    print(f"  {text.center(66)}")
    print(f"{'='*70}\n")

def print_step(step, text):
    print(f"\n📍 Step {step}: {text}")
    print("-" * 70)

def run_command(cmd, description):
    """Run a shell command"""
    print(f"   Running: {description}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ Success")
            return True
        else:
            print(f"   ❌ Failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print_header("🏥 AI-NutriCare - Quick Start")
    
    print("""
    This script will help you get the system running in 5 minutes.
    
    Prerequisites:
    ✅ Python 3.10+
    ✅ Tesseract OCR installed
    ✅ Poppler installed
    ✅ OpenAI API key ready
    
    Press Enter to continue, or Ctrl+C to exit...
    """)
    
    try:
        input()
    except KeyboardInterrupt:
        print("\n❌ Cancelled by user")
        return 1
    
    print_step(1, "Checking System Dependencies")
    
    if not os.name == 'nt':
        print("⚠️  This script is optimized for Windows.")
        print("   For Linux/Mac, see SETUP_INSTRUCTIONS.md")
    
    # Check Python
    print(f"\n   Python version: {sys.version}")
    if sys.version_info.major < 3 or sys.version_info.minor < 10:
        print("   ❌ Python 3.10+ required")
        return 1
    
    print_step(2, "Installing/Checking Python Packages")
    
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("   ❌ backend directory not found")
        print("      Are you in the project root?")
        return 1
    
    # Install requirements
    if run_command(
        f"pip install -r {backend_dir}/requirements.txt -q",
        "Installing Python packages"
    ):
        print("   ✅ All packages installed")
    else:
        print("   ⚠️  Some packages may not have installed correctly")
    
    print_step(3, "Configuring Environment")
    
    # Check/Create .env
    env_file = backend_dir / ".env"
    if env_file.exists():
        print("   ✅ .env file exists")
    else:
        print("   ℹ️  Creating .env template...")
        env_content = """# OpenAI API Configuration
OPENAI_API_KEY=sk-your-actual-api-key-here

# Environment
ENVIRONMENT=development

# Optional: Tesseract path (if not in system PATH)
# TESSERACT_PATH=C:\\Program Files\\Tesseract-OCR\\tesseract.exe
"""
        env_file.write_text(env_content)
        print("   ✅ Created backend/.env")
        print("   ⚠️  Please add your OpenAI API key to backend/.env")
        print("      Get key from: https://platform.openai.com/api-keys")
    
    print_step(4, "Testing System Setup")
    
    # Run setup check
    if os.path.exists("setup_check.py"):
        print("\n   Running setup verification...\n")
        result = subprocess.run(["python", "setup_check.py"], capture_output=False)
        if result.returncode != 0:
            print("\n   ⚠️  Some system components are missing")
            print("      See setup_check.py output above for details")
    
    print_step(5, "Starting Services")
    
    print("""
    ✅ System is ready! Now start the services:
    
    Terminal 1 - Backend Server:
    ────────────────────────────────
    cd backend
    $env:PYTHONPATH = "."
    python -m uvicorn app.main:app --reload
    
    Server: http://127.0.0.1:8000
    Docs:   http://127.0.0.1:8000/docs
    
    
    Terminal 2 - Frontend App:
    ────────────────────────────────
    cd frontend
    streamlit run app.py
    
    Frontend: http://localhost:8501
    
    
    📋 Next Steps:
    1. Upload a medical report PDF
    2. System will extract biomarkers
    3. Generate personalized diet plan
    4. Download or view recommendations
    
    📖 Documentation:
    - SETUP_INSTRUCTIONS.md - Detailed setup guide
    - IMPROVEMENTS.md - What was fixed
    - setup_check.py - Verify dependencies
    - test_improvements.py - Test improvements
    
    Need help?
    - Check SETUP_INSTRUCTIONS.md troubleshooting section
    - Review logs in terminal where backend is running
    - Ensure OpenAI API key is valid
    - Verify Tesseract & Poppler are installed
    
    """)
    
    print_header("🚀 Ready to Launch!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
