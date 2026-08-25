@echo off
cd /d %~dp0

echo =========================
echo Building KeyboardCleaner
echo =========================

call .venv\Scripts\activate

echo Installing/updating PyInstaller...
pip install pyinstaller

echo Building EXE...

pyinstaller --onefile --noconsole --clean --icon=assets\icon.ico main.py

echo.
echo =========================
echo Build finished!
echo Check the "dist" folder.
echo =========================

pause