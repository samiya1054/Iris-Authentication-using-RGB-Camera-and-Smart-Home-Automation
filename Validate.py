import cv2
import os
import subprocess  # To run gaze tracking after validation
from skimage.metrics import structural_similarity as ssim
import numpy as np

def validate_user(name):
    # Initialize the camera
    cam = cv2.VideoCapture(0)  # Adjust index if needed
    if not cam.isOpened():
        print("Error: Could not open the camera.")
        return

    # Path to user's enrolled iris images
    user_folder = f'iris_data/{name}'
    if not os.path.exists(user_folder):
        print(f"No enrollment data found for {name}")
        cam.release()
        return

    # Load Haar cascades for face and eye detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    print("Validating...")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: Failed to grab frame from camera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (ex, ey, ew, eh) in eyes:
                eye_img = roi_gray[ey:ey + eh, ex:ex + ew]
                eye_resized = cv2.resize(eye_img, (100, 100))
                hist_eq_eye = cv2.equalizeHist(eye_resized)

                # Start validation by comparing with each enrolled image
                for img_file in os.listdir(user_folder):
                    enrolled_img_path = os.path.join(user_folder, img_file)
                    enrolled_img = cv2.imread(enrolled_img_path, cv2.IMREAD_GRAYSCALE)

                    if enrolled_img is None:
                        continue

                    # Compare using SSIM
                    score, _ = ssim(hist_eq_eye, enrolled_img, full=True)
                    if score > 0.60:  # Threshold for similarity
                        print(f"Validation successful! Match found with score: {score:.2f}")
                        cam.release()
                        cv2.destroyAllWindows()

                        # Run gaze tracking code after successful validation
                        subprocess.run(["python", "-m", "gaze_tracking.example"], cwd="d:/Biometrics/GazeTracking-master")
  # Replace example.py with gaze tracking script filename
                        return

        # Display the camera feed
        cv2.imshow("Iris Validation", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Example usage: validate a person
name = input("Enter name for validation: ")
validate_user(name)
