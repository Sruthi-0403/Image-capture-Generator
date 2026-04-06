import cv2
import os
from datetime import datetime

SAVE_DIR = "captured_images"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def capture_frame(cap):
    return cap.read()

def save_image(frame):
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
    filepath = os.path.join(SAVE_DIR, filename)
    cv2.imwrite(filepath, frame)
    return filepath