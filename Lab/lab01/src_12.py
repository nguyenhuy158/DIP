import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(img, (1050, 1610))
 
stretch_near = cv2.resize(img, (780, 540),
               interpolation = cv2.INTER_LINEAR)
 
 
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[img, half, bigger, stretch_near]
count = 4
 
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
 
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()