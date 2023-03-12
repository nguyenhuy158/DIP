import cv2
import numpy as np
from matplotlib import pyplot as plt

imageSource = "5_histogram.jpeg"
image = cv2.imread(imageSource)
outputFigure = "image_03_03.png"
n = 2
m = 2
kernelSize = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernelSize)
sharpOther = cv2.GaussianBlur(src=image, ksize=(9, 9), sigmaX=10)
sharpOther = cv2.addWeighted(src1=image, alpha=1.5, src2=sharpOther, beta=-0.5, gamma=0)
cv2.imshow("Exercise 2: blur version 1", np.hstack((image, sharp)))
cv2.imshow("Exercise 2: blur version 2", np.hstack((image, sharpOther)))
cv2.imwrite("image_03_01.png", np.hstack((image, sharp)))
cv2.imwrite("image_03_02.png", np.hstack((image, sharpOther)))
cv2.waitKey(0)
cv2.destroyAllWindows()

figure, axs = plt.subplots(n, m)
figure.set_size_inches(10, 7)
figure.suptitle("Exercise 3: Sharp image")
plt.tight_layout(h_pad=1)
axs[0][0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0][0].set_title("original: ")
axs[0][1].imshow(cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB))
axs[0][1].set_title("sharp v1: filter2D")
axs[1][0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[1][0].set_title("original: ")
axs[1][1].imshow(cv2.cvtColor(sharpOther, cv2.COLOR_BGR2RGB))
axs[1][1].set_title("sharp v2: gaussian + addWeigh")
plt.savefig(outputFigure)
plt.show()
