import cv2

image = cv2.imread("Screenshot 2026-10-16 140515.png")

if image is not None:
    print("Image Loaded Successfully")
    flipped_vertically = cv2.flip(image, 0) # 1 for horizontal flip, 0 for vertical flip
    flipped_horizontally = cv2.flip(image, 1) # 1 for horizontal flip, 0 for vertical flip
    flipped_both = cv2.flip(image, -1) # -1 for both horizontal and vertical flip
    cv2.imshow("Original SoNiOn Image", image)
    cv2.imshow("Flipped Horizontal SoNiOn Image", flipped_horizontally)
    cv2.imshow("Flipped Vertically SoNiOn Image", flipped_vertically)
    cv2.imshow("Flipped Both SoNiOn Image", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found - Error")