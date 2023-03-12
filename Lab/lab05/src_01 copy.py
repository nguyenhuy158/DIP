import cv2

import numpy as np

image_path = "image_demo.jpg"
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
noise_image = np.zeros(gray_image.shape[:2])
cv2.randu(noise_image, 0, 255)

noise_image = np.array(noise_image, dtype=np.uint8)
noise_gray = cv2.add(
    gray_image,
    np.array(noise_image * 0.2, dtype=np.uint8),
)

cv2.imshow("noise_gray", noise_gray)
cv2.imshow("noise_image", noise_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
