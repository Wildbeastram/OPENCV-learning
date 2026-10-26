import cv2

image = cv2.imread("Screenshot 2026-10-16 140515.png")
#Context = imagine person standing and long hair detected , now we will display LONG HAIR FOUND type text
#cv2.putText(img, text, org(bottom left corner of text), fontFace, fontScale(1.0 normal ,2.0 double size), color, thickness(1 normal, 2 double size), lineType(0 normal, 2 double size), color, thickness)

if image is not None:
    print("Image Loaded Successfully!")
    cv2.putText(image, "Namaste!", (390, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)

    cv2.imshow("Text drawn Ram Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found - Error")
