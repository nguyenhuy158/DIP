import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)


B, G, R = cv2.split(img)

cv2.imshow("Exercises 9 - Original", img)
cv2.waitKey(0)

cv2.imshow("Exercises 9 - Blue", B)
cv2.waitKey(0)

cv2.imshow("Exercises 9 - Green", G)
cv2.waitKey(0)

cv2.imshow("Exercises 9 - Red", R)
cv2.waitKey(0)


cv2.imshow("Exercises 9", img)
cv2.waitKey(0)
cv2.destroyAllWindows()