import cv2
import numpy as np

WIDTH = 1
HEIGHT = 0
startPoint = 10
scale = 30 / 100

pathLogo = "lab3_img2.png"
imgLogo = cv2.imread(pathLogo)

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, imgLogo.shape[WIDTH])
video.set(cv2.CAP_PROP_FRAME_HEIGHT, imgLogo.shape[HEIGHT])
newSize = (int(imgLogo.shape[WIDTH] * scale), int(imgLogo.shape[HEIGHT] * scale))
imgLogo = cv2.resize(imgLogo, newSize)


while True:
    ret, frame = video.read()
    h_frame, w_frame = frame.shape[:2]
    h_imgLogo, w_imgLogo = imgLogo.shape[:2]

    roi = frame[
        startPoint : startPoint + h_imgLogo, startPoint : startPoint + w_imgLogo
    ]
    result = cv2.addWeighted(roi, 0, imgLogo, 1, 0)
    frame[
        startPoint : startPoint + h_imgLogo, startPoint : startPoint + w_imgLogo
    ] = result
    cv2.imshow("video capture original", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
