# Task - take image as user input and ask if user wants to save or show , if they want to show , then just show simply , if they want to save  then take output_name as input and save the image with that name
import cv2

image_path = input("Enter the Relative path of the image: ")
image = cv2.imread(image_path)

if image is not None:
    action = input("Do you want to 'show','save' or 'convert to grayscale' the image? (Enter 'show' or 'save'or 'convert'): ").strip().lower()
    if action == 'show':
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif action == 'convert':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif action == 'save':
        output_name=input("Enter the output filename (with extension, e.g., 'output.png'): ").strip()
        success= cv2.imwrite(output_name, image)
        if success:
            print(f"Image saved successfully as '{output_name}'")
        else:
            print("Failed to save image - Error")
    else:
        print("Invalid action. Please enter 'show', 'save', or 'convert'.")
else:
    print("Image not found - Error")