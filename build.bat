@echo off
pyinstaller --onefile --windowed --name "DmNotes" --add-data "assets;assets" --icon=ico.ico src/main.py