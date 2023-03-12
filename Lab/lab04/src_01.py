import cv2


path = "4_sudoku.png"
pathOutput = "image_01_01.png"

image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
image = cv2.medianBlur(image, cv2.MORPH_TOPHAT)

output = cv2.adaptiveThreshold(image,
                               255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY,
                               11,
                               2)

cv2.imshow("Exercises 1", output)
cv2.imwrite(pathOutput, output)
cv2.waitKey(0)
cv2.destroyAllWindows()
