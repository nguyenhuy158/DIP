import cv2
import numpy as np
from matplotlib import pyplot as plt

imageSource = "5_histogram.jpeg"
image = cv2.imread(imageSource)
outputFigure = "image_01_01.png"
output = "image_01_02.png"

grayImage = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
equalizationHistogram = cv2.equalizeHist(src=grayImage)

cv2.imshow("Exercise 1", np.hstack((grayImage, equalizationHistogram)))
cv2.imwrite(output, np.hstack((grayImage, equalizationHistogram)))
cv2.waitKey(0)
cv2.destroyAllWindows()

figure, axs = plt.subplots(2, 2)
figure.suptitle("Exercise 1: equalization Histogram")
plt.tight_layout(h_pad=1.5)
# axs[0][0].plot(cv2.calcHist([grayImage], [0], None, [256], [0, 256]))
axs[0][0].hist(grayImage.ravel(), 256, [0, 256])
axs[0][1].imshow(grayImage, cmap="gray")
axs[0][1].set_title("Gray normal")
# axs[0][0].plot(cv2.calcHist([equalizationHistogram], [0], None, [256], [0, 256]))
axs[1][0].hist(equalizationHistogram.ravel(), 256, [0, 256])
axs[1][1].imshow(equalizationHistogram, cmap="gray")
axs[1][1].set_title("Equalization Histogram")

plt.savefig(outputFigure)
plt.show()
