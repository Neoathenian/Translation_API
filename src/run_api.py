import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

# Use the env var or fallback to current directory
os.environ["XDG_DATA_HOME"] = os.getcwd()
os.environ.setdefault("ARGOS_TRANSLATE_PACKAGE_PATH", os.path.join(os.getcwd(), "argos-translate"))

import argostranslate.translate

# ✅ NO need to call `load_installed_packages()` in older versions

app = FastAPI()

class TranslateRequest(BaseModel):
    text: str
    to_lang: str
    from_lang: Optional[str] = "en"


@app.post("/translate")
def translate_text(req: TranslateRequest):
    try:
        result = argostranslate.translate.translate(req.text, req.from_lang, req.to_lang)
        return {"translated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--is_local", action="store_true")
    args = parser.parse_args()

    host = "127.0.0.1" if args.is_local else "0.0.0.0"
    uvicorn.run(app, host=host, port=args.port)
