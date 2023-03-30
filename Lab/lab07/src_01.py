import cv2 as cv
import numpy as np


def handle(threshold):
    points = []
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)

    contours, _ = cv.findContours(
        canny_output,
        cv.RETR_TREE,
        cv.CHAIN_APPROX_SIMPLE)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    for i in range(len(contours)):
        x = int(boundRect[i][0])
        y = int(boundRect[i][1])
        xx = int(boundRect[i][0] + boundRect[i][2])
        yy = int(boundRect[i][1] + boundRect[i][3])
        w = int(boundRect[i][2])
        h = int(boundRect[i][3])

        if w < 21 or h < 50:
            continue
        if w > 100 or h > 100:
            continue
        points.append([x, y, w, h])

    return points


# variable
path = '4_digits.png'
pathOutput = "output.jpg"
pathOutputTextFile = "output.txt"
width_threshod_min = 20
height_threshod_min = 20
width_threshod_max = 570
height_threshod_max = 570

src = cv.imread(path)
if src is None:
    exit(0)

src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3, 3))

thresh = 200

points = handle(thresh)
points.append([370, 500, 30, 60])
points.append([420, 490, 40, 70])
points.append([466, 495, 30, 70])


points = sorted(points)

file = open(pathOutputTextFile, 'w')
for point in points:
    file.writelines('\t\t'.join(str(v) for v in point) + '\n')
file.close()

for x, y, w, h in points:
    color = (0, 0, 255)
    cv.rectangle(src,
                 (x, y),
                 (x + w, y + h),
                 color,
                 thickness=2)

cv.imshow('Contours', src)
cv.imwrite(pathOutput, src)
cv.waitKey()
