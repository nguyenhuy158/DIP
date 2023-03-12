import cv2
import numpy as np
from matplotlib import pyplot as plt

imageSource = "5_histogram.jpeg"
image = cv2.imread(imageSource)
outputFigure = "image_02_01.png"
n = 2
m = 3
blurSize = (5, 5)

grayImage = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
noiseImage = np.zeros(grayImage.shape[:2])
noiseImage = np.array(cv2.randu(noiseImage, 0, 255), dtype=np.uint8)
noiseImage = cv2.add(
    grayImage,
    np.array(noiseImage * 0.5, dtype=np.uint8),
)

blur = cv2.blur(src=image, ksize=blurSize)
boxFilter = cv2.boxFilter(src=image, ddepth=-1, ksize=blurSize)
gaussianBlur = cv2.GaussianBlur(src=image, ksize=blurSize, sigmaX=0)
medianBlur = cv2.medianBlur(src=image, ksize=blurSize[0])
bilateralFilter = cv2.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imshow("Exercise 2: blur", np.hstack((image, blur)))
cv2.imwrite("image_02_02.png", np.hstack((image, blur)))
cv2.imwrite("image_02_03.png", np.hstack((image, boxFilter)))
cv2.imwrite("image_02_04.png", np.hstack((image, medianBlur)))
cv2.imwrite("image_02_05.png", np.hstack((image, gaussianBlur)))
cv2.imwrite("image_02_06.png", np.hstack((image, bilateralFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()

figure, axs = plt.subplots(n, m)
figure.set_size_inches(10, 7)
figure.suptitle("Exercise 2: Blur")
plt.tight_layout(h_pad=1)
axs[0][0].imshow(noiseImage, cmap="gray")
axs[0][0].set_title("noiseImage")
axs[0][1].imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
axs[0][1].set_title("blur")
axs[0][2].imshow(cv2.cvtColor(boxFilter, cv2.COLOR_BGR2RGB))
axs[0][2].set_title("boxFilter")
axs[1][1].imshow(cv2.cvtColor(medianBlur, cv2.COLOR_BGR2RGB))
axs[1][1].set_title("medianBlur")
axs[1][0].imshow(cv2.cvtColor(gaussianBlur, cv2.COLOR_BGR2RGB))
axs[1][0].set_title("gaussianBlur")
axs[1][2].imshow(cv2.cvtColor(bilateralFilter, cv2.COLOR_BGR2RGB))
axs[1][2].set_title("bilateralFilter")

plt.savefig(outputFigure)
plt.show()
