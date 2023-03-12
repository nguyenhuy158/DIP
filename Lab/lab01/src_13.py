import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

img = cv2.copyMakeBorder(img, 15, 15, 15, 15, cv2.BORDER_CONSTANT, None, value = 255)

cv2.imshow("Exercises 13", img)
cv2.waitKey(0)
cv2.destroyAllWindows()