@echo off
SETLOCAL
echo Checking for Python...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Python is not installed or not in your PATH.
    echo Please install Python to run the 3D Physics Lab offline.
    echo.
    pause
    exit /b 1
)

echo Starting Local Physics Lab Server...
python server.py
pause
