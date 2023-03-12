# importing numpy to work with pixels
import numpy as np
import cv2


fileOutput1st = "image_03_01.png"
fileOutput2nd = "image_03_02.png"
kernel = np.ones((5, 5), np.uint8)

path = "threshold.png"
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 3.1.a
thresh = 170
maxValue = 255

th, output1st = cv2.threshold(image, thresh, maxValue, cv2.THRESH_BINARY_INV)
output1st = cv2.morphologyEx(output1st, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(fileOutput1st, output1st)
cv2.imshow(fileOutput1st, output1st)

# 3.1.b
thresh = 170
maxValue = 255

th, output2nd = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TOZERO_INV)
output2nd = cv2.morphologyEx(output2nd, cv2.MORPH_OPEN, kernel)
thresh = 0
maxValue = 255
th, output2nd = cv2.threshold(output2nd, thresh, maxValue, cv2.THRESH_BINARY)
cv2.imwrite(fileOutput2nd, output2nd)
cv2.imshow(fileOutput2nd, output2nd)


# 3.2
cv2.destroyAllWindows()
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([0, 0, 255])
upper = np.array([0, 0, 255])

mask255 = cv2.inRange(image, lower, upper)
output255 = cv2.bitwise_and(image, image, mask=mask255)

lower = np.array([0, 0, 200])
upper = np.array([0, 0, 200])

mask200 = cv2.inRange(image, lower, upper)
output200 = cv2.bitwise_and(image, image, mask=mask200)

lower = np.array([0, 0, 180])
upper = np.array([0, 0, 180])

mask180 = cv2.inRange(image, lower, upper)
output180 = cv2.bitwise_and(image, image, mask=mask180)

lower = np.array([0, 0, 128])
upper = np.array([0, 0, 128])

mask128 = cv2.inRange(image, lower, upper)
output128 = cv2.bitwise_and(image, image, mask=mask128)

lower = np.array([0, 0, 100])
upper = np.array([0, 0, 100])

mask100 = cv2.inRange(image, lower, upper)
output100 = cv2.bitwise_and(image, image, mask=mask100)

lower = np.array([0, 0, 64])
upper = np.array([0, 0, 64])

mask64 = cv2.inRange(image, lower, upper)
output64 = cv2.bitwise_and(image, image, mask=mask64)

lower = np.array([0, 0, 32])
upper = np.array([0, 0, 32])

mask32 = cv2.inRange(image, lower, upper)
output32 = cv2.bitwise_and(image, image, mask=mask32)

output255 = cv2.cvtColor(output255, cv2.COLOR_HSV2RGB)
output200 = cv2.cvtColor(output200, cv2.COLOR_HSV2RGB)
output180 = cv2.cvtColor(output180, cv2.COLOR_HSV2RGB)
output128 = cv2.cvtColor(output128, cv2.COLOR_HSV2RGB)
output100 = cv2.cvtColor(output100, cv2.COLOR_HSV2RGB)
output64 = cv2.cvtColor(output64, cv2.COLOR_HSV2RGB)
output32 = cv2.cvtColor(output32, cv2.COLOR_HSV2RGB)


cv2.imwrite("image_03_03.png", output255)
cv2.imwrite("image_03_04.png", output200)
cv2.imwrite("image_03_05.png", output180)
cv2.imwrite("image_03_06.png", output128)
cv2.imwrite("image_03_07.png", output100)
cv2.imwrite("image_03_08.png", output64)
cv2.imwrite("image_03_09.png", output32)
# cv2.imshow("output255", output255)
# cv2.imshow("output200", output200)
# cv2.imshow("output180", output180)
# cv2.imshow("output128", output128)
# cv2.imshow("output100", output100)
# cv2.imshow("output64", output64)
# cv2.imshow("output32", output32)
cv2.waitKey(0)
