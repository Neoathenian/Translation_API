@echo off
setlocal

:: === CONFIGURATION ===
set TEXT=Hello world
set TO_LANG=ro
set FROM_LANG=en
set PORT=8090
set HOST=127.0.0.1

:: === CALL API ===
curl -X POST http://%HOST%:%PORT%/translate ^
  -H "Content-Type: application/json" ^
  -d "{\"text\": \"%TEXT%\", \"to_lang\": \"%TO_LANG%\", \"from_lang\": \"%FROM_LANG%\"}"

echo.
pause
