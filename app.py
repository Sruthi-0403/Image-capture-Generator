import streamlit as st
import cv2
from utils import save_image
from model import process_image

st.title("📸 Image Capture Generator")

# Start camera
run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Windows fix
    ret, frame = cap.read()

    if ret:
        FRAME_WINDOW.image(frame, channels="BGR")

        if st.button("Capture Image"):
            filename = save_image(frame)
            processed = process_image(frame)

            st.success(f"Saved: {filename}")
            st.image(processed, channels="BGR")

    cap.release()