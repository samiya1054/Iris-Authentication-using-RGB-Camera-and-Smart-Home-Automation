#  Iris Authentication using RGB Camera & Smart Home Automation

##  Overview  
This project leverages **iris-based authentication** via an RGB camera to enable secure and smart home automation. Upon verifying a user’s identity through their iris, the system can autonomously control smart home devices (e.g., lights, appliances). It combines computer vision, biometrics, and home IoT control in one pipeline.

---

##  Table of Contents  
1. [Background & Motivation](#-background--motivation)  
2. [Features](#-features)  
3. [System Architecture & Workflow](#-system-architecture--workflow)  
4. [Tech Stack & Tools](#-tech-stack--tools)  
5. [Installation & Setup](#-installation--setup)  
6. [Usage Guide](#-usage-guide)  
 


---

## Background & Motivation  
- Biometric authentication adds a strong security layer compared to passwords or PINs.  
- Iris recognition is stable over time and difficult to spoof.  
- Integrating biometrics with smart homes ensures only authorized users can control devices.  
- This project demonstrates a real-world application combining computer vision, biometrics, and IoT control.

---

##  Features  
- **Enroll Users:** Capture iris images to register authorized users.  
- **Authenticate:** Recognize the user’s iris and confirm identity.  
- **Smart Home Control:** On successful authentication, trigger home automation routines (e.g., switching ON/OFF devices).  
- **Calibration & Eye Positioning:** Adjust camera alignment and eye positioning for better recognition.  
- **Gaze Tracking / Pupil Detection:** Additional modules to enhance precision.  

---

##  System Architecture & Workflow  

1. **Calibration Module**  
   - Align camera setup; account for distance, angle, lighting  
   - Helps in preparing input for iris capture  

2. **Enrollment (Enroll.py)**  
   - Capture and store iris images tied to user IDs  
   - Preprocess images (cropping, normalization)  

3. **Iris Recognition / Validation (Validate.py + eye / pupil / gaze modules)**  
   - Detect eye / pupil / gaze regions using computer vision  
   - Extract iris features  
   - Compare with enrolled iris templates  
   - Decide match / no match  

4. **Smart Home Automation Trigger**  
   - If authentication succeeds, send command to smart home systems  
   - Control devices (via APIs or GPIO, depending on your setup)  

5. **Supporting Modules**  
   - `calibration.py` — camera alignment  
   - `eye.py`, `pupil.py`, `gaze_tracking.py` — modules to localize relevant eye region  

---

##  Tech Stack & Tools  
- **Language:** Python  
- **Computer Vision / Image Processing:** OpenCV, NumPy  
- **Machine Learning / Biometrics:** (if you used any ML libraries, include them here)  
- **Smart Home / IoT Interface:** (e.g. Raspberry Pi GPIO, MQTT, REST calls)  
- **Additional Tools:**  
  - Modules for eye / gaze / pupil detection  
  - Configuration files, calibration routines  

---
##  Repository Structure  

```

/
├─ Enroll.py
├─ Validate.py
├─ calibration.py
├─ eye.py
├─ pupil.py
├─ gaze\_tracking.py
├─ **init**.py
├─ requirements.txt
├─ trained\_models/
└─ README.md

````

- `Enroll.py`: Register new users’ iris data  
- `Validate.py`: Authenticate users based on input iris  
- `calibration.py`: Utilities to calibrate camera / alignment  
- `eye.py`, `pupil.py`, `gaze_tracking.py`: Support modules for eye region detection  
- `trained_models/`: Stores any models or templates used  
- `requirements.txt`: Python dependencies  

---

##  Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/DINESHMD2033/Iris-Authentication-using-RGB-Camera-and-Smart-Home-Automation.git
   cd Iris-Authentication-using-RGB-Camera-and-Smart-Home-Automation

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Prepare hardware / IoT interface**

   * If using Raspberry Pi, ensure GPIO settings are configured
   * If controlling devices via APIs or MQTT, configure endpoints, credentials

5. **Run calibration (optional but recommended)**

   ```bash
   python calibration.py
   ```

6. **Enroll a user**

   ```bash
   python Enroll.py
   ```

7. **Run authentication / validation**

   ```bash
   python Validate.py
   ```

---

##  Usage Guide

* **Enroll Mode:**

  * Run `Enroll.py`, provide user identifier
  * Capture several iris images under good lighting
  * Store templates in `trained_models/`

* **Validation / Authentication Mode:**

  * Run `Validate.py`
  * Present iris in front of camera
  * System will process and return match / no match
  * On success, smart home commands are triggered

* **Calibration:**

  * Use `calibration.py` to adjust camera setup before enrollment/authentication
  * Helps reduce errors from misalignment

---
