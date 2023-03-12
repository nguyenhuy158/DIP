import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)
img1 = cv2.imread(path)
  
weightedSum = cv2.addWeighted(img, 0.5, img1, 0.4, 0)
  
cv2.imshow("Exercises 10", img)
cv2.waitKey(0)
cv2.imshow("Exercises 10 - Weighted Image", weightedSum)
cv2.waitKey(0)

path = r"D:\open-cv\image_input_other.jpg"
img1 = cv2.imread(path)
sub = cv2.subtract(img, img1)
cv2.imshow("Exercises 10", img)
cv2.waitKey(0)
cv2.imshow("Exercises 10 - subtract", sub)
cv2.waitKey(0)

cv2.destroyAllWindows()