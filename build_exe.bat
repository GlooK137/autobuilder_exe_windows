python -m venv venv
venv\Scripts\pip install -r requirements.txt
venv\Scripts\pyinstaller -F main.py
rmdir /S/Q venv
copy dist\main.exe main.exe
rmdir /S/Q dist
rmdir /S/Q build
del /S/Q main.spec
