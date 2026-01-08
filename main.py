from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

DATA_FILE = Path(__file__).resolve().parent.parent / "data.json"

@app.get("/check-update")
def check_update(app_version: int):
    data = json.loads(DATA_FILE.read_text())
    if app_version < data["latest_version"]:
        return {
            "update": True,
            "latest_version": data["latest_version"],
            "apk_url": data["apk_url"],
            "force_update": data["force_update"],
            "message": data["message"]
        }
    return {"update": False}

