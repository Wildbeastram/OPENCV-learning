import cv2
import numpy as np

image = cv2.imread("opencv tuting my way through\Son.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #BGR (RGB) is from color to gray 
    cv2.imshow("Grayscale SON Image", gray)#display
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("Grayscale_Son.png", gray) #SAVING
else:
    print("Image not found")