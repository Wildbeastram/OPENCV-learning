import cv2
import numpy as np

image = cv2.imread("opencv tuting my way through\Son.png")

if image is not None:
    
    cv2.imshow("SoN??", image)#image title SON??
    cv2.waitKey(0)# wait for a key ,image open hui hai to user usko dekhte rahe ,0 means if keyboard pe koi button dabaye nai jati , jabtak open rakho image
    cv2.destroyAllWindows()#image close karne ke liye
else:

    print("Image not found")