from fastapi import HTTPException
import json


def load_data():
    try:
        with open("./data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Data file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid data format")
