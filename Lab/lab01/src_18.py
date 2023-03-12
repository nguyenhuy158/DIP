import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)
cv2.imshow("Exercises 18", img)
cv2.waitKey(0)

out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Exercises 18', out) 
cv2.waitKey(0)

out = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('Exercises 18', out) 
cv2.waitKey(0)

out = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Exercises 18', out) 
cv2.waitKey(0)

out = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('Exercises 18', out) 
cv2.waitKey(0)

out = cv2.cvtColor(img, cv2.CV_64F)
cv2.imshow('Exercises 18', out) 
cv2.waitKey(0)

cv2.destroyAllWindows()