import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

start_point = (0, 0)
end_point = (250, 250)
color = (255, 255, 0)  
thickness = 9
img = cv2.arrowedLine(img, start_point, end_point, color, thickness)
  
cv2.imshow("Exercises 5", img)
cv2.waitKey(0)
cv2.destroyAllWindows()