#!/usr/bin/env python3
"""
Quick setup verification script for AI-NutriCare
Checks all dependencies and guides installation
"""

import sys
import subprocess
import os
from pathlib import Path

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def print_success(text):
    print(f"✅ {text}")

def print_error(text):
    print(f"❌ {text}")

def print_warning(text):
    print(f"⚠️  {text}")

def print_info(text):
    print(f"ℹ️  {text}")

def check_python_version():
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 10:
        print_success(f"Python {version.major}.{version.minor} is compatible")
        return True
    else:
        print_error(f"Python 3.10+ required (you have {version.major}.{version.minor})")
        return False

def check_package(package_name, import_name=None):
    """Check if a Python package is installed"""
    import_name = import_name or package_name
    try:
        __import__(import_name)
        return True
    except ImportError:
        return False

def check_python_packages():
    print_header("Checking Python Packages")
    
    packages = {
        "fastapi": "fastapi",
        "uvicorn": "uvicorn",
        "transformers": "transformers",
        "torch": "torch",
        "pdf2image": "pdf2image",
        "pdfplumber": "pdfplumber",
        "pytesseract": "pytesseract",
        "PIL": "PIL",
        "openai": "openai",
        "numpy": "numpy",
        "pandas": "pandas",
        "scikit-learn": "sklearn",
    }
    
    missing = []
    for pkg, import_name in packages.items():
        if check_package(pkg, import_name):
            print_success(f"{pkg}")
        else:
            print_error(f"{pkg} - NOT INSTALLED")
            missing.append(pkg)
    
    if missing:
        print_error(f"\nMissing packages: {', '.join(missing)}")
        print_info("Install with: pip install -r backend/requirements.txt")
        return False
    
    print_success("All Python packages installed!")
    return True

def check_tesseract():
    print_header("Checking Tesseract OCR")
    
    try:
        import pytesseract
        from PIL import Image
        print_info("pytesseract module found")
        
        # Try to call tesseract
        result = subprocess.run(
            ["tesseract", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print_success(f"Tesseract is installed: {version_line}")
            return True
        else:
            print_error("Tesseract not found in PATH")
            return False
            
    except FileNotFoundError:
        print_error("Tesseract executable not found")
        print_warning("Installation instructions:")
        print_info("1. Download from: https://github.com/UB-Mannheim/tesseract/wiki")
        print_info("2. Run the Windows installer (tesseract-ocr-w64-setup-v5.x.x.exe)")
        print_info("3. Default path: C:\\Program Files\\Tesseract-OCR")
        print_info("4. Restart your terminal/IDE after installation")
        return False
    except Exception as e:
        print_error(f"Error checking Tesseract: {e}")
        return False

def check_poppler():
    print_header("Checking Poppler")
    
    try:
        result = subprocess.run(
            ["pdftotext", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print_success("Poppler is installed")
            return True
        else:
            print_error("Poppler not found in PATH")
            return False
            
    except FileNotFoundError:
        print_error("Poppler executable not found")
        print_warning("Installation instructions:")
        print_info("1. Download from: https://github.com/oschwartz10612/poppler-windows/releases/")
        print_info("2. Extract to a folder (e.g., C:\\poppler)")
        print_info("3. Add bin folder to Windows PATH:")
        print_info("   - Right-click 'This PC' → Properties")
        print_info("   - Click 'Advanced system settings'")
        print_info("   - Click 'Environment Variables'")
        print_info("   - Add C:\\poppler\\bin to PATH")
        print_info("4. Restart your terminal/IDE")
        return False
    except Exception as e:
        print_error(f"Error checking Poppler: {e}")
        return False

def check_openai_key():
    print_header("Checking OpenAI API Key")
    
    # Check .env file
    env_path = Path("backend/.env")
    if env_path.exists():
        with open(env_path, 'r') as f:
            content = f.read()
            if "OPENAI_API_KEY=sk-" in content or "OPENAI_API_KEY=" in content:
                print_success(".env file found with OpenAI API key configured")
                return True
            else:
                print_warning(".env file exists but OPENAI_API_KEY not properly set")
                return False
    else:
        print_error(".env file not found in backend directory")
        print_warning("Create backend/.env with:")
        print_info("OPENAI_API_KEY=sk-your-actual-api-key-here")
        print_info("\nGet key from: https://platform.openai.com/api-keys")
        return False

def check_bert_model():
    print_header("Checking BERT Model")
    
    model_path = Path("backend/app/models/bert_disease_classifier")
    if model_path.exists() and (model_path / "config.json").exists():
        print_success(f"BERT model found at {model_path}")
        return True
    else:
        print_warning("BERT model not found")
        print_info("Run: cd training && python init_bert_model.py")
        return False

def main():
    print("\n" + "="*60)
    print("  AI-NutriCare Setup Verification")
    print("="*60)
    
    results = {}
    
    # Run all checks
    results["Python Version"] = check_python_version()
    results["Python Packages"] = check_python_packages()
    results["Tesseract OCR"] = check_tesseract()
    results["Poppler"] = check_poppler()
    results["OpenAI API Key"] = check_openai_key()
    results["BERT Model"] = check_bert_model()
    
    # Summary
    print_header("Setup Summary")
    
    all_ok = True
    for check, passed in results.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check}")
        if not passed:
            all_ok = False
    
    print()
    if all_ok:
        print_success("All checks passed! You're ready to go.")
        print_info("Start backend: cd backend && python -m uvicorn app.main:app --reload")
        print_info("Start frontend: cd frontend && streamlit run app.py")
    else:
        print_error("Some checks failed. Please fix the issues above.")
        print_info("Re-run this script after fixing issues.")
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
