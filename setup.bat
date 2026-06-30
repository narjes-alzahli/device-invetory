@echo off
cd /d "%~dp0"

echo.
echo  Setting up mhmd-world...
echo.

REM Try py launcher first (works even without Python in PATH)
where py >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON=py
    goto found
)

REM Fallback to python3
where python3 >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON=python3
    goto found
)

REM Fallback to python
where python >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON=python
    goto found
)

echo  Python not found.
echo.
echo  Please install Python from https://python.org
echo  During install, tick the box that says "Add Python to PATH"
echo.
pause
exit /b 1

:found
echo  Python found:
%PYTHON% --version
echo.

echo  Installing dependencies...
%PYTHON% -m pip install -r requirements.txt -q

echo.
echo  Setup complete! Starting server...
echo  Open http://localhost:7788 in your browser.
echo.

%PYTHON% server.py
pause
