@echo off
setlocal

:: Paths
set "EXTRACT_DIR=%~dp0PythonPortable"
set "PYTHON=%EXTRACT_DIR%\python.exe"
set "SCRIPT_NAME=src\download_language_models.py"

:: Set custom package path (for portability)
set "ARGOS_TRANSLATE_PACKAGE_PATH=%~dp0PythonPortable\data\argos-packages"

:: Make sure target directory exists
if not exist "%ARGOS_TRANSLATE_PACKAGE_PATH%" mkdir "%ARGOS_TRANSLATE_PACKAGE_PATH%"

:: Add python and Scripts to PATH
set "PATH=%EXTRACT_DIR%;%EXTRACT_DIR%\Scripts;%PATH%"

:: Run the installer script
"%PYTHON%" "%~dp0%SCRIPT_NAME%"

echo.
echo Argos Translate EN→RO model installed to portable path!
pause
endlocal
