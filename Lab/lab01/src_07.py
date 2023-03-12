import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

center_coordinates = (120, 100)
radius = 20
color = (255, 255, 0)  
thickness = 9
img = cv2.circle(img, center_coordinates, radius, color, thickness)
  
cv2.imshow("Exercises 7", img)
cv2.waitKey(0)
cv2.destroyAllWindows()