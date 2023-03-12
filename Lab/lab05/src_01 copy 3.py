import cv2
import numpy as np
from matplotlib import pyplot as plt

imageSource = "./flower.png"
image = cv2.imread(imageSource)

grayImage = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

equalizeHistogram = cv2.equalizeHist(src=grayImage)
print(grayImage.ravel())
print(grayImage)
print(type(grayImage))
plt.hist(grayImage.ravel(), 256, [0, 256])


# figure = plt.figure()
# image1 = figure.add_subplot(2, 2, 1)
# image1.imshow(grayImage)
# image1 = figure.add_subplot(2, 2, 2)
# image1.imshow(image)
# image1 = figure.add_subplot(2, 2, 3)
# image1.imshow(equalizeHistogram)

plt.show()
# cv2.imshow("windown 1", grayImage)
cv2.imshow("windown", np.vstack((grayImage, equalizeHistogram)))
cv2.waitKey(0)
cv2.destroyAllWindows()
