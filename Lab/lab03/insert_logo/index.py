import cv2
import matplotlib.pyplot as plt

image = cv2.imread("insert_logo/image3.png", cv2.IMREAD_COLOR)
logo = cv2.imread("insert_logo/image-3.png", cv2.IMREAD_COLOR)

h_image, w_image = image.shape[:2]
h_logo, w_logo = logo.shape[:2]

roi = image[0:h_logo, 0:w_logo]
result = cv2.addWeighted(roi, 0, logo, 1, 0)
image[0:h_logo, 0:w_logo] = result

cv2.imshow("mask_Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("insert_logo/mask_Image.jpg", image)
