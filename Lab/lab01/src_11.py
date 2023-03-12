import cv2


path = r"D:\open-cv\image_input.jpg"
path1 = r"D:\open-cv\image_input_other.jpg"
img = cv2.imread(path)
img1 = cv2.imread(path1)
  
dest_and  = cv2.bitwise_and(img1, img, mask = None)

cv2.imshow("Exercises 11", img)
cv2.waitKey(0)
cv2.imshow("Exercises 11 - bitwise_and", dest_and)
cv2.waitKey(0)

dest_not = cv2.bitwise_not(img1, mask = None)

cv2.imshow("Exercises 11 - bitwise_xor", dest_not)
cv2.waitKey(0)
cv2.destroyAllWindows()