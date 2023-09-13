@echo off
where py >nul 2>nul
if %ERRORLEVEL% NEQ 0 echo Python not found. Please download and install: https://www.python.org/downloads & pause & exit

echo Starting...
pip install --upgrade pip
pip install -r requirements.txt
py main.py