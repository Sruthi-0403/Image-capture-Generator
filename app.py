import streamlit as st
import cv2
import numpy as np
from model import process_image
from utils import save_image

st.title("📸 Image Capture Generator (Cloud Version)")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    st.image(frame, channels="BGR", caption="Original Image")

    if st.button("Process Image"):
        filename = save_image(frame)
        processed = process_image(frame)

        st.success(f"Saved: {filename}")
        st.image(processed, channels="BGR", caption="Processed Image")
