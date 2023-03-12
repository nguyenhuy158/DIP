import cv2
import numpy as np

path = r"lab02_ex.png"
img = cv2.imread(path)
# 1. Split each color channel of the image
# split
b, g, r = cv2.split(img)
# show
cv2.imshow("Exercises 1.1 - original", img)
cv2.imshow("Exercises 1.1 - red channel", r)
cv2.imshow("Exercises 1.1 - green channel", g)
cv2.imshow("Exercises 1.1 - blue channel", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Locate the position of each balloon by drawing a rectangle (bounding-box)
# surrounding each balloon
light_blue_color = (250, 250, 0)
thickness = 2
# yellow
start_yellow_point = (25, 10)
end_yellow_point = (140, 150)
output = cv2.rectangle(
    img, start_yellow_point, end_yellow_point, light_blue_color, thickness
)
# blue
start_blue_point = (145, 60)
end_blue_point = (235, 200)
output = cv2.rectangle(
    img, start_blue_point, end_blue_point, light_blue_color, thickness
)
# red
start_red_point = (250, 18)
end_red_point = (355, 160)
output = cv2.rectangle(img, start_red_point, end_red_point, light_blue_color, thickness)
# green
start_green_point = (375, 60)
end_green_point = (475, 200)
output = cv2.rectangle(
    img, start_green_point, end_green_point, light_blue_color, thickness
)
# orange
start_orange_point = (490, 20)
end_orange_point = (590, 150)
output = cv2.rectangle(
    img, start_orange_point, end_orange_point, light_blue_color, thickness
)
# show
cv2.imshow("Exercises 1.2 - surrounding", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Name each balloon by putting a text of color name right above the bounding boxes.
green_color = (0, 250, 0)
font = cv2.FONT_HERSHEY_PLAIN
fontScale = 1
# yellow
output = cv2.putText(img, "Yellow", start_yellow_point, font, fontScale, green_color)
# blue
output = cv2.putText(img, "Blue", start_blue_point, font, fontScale, green_color)
# red
output = cv2.putText(img, "Red", start_red_point, font, fontScale, green_color)
# green
output = cv2.putText(img, "Green", start_green_point, font, fontScale, green_color)
# orange
output = cv2.putText(img, "Orange", start_orange_point, font, fontScale, green_color)
# show
cv2.imshow("Exercises 1 - 1.3 write text", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Extract the yellow balloon by creating a new image of only one balloon.
ROW = 1
COLUMN = 0

yellowBallFileName = "yellowBall.jpg"
blueBallFileName = "blueBall.jpg"
redBallFileName = "redBall.jpg"
greenBallFileName = "greenBall.jpg"
orangeBallFileName = "orangeBall.jpg"

yellowBall = img[
    start_yellow_point[ROW] : end_yellow_point[ROW],
    start_yellow_point[COLUMN] : end_yellow_point[COLUMN],
]
cv2.imwrite(yellowBallFileName, yellowBall)

blueBall = img[
    start_blue_point[ROW] : end_blue_point[ROW],
    start_blue_point[COLUMN] : end_blue_point[COLUMN],
]
cv2.imwrite(blueBallFileName, blueBall)

redBall = img[
    start_red_point[ROW] : end_red_point[ROW],
    start_red_point[COLUMN] : end_red_point[COLUMN],
]
cv2.imwrite(redBallFileName, redBall)

greenBall = img[
    start_green_point[ROW] : end_green_point[ROW],
    start_green_point[COLUMN] : end_green_point[COLUMN],
]
cv2.imwrite(greenBallFileName, greenBall)

orangeBall = img[
    start_orange_point[ROW] : end_orange_point[ROW],
    start_orange_point[COLUMN] : end_orange_point[COLUMN],
]
cv2.imwrite(orangeBallFileName, orangeBall)

# show
cv2.imshow("Exercises 1.4 - yellowBall", yellowBall)
cv2.imshow("Exercises 1.4 - blueBall", blueBall)
cv2.imshow("Exercises 1.4 - redBall", redBall)
cv2.imshow("Exercises 1.4 - greenBall", greenBall)
cv2.imshow("Exercises 1.4 - orangeBall", orangeBall)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5. Extract the yellow balloon automatically by using HSV color space
# to extract only pixels of yellow color.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
yellowBall = cv2.bitwise_and(img, img, mask=yellow_mask)

lower_blue = np.array([94, 80, 2])
upper_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
blueBall = cv2.bitwise_and(img, img, mask=blue_mask)

lower_red = np.array([0, 160, 70])
upper_red = np.array([10, 250, 250])
red_mask = cv2.inRange(hsv, lower_red, upper_red)
redBall = cv2.bitwise_and(img, img, mask=red_mask)

lower_green = np.array([30, 50, 70])
upper_green = np.array([80, 250, 250])
green_mask = cv2.inRange(hsv, lower_green, upper_green)
greenBall = cv2.bitwise_and(img, img, mask=green_mask)

lower_orange = np.array([5, 50, 50])
upper_orange = np.array([15, 255, 255])
orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
orangeBall = cv2.bitwise_and(img, img, mask=orange_mask)

yellowBallFileName = "yellowBall-hsv.jpg"
blueBallFileName = "blueBall-hsv.jpg"
redBallFileName = "redBall-hsv.jpg"
greenBallFileName = "greenBall-hsv.jpg"
orangeBallFileName = "orangeBall-hsv.jpg"

# write
cv2.imwrite(yellowBallFileName, yellowBall)
cv2.imwrite(blueBallFileName, blueBall)
cv2.imwrite(redBallFileName, redBall)
cv2.imwrite(greenBallFileName, greenBall)
cv2.imwrite(orangeBallFileName, orangeBall)

# show
cv2.imshow("Exercises 1.5 - yellowBall", yellowBall)
cv2.imshow("Exercises 1.5 - blueBall", blueBall)
cv2.imshow("Exercises 1.5 - redBall", redBall)
cv2.imshow("Exercises 1.5 - greenBall", greenBall)
cv2.imshow("Exercises 1.5 - orangeBall", orangeBall)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Re-paint the yellow balloon by replacing the pixels of yellow by green.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

ouput = img.copy()
ouput[yellow_mask > 0] = green_color
# show
cv2.imshow("Exercises 1.6 - replace color", ouput)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Rotate the first balloon an angle of 20 degree
yellowBall = img[
    start_yellow_point[ROW] : end_yellow_point[ROW],
    start_yellow_point[COLUMN] : end_yellow_point[COLUMN],
]

(h, w) = yellowBall.shape[:2]
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, angle=20, scale=1)
rotated = cv2.warpAffine(yellowBall, M, (w, h))

# show
cv2.imshow("Exercises 1.7 - rotate img", rotated)
cv2.imwrite("rotate.jpg", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
