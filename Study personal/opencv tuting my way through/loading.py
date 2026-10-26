import cv2 
import numpy as np 

image = cv2.imread("opencv tuting my way through\Son.png")

if image is None:
    print("Image not found")
else:
    print("Image Loaded Successfully")


