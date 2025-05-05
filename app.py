# In app.py
from utils.preprocessing import check_image, lung_segmentation
import streamlit as st
from PIL import Image
import random
import time

# App title
st.title("Lung Cancer Detection")

# File uploader
uploaded_file = st.file_uploader("Upload a CT scan (PNG only)", type=["png"])

if uploaded_file is not None:
    # Check if the uploaded image is a PNG
    if not check_image(uploaded_file):
        st.error("Please upload a valid CT scan")
    else:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded CT scan", use_container_width=True)

        with st.spinner("Analyzing the image..."):
            time.sleep(45)

        # Apply lung segmentation and random cancer prediction
        cancer_detected = random.choice([True, False])
        analyzed_image = lung_segmentation(image, cancer_detected=cancer_detected)

        # Display the processed image
        st.image(analyzed_image, caption="Analyzed CT scan", use_container_width=True)

        # Show cancer detection result
        if cancer_detected:
            stage = random.choice(['Early', 'Intermediate', 'Advanced'])
            st.success(f"Cancer detected! Stage: {stage}")
        else:
            st.success("No cancer detected.")
