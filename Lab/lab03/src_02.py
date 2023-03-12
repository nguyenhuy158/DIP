# importing numpy to work with pixels
import numpy as np
import cv2


output = "image_02_01.png"
pathPeople = "lab3_img1.png"
pathLogo = "lab3_img2.png"
imgPeople = cv2.imread(pathPeople)
imgLogo = cv2.imread(pathLogo)

# resize logo
imgLogo = cv2.resize(imgLogo, imgPeople.shape[1::-1])

# imgOutput = np.zeros(imgPeople.shape[:2], dtype="uint8")
imgOutput = cv2.addWeighted(imgPeople, 0.5, imgLogo, 0.5, 0)


cv2.imwrite(output, imgOutput)
cv2.imshow("Exercises 2", imgOutput)
cv2.waitKey(0)
