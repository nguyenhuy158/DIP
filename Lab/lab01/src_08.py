import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

start_point = (5, 5)
end_point = (220, 220)
color = (255, 255, 0)  
thickness = 9
img = cv2.rectangle(img, start_point, end_point, color, thickness)
  
cv2.imshow("Exercises 8", img)
cv2.waitKey(0)
cv2.destroyAllWindows()