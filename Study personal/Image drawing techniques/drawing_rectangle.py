import cv2

image = cv2.imread("Screenshot 2026-10-16 140515.png")

#cv2.rectangle(img, point1(top left corner of rectangle), point2(bottom right corner of rectangle), color of line, thickness of line)

if image is not None:
    print("Image Loaded Successfully!")
    pt1 = (370, 100)
    pt2 = (530, 300)
    color=(255, 0, 0) #BGR format
    thickness = 5
    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Rectangle drawn Ram Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found - Error")
