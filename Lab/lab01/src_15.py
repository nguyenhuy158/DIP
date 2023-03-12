import cv2


path = r"D:\open-cv\image_input.jpg"
path_ouput = r"D:\open-cv\image_output"

img = cv2.imread(path)

(height, width) = img.shape[:2]
res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

cv2.imwrite(path_ouput+"resize.jpg", res)

(rows, cols) = img.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))
cv2.imwrite(path_ouput+"warpAffine.jpg", res)

cv2.imshow("Exercises 15", img)
cv2.waitKey(0)
cv2.destroyAllWindows()