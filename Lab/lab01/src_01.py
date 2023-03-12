
import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

cv2.imshow("Exercises 1", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
