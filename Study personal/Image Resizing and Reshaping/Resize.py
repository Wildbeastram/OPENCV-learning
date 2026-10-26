import cv2

image = cv2.imread("opencv tuting my way through\Son.png")

if image is not None:
    print("Image Loaded!!")
    resize= cv2.resize(image,(300,300)) #(width,height)

    cv2.imshow("Original SoNiOn Image",image)
    cv2.imshow("Resized SoNiOn Image",resize)
    cv2.imwrite("Resized_Son.png",resize) #always save the resized image with a new name to avoid overwriting the original image

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found - Error")