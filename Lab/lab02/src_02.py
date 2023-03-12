import cv2
import numpy as np

SIZE = 350

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, SIZE)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, SIZE)

while True:
    ret, frame = video.read()
    cv2.imshow("video capture original", frame)

    # 8.	Increase the brightness of the image
    alpha = 1.0
    beta = 100
    brightness = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    cv2.imshow("2.8 increase the brightness", brightness)

    # 9.	Enhance the image contrast by using global histogram equalization
    equalization = cv2.equalizeHist(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    cv2.imshow("2.9 histogram equalization", equalization)

    # 10.	Enhance the image contrast by using adaptive histogram equalization (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    cv2.imshow("2.10 adaptive histogram equalization", cl1)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
