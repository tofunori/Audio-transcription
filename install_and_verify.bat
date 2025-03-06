@echo off
echo AudioTrans Pro - Installation and Verification
echo ===========================================
echo.

REM Check if running with admin rights
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with administrative privileges...
) else (
    echo This script doesn't require administrative privileges.
)
echo.

REM Verify the installer if it exists
if exist "installer\AudioTrans_Setup.exe" (
    echo Verifying installer integrity...
    powershell -Command "Get-FileHash '.\installer\AudioTrans_Setup.exe' -Algorithm SHA256 | Format-List"
    echo.
    
    echo Starting installation...
    echo Please review any security prompts that appear.
    echo.
    start "" "installer\AudioTrans_Setup.exe"
) else (
    echo Error: Installer not found.
    echo Please ensure "AudioTrans_Setup.exe" is present in the installer directory.
    pause
    exit /b 1
)

echo.
echo After installation, please review:
echo - README.txt
echo - LICENSE.txt
echo - VERIFICATION.txt
echo - antivirus_instructions.txt

pause
