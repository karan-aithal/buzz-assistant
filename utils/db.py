import json
import os

DB_FILE = "settings.json"

def save_settings(key, value):
    if not os.path.exists(DB_FILE):
        data = {}
    else:
        with open(DB_FILE, "r") as file:
            data = json.load(file)

    data[key] = value

    with open(DB_FILE, "w") as file:
        json.dump(data, file)

def load_settings(key, default=None):
    if not os.path.exists(DB_FILE):
        return default

    with open(DB_FILE, "r") as file:
        data = json.load(file)

    return data.get(key, default)
