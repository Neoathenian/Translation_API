# 🌐 Language Translation API

This is a simple and portable solution to create your own language translation API using pre-trained models.

## 🚀 Features
- No need to install Python globally — it's self-contained
- Easily configure language pairs
- Start your own translation API in minutes
- RESTful interface for integration with any app

---

## 📦 Setup Instructions

Follow these steps to get your translation API up and running:

### 1️⃣ Install Python Environment & Dependencies
Run:
```
installation.bat
```
This will create a `PythonPortable` folder containing a standalone Python environment with all required libraries.

### 2️⃣ Configure Language Pairs
Open `language_pairs.txt` and define the translation pairs you need.

> The **first language** is the source (e.g., English: `en`), and the **second** is the target (e.g., Romanian: `ro`).

### 3️⃣ Download Translation Models
Run:
```
2_download_language_models.bat
```
This downloads the models required for your specified language pairs.

### 4️⃣ Start the Translation API
Run:
```
3_run_api.bat
```
The API will be available at:
```
http://127.0.0.1:8090/translate
```

### 5️⃣ Test the API
You can test it using the provided script:
```
4_call_api.bat
```
Or, use Python:
```python
import requests

response = requests.post(
    "http://127.0.0.1:8090/translate",
    headers={"Content-Type": "application/json"},
    json={"text": "Hello world", "from_lang": "en", "to_lang": "ro"}
)

print(response.text)
```

---

## 🛠 Notes
- Ensure your firewall allows local connections on port `8090`
- The translation quality depends on the downloaded models
- You can add or remove language pairs anytime by updating `language_pairs.txt` and re-running step 3

---

## 📁 File Overview

| File | Purpose |
|------|---------|
| `installation.bat` | Sets up the portable Python environment |
| `language_pairs.txt` | List of source-target language codes |
| `2_download_language_models.bat` | Downloads the required translation models |
| `3_run_api.bat` | Starts the local API server |
| `4_call_api.bat` | Sample script to test the API |
