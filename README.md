## Virtual Keyboard using Hand Gesture and MediaPipe
## Overview
This project allows users to control a virtual keyboard through hand gestures. The system uses MediaPipe for hand gesture recognition and PyAutoGUI to simulate typing on the computer. Users can type text by selecting virtual keys displayed on the screen using the index finger and thumb.

The virtual keyboard displays a 3x10 grid of letters and a "DEL" button to delete the last character. The hand detection system uses the thumb and index fingers to interact with the keyboard.

## Requirements
To run this project, you will need the following libraries:

opencv-python

cvzone

mediapipe

pyautogui

pynput

## You can install them using the following command:

bash
Copy code
pip install opencv-python cvzone mediapipe pyautogui pynput
Setup and Installation
Install the required libraries as mentioned above.

Connect your webcam to the computer.

Download or clone the repository to your local machine.

## How It Works
The project works as follows:

The system uses the webcam to capture hand gestures.

Hand landmarks are detected using MediaPipe to locate the thumb and index finger.

The virtual keyboard is displayed on the screen, and each key can be selected using the finger's position.

The DEL button can be used to delete the last typed character.

PyAutoGUI is used to simulate the pressing of keys on the keyboard.

## Functionality
Thumb and Index Finger Distance: The distance between the thumb and index finger determines the interaction. When the distance is small, it simulates a "click" on the keyboard.

Debounce Mechanism: A debounce mechanism ensures that keys are not clicked multiple times unintentionally.

Delete Button: A delete button (DEL) is included to remove the last typed character.

## 📸 Screenshots
![Screenshot 2025-04-27 at 2 14 18 PM](https://github.com/user-attachments/assets/ea9b4ab2-97f2-4770-a0ae-6ea331bcd800)

## 🎥 Project Explanation Video
🎥 [Watch the Video ](https://www.linkedin.com/posts/sathiyapriya-s-22ucs048_virtualkeyboard-ai-handgesture-activity-7237479582843457539-Rl40?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEKubiABTjioeFLfoGOrHXFNNCGvYJ6moX8)




