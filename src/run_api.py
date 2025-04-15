import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn
import langid

import argostranslate.translate
# Configure langid to only recognize a specific set of languages
#langid.set_languages(['en', 'ro'])  # Add more as needed

# Set Argos Translate environment paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
os.environ["XDG_DATA_HOME"] = project_root
os.environ["ARGOS_TRANSLATE_PACKAGE_PATH"] = os.path.join(project_root, "argos-translate")


app = FastAPI()

class TranslateRequest(BaseModel):
    text: str
    to_lang: str
    from_lang: Optional[str] = None  # Allow None or "auto"


def detect_language(text: str) -> str:
    try:
        lang_code, _ = langid.classify(text)
        return lang_code
    except Exception:
        return "ro"  # Fallback


@app.post("/translate")
def translate_text(req: TranslateRequest):
    try:
        # Auto-detect if from_lang is missing or explicitly set to "auto"
        output={}
        source_lang = req.from_lang
        if not source_lang or source_lang.lower() == "auto":
            source_lang = detect_language(req.text)
            output["detected_source_lang"] = source_lang

        result = argostranslate.translate.translate(req.text, source_lang, req.to_lang)
        output["translated_text"] = result
        return output
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
