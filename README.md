🏥 Medical Gesture Detection System
A real-time computer vision–based medical gesture recognition system that enables patients to communicate critical needs using hand gestures. This project is especially useful for elderly, speech-impaired, or bedridden patients in hospitals and home care environments.

📌 Problem Statement
Many patients are unable to verbally communicate their needs due to physical limitations. This leads to delayed responses in emergency and care situations.

💡 Solution
This project uses MediaPipe Hand Tracking and OpenCV to recognize predefined hand gestures and convert them into meaningful medical alerts such as:
Help
Pain
Water
Food
Emergency
The system works in real time using a webcam and displays the detected medical need on the screen.

🚀 Features
Real-time hand gesture detection
Full-screen display (15.6-inch screen optimized)
Lightweight and fast
Works with standard webcam
No internet required
Easy to extend with new gestures

🧠 Recognized Gestures
Gesture
Medical Meaning
✋ Open Palm
Help
✊ Closed Fist
Pain
☝ Index Finger Up
Water
✌ Two Fingers
Food
👍 Thumb Up
Emergency
🛠️ Tech Stack
Python
OpenCV
MediaPipe
NumPy
VS Code
📂 Project Structure
Copy code

medical-gesture-detection/
│
├── main.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
Copy code
Bash
2️⃣ Install Dependencies
Copy code
Bash
pip install -r requirements.txt
3️⃣ Run the Project
Copy code
Bash
python main.py

🎥 Demo
The webcam opens in full-screen mode
Show hand gestures in front of the camera
Medical message appears instantly on screen
📌 Press ESC to exit

📈 Use Cases
Hospitals & ICUs
Elderly care centers
Home healthcare monitoring
Emergency response systems
Assistive technology for disabled patients

⚠️ Limitations
Works best in good lighting
Detects one hand at a time
Limited to predefined gestures
Camera angle affects accuracy
