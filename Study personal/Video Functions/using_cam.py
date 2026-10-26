import cv2 

cap = cv2.VideoCapture(0) # 0 for default camera, 1 for external camera |(Turns on camera)

while True:
    ret, frame= cap.read()#ret = True if frame is read correctly or False otherwise, frame = the captured frame |(Reading a frame from camera)
    if not ret:
        print("Failed to read frame")
        break
    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Wait 1sec | Press 'q' to exit (0xFF == ord('q') both gives ascii code and this 0xFF handles the ascii code for different platforms)
        print("Quitting...")
        break

cap.release() #turns off camera
cv2.destroyAllWindows()