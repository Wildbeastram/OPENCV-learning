import cv2

image = cv2.imread("opencv tuting my way through\Son.png")

if image is not None:
    print("Image Loaded!!")
    cropped = image[100:900, 200:800] #(starty:endy,startx:endx) x is for top to bottom and y is for left to right (y1:y2,x1:x2) (height,width)
    cv2.imshow("Original SoNiOn Image", image)
    cv2.imshow("Cropped SoNiOn Image", cropped)
    cv2.imwrite("Cropped_Son.png",cropped) #always save the resized image with a new name to avoid overwriting the original image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found - Error")