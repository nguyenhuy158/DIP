import cv2
import numpy as np

imageSource = "./src_image_01.jpeg"
image = cv2.imread(imageSource)

simpleOutput = cv2.blur(src=image, ksize=(5, 5))

gaussianOutput = cv2.GaussianBlur(src=image, ksize=(5, 5), sigmaX=0)

cv2.imshow("image", image)
cv2.imshow("simpleOutput", simpleOutput)
cv2.imshow("gaussianOutput", gaussianOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()
