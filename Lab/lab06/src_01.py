# ============================== Import library ==============================
import cv2
import sys
import math
import cv2 as cv
import numpy as np

# ============================== Default value ==============================
path_image_sudoku = 'sudoku-original.jpg'
path_image_circle = 'hough_circles_demo_01.png'



# ============================== Edge detection ==============================
img = cv2.imread(path_image_sudoku) 
# pre-process
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
# sobel algorithm 
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
# canny algorithm
edges = cv2.Canny(image=img_blur, threshold1=80, threshold2=180)
# show
cv2.imshow('Original', img)
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel X & Y', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Original', img)
cv2.imshow('Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save
cv2.imwrite('Sobel X.png', sobelx)
cv2.imwrite('Sobel Y.png', sobely)
cv2.imwrite('Sobel X & Y.png', sobelxy)
cv2.imwrite('Canny.png', edges)



# ============================== Line detection using Hough transform ==============================
img = cv.imread(cv.samples.findFile(path_image_sudoku), cv.IMREAD_GRAYSCALE)
# pre-process
dst = cv.Canny(img, 50, 200, None, 3)
cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
cdstP = np.copy(cdst)
# HoughLines
lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
# HoughLinesP
linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

# show
cv.imshow("Source", img)
cv.imshow("Detected Lines using HoughLines()", cdst)
cv.imshow("Detected Lines using HoughLinesP()", cdstP)
cv.waitKey()
cv2.destroyAllWindows()
# save
cv.imwrite("Source.png", img)
cv.imwrite("Detected Lines using HoughLines().png", cdst)
cv.imwrite("Detected Lines using HoughLinesP().png", cdstP)



# ============================== Circle detection using Hough transform ==============================
img = cv.imread(cv.samples.findFile(path_image_circle), cv.IMREAD_COLOR)
# pre-process
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
rows = gray.shape[0]
# HoughCircles()
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                            param1=100, param2=30,
                            minRadius=1, maxRadius=30)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(img, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv.circle(img, center, radius, (255, 0, 255), 3)
# show
cv.imshow("Detected circles", img)
cv.waitKey(0)
cv2.destroyAllWindows()
# save
cv.imwrite("Detected circles.png", img)



# ============================== End ==============================
