@echo off
cd /d "%~dp0"

where py >nul 2>&1
if %errorlevel% == 0 ( py server.py & goto end )

where python3 >nul 2>&1
if %errorlevel% == 0 ( python3 server.py & goto end )

python server.py

:end
pause
