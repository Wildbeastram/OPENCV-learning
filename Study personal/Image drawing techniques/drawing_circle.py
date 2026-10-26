import cv2

image = cv2.imread("Screenshot 2026-10-16 140515.png")

#cv2.circle(img, center(x, y), radius, color, thickness (-1 for filled circle))

if image is not None:
    print("Image Loaded Successfully!")
    center = (460, 200)
    radius = 90
    color=(255, 0, 0) #BGR format
    thickness = 5
    cv2.circle(image, center, radius, color, thickness)

    cv2.imshow("Circle drawn Ram Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found - Error")
