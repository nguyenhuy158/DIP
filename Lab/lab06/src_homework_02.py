# ============================== Import library ==============================
import cv2
import sys
import math
import cv2
import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector


# ============================== “Hand detection and finger counting” ==============================
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

while True:
    _, image = video.read()
    image = cv2.flip(image, 1)
    hand = detector.findHands(image, draw=False)
    finger = 0
    if hand:
        firstHand = hand[0]
        if firstHand:
            fingerUp = detector.fingersUp(firstHand)
            finger = sum(fingerUp)

    cv2.putText(image, str(finger),
                (200, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                5,
                (100, 200, 255),
                5,
                2)

    cv2.imshow("Video detect number finger", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# ============================== End ==============================
