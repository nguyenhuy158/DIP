import cv2


path = "threshold.png"
pathOutput = "image_02_01.png"

output = cv2.imread(path)
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

ret, binaryTheshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

binaryTheshold = cv2.dilate(binaryTheshold, kernel, iterations=7)

contours, hierarchy = cv2.findContours(
    binaryTheshold, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE
)

for index in range(len(contours)):
    cnt = contours[index]
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Exercises 2", output)
cv2.imwrite(pathOutput, output)

cv2.waitKey(0)
cv2.destroyAllWindows()
