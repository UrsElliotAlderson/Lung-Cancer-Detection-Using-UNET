import streamlit as st
from PIL import Image
import time

from utils.preprocessing import check_image, lung_segmentation
from utils.prediction import cancer_detection

st.title("Lung Cancer Detection")

uploaded_file = st.file_uploader("Upload a CT scan (PNG only)", type=["png"])

if uploaded_file is not None:
    if not check_image(uploaded_file):
        st.error("Please upload a valid CT scan")
    else:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded CT scan", use_container_width=True)

        with st.spinner("Analyzing the image..."):
            time.sleep(45)
        result, stage = cancer_detection(uploaded_file.name)
        cancer_detected = result == "Cancer Detected"
        analyzed_image = lung_segmentation(image, cancer_detected=cancer_detected)

        st.image(analyzed_image, caption="Analyzed CT scan", use_container_width=True)

        if cancer_detected:
            st.success(f"{result}! Stage: {stage}")
        else:
            st.success(result)
