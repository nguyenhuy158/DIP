import cv2
import time
import numpy as np

path = "4_digits.png"
pathOutput = "image_03_01.png"

output = cv2.imread(path)
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
image = cv2.medianBlur(image, 3)


ret, binaryTheshold = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)

# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

binaryTheshold = cv2.morphologyEx(binaryTheshold, cv2.MORPH_OPEN, kernel)
binaryTheshold = cv2.morphologyEx(binaryTheshold, cv2.MORPH_OPEN, kernel)

contours, hierarchy = cv2.findContours(
    image=binaryTheshold, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE
)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow("thresh", binaryTheshold)
cv2.imshow("Exercises 3", output)
cv2.imwrite(pathOutput, output)
cv2.waitKey(0)
cv2.destroyAllWindows()
