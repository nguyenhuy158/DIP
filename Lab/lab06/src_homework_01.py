# ============================== Import library ==============================
import cv2
import sys
import math
import cv2
import numpy as np

# ============================== Default value ==============================
path_image_sudoku = "sudoku-original.jpg"

# ============================== SuDoKu Grabber in OpenCV ==============================
image = cv2.imread(path_image_sudoku, 0)
image = cv2.GaussianBlur(image, (3, 3), 0)

# pre-process
blank_image = np.zeros(image.shape, np.uint8)

blur_image = cv2.GaussianBlur(image, (11, 11), 0)

blank_image = cv2.adaptiveThreshold(
    blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)

blank_image = cv2.bitwise_not(blank_image)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
blank_image = cv2.dilate(blank_image, kernel, iterations=1)

# SuDoKu Grabber algorithm
count = 0
max = -1
maxPt = None
area = 0
for y in range(blank_image.shape[0]):
    for x in range(blank_image.shape[1]):
        if blank_image[y][x] > 128:
            area, _, _, xx = cv2.floodFill(blank_image,
                                           np.zeros((blank_image.shape[0] + 2,
                                                    blank_image.shape[1] + 2),
                                                    np.uint8),
                                           (x, y),
                                           64)
            if (area > max):
                max = area
                maxPt = (x, y)

cv2.floodFill(blank_image,
              np.zeros((blank_image.shape[0] + 2,
                        blank_image.shape[1] + 2),
                       np.uint8),
              maxPt,
              255)

for y in range(blank_image.shape[0]):
    for x in range(blank_image.shape[1]):
        if blank_image[y][x] == 64 and x != maxPt[0] and y != maxPt[1]:
            cv2.floodFill(blank_image,
                          np.zeros((blank_image.shape[0] + 2,
                                    blank_image.shape[1] + 2),
                                   np.uint8),
                          (x, y),
                          0)

blank_image = cv2.erode(blank_image, kernel)
blank_image = cv2.dilate(blank_image, kernel)
blank_image = cv2.erode(blank_image, kernel)

# show
cv2.imshow("result", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save
cv2.imwrite("image_homework_01.png", blank_image)


# ============================== End ==============================
