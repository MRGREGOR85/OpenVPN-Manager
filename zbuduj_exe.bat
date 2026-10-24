@echo off
:: Buduje GhostNet.exe z ghostnet.py (PyInstaller): jeden plik, okno konsoli, prosi o administratora (UAC).
:: Gotowy GhostNet.exe trafia obok tego pliku - tam, gdzie Login.txt, loginy i bledy.
:: Autor: MRGREGOR85
cd /d "%~dp0"
python -m pip install --upgrade pyinstaller || (echo [!] Nie udalo sie zainstalowac PyInstaller & pause & exit /b 1)
python -m PyInstaller --onefile --console --uac-admin --clean --name GhostNet ghostnet.py || (echo [!] Budowanie nie powiodlo sie & pause & exit /b 1)
copy /y "dist\GhostNet.exe" "%~dp0GhostNet.exe" >nul
echo(
echo [+] Gotowe: %~dp0GhostNet.exe
pause
