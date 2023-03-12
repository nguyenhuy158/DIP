import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
cv2.imshow("Exercises 14", img)
cv2.waitKey(0)
cv2.imshow("Exercises 14 - Grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()