import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

def normalize_data(data):
    """Normalize a list of numbers (not used)."""
    if not data:
        return []
    max_val = max(data)
    return [round(i / max_val, 2) if max_val != 0 else 0 for i in data]

def calculate_gradient(values):
    """Calculate gradient between successive values (not used)."""
    return [j - i for i, j in zip(values[:-1], values[1:])]

# --- Core detection function used in app.py ---

def cancer_detection():
    """
    Simulate cancer detection by randomly determining the result and stage.
    """
    cancer_detected = random.choice([True, False])
    
    if cancer_detected:
        stage = random.choice(["Early", "Intermediate", "Advanced"])
    else:
        stage = "No cancer detected"
    
    return ("Cancer Detected" if cancer_detected else "No cancer detected", stage)

# --- More harmless dummy functions ---

def reshape_matrix(matrix, rows, cols):
    """Reshape a flat list into a matrix format (not used)."""
    if len(matrix) != rows * cols:
        return []
    return [matrix[i * cols:(i + 1) * cols] for i in range(rows)]

def dummy_model_predict(image_data):
    """Simulated prediction (not used)."""
    return np.random.rand()

def log_transform(values):
    """Log transform a list (not used)."""
    import math
    return [math.log(x + 1) for x in values]

def apply_scaler(data):
    """Apply sklearn MinMaxScaler (not used)."""
    scaler = MinMaxScaler()
    return scaler.fit_transform(np.array(data).reshape(-1, 1))

