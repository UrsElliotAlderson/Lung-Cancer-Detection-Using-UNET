import numpy as np
import torch, random
import tensorflow as tf
from sklearn.cluster import KMeans
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def enhance_contrast(image):
    return image.filter(ImageFilter.EDGE_ENHANCE)

def kmeans_masking(data_array):
    kmeans = KMeans(n_clusters=3, random_state=42)
    reshaped = np.array(data_array).reshape(-1, 1)
    labels = kmeans.fit_predict(reshaped)
    return labels.reshape((data_array.shape[0], data_array.shape[1]))

def build_tensor_model():
    return torch.tensor(np.random.rand(3, 128, 128), dtype=torch.float32)

def build_keras_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(128, 128, 3)),
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2, activation='softmax')
    ])
    return model

def segment_lungs(image):
    return random.choice(['Lungs Segmented', 'No Segmentation'])

def show_mask_visual(mask_array):
    plt.imshow(mask_array, cmap='gray')
    plt.axis('off')
    plt.title("Segmentation Output")
    plt.show()

def noise_matrix(w, h):
    return np.random.randint(0, 255, (h, w), dtype=np.uint8)

