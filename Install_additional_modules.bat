@echo off
setlocal

::set http_proxy=http://proxy.groupama.ro:3128
::set https_proxy=http://proxy.groupama.ro:3128
::set ftp_proxy=http://proxy.groupama.ro:3128
::set no_proxy=localhost,127.0.0.1

:: Variables for setup
set PYTHON_VERSION=3.11.8
set EXTRACT_DIR=%~dp0PythonPortable
:: Ensure this is just the file name if in the same directory

SET PATH=%PATH%;%~dp0PythonPortable\Scripts


:: Install packages from requirements.txt
:: Adjust the pip call to use the python executable and the -m option to ensure compatibility
:: echo Installing dependencies from requirements.txt...
::"%EXTRACT_DIR%\python.exe" -m pip install rank_bm25
::"%EXTRACT_DIR%\python.exe" -m pip install traits

::Can not upgrade gradio cause it breaks everything
::"%EXTRACT_DIR%\python.exe" -m pip install gradio fastapi uvicorn
::"%EXTRACT_DIR%\python.exe" -m pip install -r requirements.txt
::"%EXTRACT_DIR%\python.exe" -m pip install --upgrade gradio fastapi uvicorn huggingface_hub
"%EXTRACT_DIR%\python.exe" -m pip freeze
::pip install --upgrade pip
::"%EXTRACT_DIR%\python.exe" -m pip install langid
::"%EXTRACT_DIR%\python.exe" -m pip install --upgrade weasel
::"%EXTRACT_DIR%\python.exe" --version
::-m pip install -U -q "google-genai"
::google-cloud-logging==3.11.3
::"%EXTRACT_DIR%\python.exe" -m pip install gradio==4.0.0 --no-deps
::"%EXTRACT_DIR%\python.exe" -m pip list

::"%EXTRACT_DIR%\python.exe" -m pip list


::"%EXTRACT_DIR%\python.exe" -m spacy download ro_core_news_sm

echo.
echo Script execution finished. Press any key to exit.
pause >nul

endlocal
