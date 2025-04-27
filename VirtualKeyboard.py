import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cvzone
import pyautogui  # Import pyautogui for better control
from pynput.keyboard import Controller

# Setup camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Hand detector
detector = HandDetector(detectionCon=0.8)

# Virtual keyboard keys
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
finalText = ""

# Button class
class Button:
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

# Define positions and size for the Delete button
delete_button = Button([1150, 50], "DEL", size=[100, 50])

# Function to draw all buttons
def drawAll(img, buttonList, delete_btn):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    
    # Draw the Delete button
    x, y = delete_btn.pos
    w, h = delete_btn.size
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), cv2.FILLED)
    cv2.putText(img, delete_btn.text, (x + 20, y + 35),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    
    return img

# Create button list
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# Variables to manage button state
last_clicked_time = 0
debounce_time = 0.15

# Main loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Detect hands and return the image with annotations

    if hands:
        lmList = hands[0]['lmList']  # Get landmark list of the first hand detected

        if lmList:
            x_index, y_index = lmList[8][0], lmList[8][1]
            cv2.circle(img, (x_index, y_index), 10, (0, 255, 0), cv2.FILLED)

            l_thumb_index, _, _ = detector.findDistance(lmList[4][:2], lmList[8][:2])  # Thumb and index fingers

            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                if x < x_index < x + w and y < y_index < y + h:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                    # Execute click if thumb and index fingers are close
                    if l_thumb_index < 30:
                        current_time = cv2.getTickCount() / cv2.getTickFrequency()
                        if current_time - last_clicked_time > debounce_time:
                            if button.text == "DEL":
                                finalText = finalText[:-1]  # Remove last character
                                pyautogui.press('backspace')  # Simulate backspace key
                            else:
                                pyautogui.write(button.text)  # Simulate typing the text
                                finalText += button.text
                            last_clicked_time = current_time

            del_x, del_y = delete_button.pos
            del_w, del_h = delete_button.size
            if del_x < x_index < del_x + del_w and del_y < y_index < del_y + del_h:
                cv2.rectangle(img, (del_x - 5, del_y - 5), (del_x + del_w + 5, del_y + del_h + 5), (0, 0, 175), cv2.FILLED)
                cv2.putText(img, delete_button.text, (del_x + 20, del_y + 35),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                
                if l_thumb_index < 30:
                    current_time = cv2.getTickCount() / cv2.getTickFrequency()
                    if current_time - last_clicked_time > debounce_time:
                        finalText = finalText[:-1]  # Remove last character
                        pyautogui.press('backspace')  # Simulate backspace key
                        last_clicked_time = current_time

    img = drawAll(img, buttonList, delete_button)

    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()

