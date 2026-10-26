import cv2

image = cv2.imread("opencv tuting my way through\Son.png")

if image is not None:
    print("Image Loaded Successfully")
    (h, w) = image.shape[:2]#sliced to get the height and width of the image only
    center = (w // 2, h // 2) #center of the image
    M = cv2.getRotationMatrix2D(center, 90, 1.0) #rotation matrix, -90 for anti clockwise, (center,angle,scale 1.0 is same scale , 0.5 is half scale, 2.0 is double scale)
    rotated = cv2.warpAffine(image, M, (w, h)) #warpAffine is used to rotate the image(original one)
    cv2.imshow("Original Son Image", image)
    cv2.imshow("Rotated Son Image", rotated)
    cv2.imwrite("Rotated_Son.png",rotated) #always save the resized image with a new name to avoid overwriting the original image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found - Error")