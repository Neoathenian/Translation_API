:: @echo off
setlocal

:: Variables for setup
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-embed-amd64.zip
set EXTRACT_DIR=%~dp0PythonPortable
set SCRIPT_NAME=src/run_api.py  

:: Set environment variables for portable Argos Translate data

set "ARGOS_TRANSLATE_PACKAGE_PATH=%~dp0%\argos-translate"

:: Run your Python script
::echo Running Python script...
"%EXTRACT_DIR%\python.exe" "%~dp0%SCRIPT_NAME%" --port 8090 --is_local
::--listen #When putting it on google cloud/docker
::--launch_web so that it launches it online




echo.
echo Script execution finished. Press any key to exit.
pause >nul

endlocal
