import cv2
import os

# Create the main directory for storing enrolled data if it doesn't exist
if not os.path.exists('iris_data'):
    os.makedirs('iris_data')

def capture_and_store(name):
    # Initialize the camera
    cam = cv2.VideoCapture(0)  # Try changing index if 1 doesn't work for your camera
    if not cam.isOpened():
        print("Error: Could not open the camera.")
        return

    # Create a directory for each user inside 'iris_data'
    user_folder = f'iris_data/{name}'
    os.makedirs(user_folder, exist_ok=True)

    # Load Haar cascades for face and eye detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    capture_count = 0
    max_captures = 100  # Reduce the number of captures for quality over quantity

    while capture_count < max_captures:
        ret, frame = cam.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

            for (ex, ey, ew, eh) in eyes:
                eye_img = roi_gray[ey:ey + eh, ex:ex + ew]
                eye_resized = cv2.resize(eye_img, (100, 100))
                hist_eq_eye = cv2.equalizeHist(eye_resized)

                # Save each clear image
                iris_path = os.path.join(user_folder, f"{name}_eye_{capture_count + 1}.jpg")
                cv2.imwrite(iris_path, hist_eq_eye)
                print(f"Saved iris image {capture_count + 1} for {name}")
                capture_count += 1
                if capture_count >= max_captures:
                    break

        cv2.imshow("Iris Enrollment", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Enrollment cancelled.")
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"Enrollment completed for {name}. Images saved in folder: {user_folder}")

# Example usage: enroll a person
name = input("Enter name for enrollment: ")
capture_and_store(name)