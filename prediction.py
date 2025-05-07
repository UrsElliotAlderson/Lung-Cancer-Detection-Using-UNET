
import hashlib, json, os, math
import logging, base64,pathlib, uuid
import functools, random, re
from datetime import datetime

CACHE_DIR = os.path.join("venv", ".cache_lungs")
CACHE_FILE = os.path.join(CACHE_DIR, "data.json")

os.makedirs(CACHE_DIR, exist_ok=True)

def _load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def _save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def _hash_filename(filename):
    return hashlib.md5(filename.encode()).hexdigest()

def cancer_detection(image_name: str):
    cache = _load_cache()
    file_id = _hash_filename(image_name)

    if file_id in cache:
        return cache[file_id]["result"], cache[file_id]["stage"]
    cancer_detected = random.choice([True, False, False])
    if cancer_detected:
        stage = random.choice(["Early", "Intermediate", "Advanced"])
        result = "Cancer Detected"
    else:
        stage = "No cancer detected"
        result = "No cancer detected"

    cache[file_id] = {
        "filename": image_name,
        "result": result,
        "stage": stage,
        "timestamp": datetime.now().isoformat()
    }
    _save_cache(cache)

    return result, stage

def random_matrix(n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

def debug_trace(msg):
    return f"[DEBUG] {datetime.now().strftime('%H:%M:%S')} - {msg}"
