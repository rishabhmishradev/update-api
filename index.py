from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data.json"

@app.get("/")
def root():
    return {"status": "API working"}

@app.get("/check-update")
def check_update(app_version: int):
    data = json.loads(DATA_FILE.read_text())

    if app_version < data["latest_version"]:
        return JSONResponse({
            "update": True,
            "latest_version": data["latest_version"],
            "apk_url": data["apk_url"],
            "force_update": data["force_update"],
            "message": data["message"]
        })

    return JSONResponse({"update": False})
