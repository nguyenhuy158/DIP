import cv2
import numpy as np

path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      
lower_yellow = np.array([25, 50, 70])
upper_yellow = np.array([35, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
result = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("Exercises 17 - img", img)
cv2.imshow("Exercises 17 - mask", mask)
cv2.imshow("Exercises 17 - result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()