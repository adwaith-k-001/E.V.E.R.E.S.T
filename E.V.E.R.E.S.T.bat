@echo off
title Starting E.V.E.R.E.S.T. AI Assistant
color 0A

REM === Navigate to project directory ===
cd /d "C:\stuff\Jarvis\E.V.E.R.E.S.T"

REM === Activate virtual environment ===
call venv\Scripts\activate.bat

REM === Start memory monitor in a new terminal window ===
start cmd /k "title 🧠 Memory Monitor & call venv\Scripts\activate.bat & python Modules\memory_monitor.py"

REM === Run the assistant ===
python main.py

REM === Pause to keep terminal open after assistant exits ===
echo.
pause
