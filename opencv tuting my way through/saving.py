import cv2
import numpy as np

image = cv2.imread("opencv tuting my way through\Son.png")

if image is not None:
    success = cv2.imwrite("Edited_son.png",image)
    if success:
        print("Image saved successfully as 'Edited_son.png'")
    else:
        print("Failed to save image- Error ")
else:
    print("Image not found - Error ")