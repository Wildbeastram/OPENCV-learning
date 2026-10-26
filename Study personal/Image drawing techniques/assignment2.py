import cv2
from tkinter import Tk, filedialog

# Create a hidden Tk window because we only need the file dialogs.
root = Tk()
root.withdraw()  # Hide the empty Tkinter window

# Ask the user to choose an image; the dialog returns its full file path.
image_path = filedialog.askopenfilename(
    title="Select an image file",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")]
)

if not image_path:
    print("No image selected.")
    root.destroy()
    raise SystemExit

# Read the selected image from disk. OpenCV drawing functions need image data,
# not the file path string returned by the file dialog.
image = cv2.imread(image_path)
root.destroy()

if image is None:
    print("Could not load the selected image.")
else:
    print("Image Loaded Successfully!")
    print("What do you want to draw on the image?")
    print("1. Line")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Text")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        x1 = int(input("Enter x1 coordinate: "))
        y1 = int(input("Enter y1 coordinate: "))
        x2 = int(input("Enter x2 coordinate: "))
        y2 = int(input("Enter y2 coordinate: "))
        color = (255, 0, 0)  # BGR format
        thickness = 5
        cv2.line(image, (x1, y1), (x2, y2), color, thickness)
        
    elif choice == '2':
        center_x = int(input("Enter center x coordinate: "))
        center_y = int(input("Enter center y coordinate: "))
        radius = int(input("Enter radius: "))
        color = (255, 0, 0)  # BGR format
        thickness = 5
        cv2.circle(image, (center_x, center_y), radius, color, thickness)
        
    elif choice == '3':
        x1 = int(input("Enter top left x coordinate: "))
        y1 = int(input("Enter top left y coordinate: "))
        x2 = int(input("Enter bottom right x coordinate: "))
        y2 = int(input("Enter bottom right y coordinate: "))
        color = (255, 0, 0)  # BGR format
        thickness = 5
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        
    elif choice == '4':
        text = input("Enter the text to draw: ")
        x = int(input("Enter x coordinate for text: "))
        y = int(input("Enter y coordinate for text: "))
        font_scale = float(input("Enter font scale (e.g., 1.0): "))
        color = (255, 0, 0)  # BGR format
        thickness = 2
        cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
        
    else:
        print("Invalid choice!")
    
    save_image = input("Do you want to save the image? (yes/no): ").strip().lower()
    if save_image == "yes":
        # Let the user choose the output filename and folder.
        save_path = filedialog.asksaveasfilename(
            title="Save edited image",
            defaultextension=".png",
            filetypes=[("PNG image", "*.png"), ("JPEG image", "*.jpg *.jpeg"), ("All files", "*.*")]
        )
        if not save_path:
            print("Save cancelled; image was not saved.")
        elif cv2.imwrite(save_path, image):
            print(f"Image saved at {save_path}")
        else:
            print("Could not save the image.")
    
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()