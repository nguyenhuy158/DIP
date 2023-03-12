# importing numpy to work with pixels
import numpy as np
import cv2


path = "lab3_img1.png"
output = "image_01_01.png"
img = cv2.imread(path)

mask = np.zeros(img.shape[:2], dtype="uint8")
firstPoint = (145, 220)
firstRadius = 90
whiteColor = 255
thinkNessFull = -1
mask = cv2.circle(mask, firstPoint, firstRadius, whiteColor, thinkNessFull)

secondPoint = (430, 180)
secondRadius = 80
mask = cv2.circle(mask, secondPoint, secondRadius, whiteColor, thinkNessFull)

secondPoint = (700, 275)
secondRadius = 50
mask = cv2.circle(mask, secondPoint, secondRadius, whiteColor, thinkNessFull)

img = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite(output, img)
cv2.imshow("Exercises 1", img)
cv2.waitKey(0)
