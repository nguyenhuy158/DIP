import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

center_coordinates = (120, 100)
axesLength = (100, 50)
angle = 0
startAngle = 0
endAngle = 360
color = (255, 255, 0)  
thickness = 9
img = cv2.ellipse(img, center_coordinates, axesLength,
           angle, startAngle, endAngle, color, thickness)
  
cv2.imshow("Exercises 6", img)
cv2.waitKey(0)
cv2.destroyAllWindows()