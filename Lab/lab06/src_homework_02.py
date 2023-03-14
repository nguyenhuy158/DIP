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
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    fing = "0"
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                fing = "1"
            if fingerup == [0, 1, 1, 0, 0]:
                fing = "2"
            if fingerup == [0, 1, 1, 1, 0]:
                fing = "3"
            if fingerup == [0, 1, 1, 1, 1]:
                fing = "4"
            if fingerup == [1, 1, 1, 1, 1]:
                fing = "5"

    cv2.putText(img, fing,
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                1,
                2)

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
# ============================== End ==============================
