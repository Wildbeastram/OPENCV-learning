import cv2
import numpy as np

image = cv2.imread("opencv tuting my way through\Son.png")

if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nColor Channels: {c}") #for grayscale no color channel output
else:
    print("Image not found")