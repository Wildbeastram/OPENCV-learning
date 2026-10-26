import cv2

image = cv2.imread("Screenshot 2026-10-16 140515.png")

#cv2.line(img, point1(x(left to right),y(top to bottom)), point2(x,y), color of line, thickness of line)

if image is not None:
    print("Image Loaded Successfully!")
    pt1 = (350, 100)
    pt2 = (530, 100)
    color=(255, 0, 0) #BGR format
    thickness = 5
    cv2.line(image, pt1, pt2, color, thickness)

    cv2.imshow("Line drawn Ram Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found - Error")
