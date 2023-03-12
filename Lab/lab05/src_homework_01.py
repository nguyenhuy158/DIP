import numpy as np
import cv2

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg = cv2.createBackgroundSubtractorMOG2()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    mask = fgbg.apply(frame)
    cv2.imshow("background subtract - noise", mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cv2.imshow("background subtract", mask)

    # esc to exit
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
