
import cv2


path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)
height = img.shape[0]
width = img.shape[1]

font = cv2.FONT_HERSHEY_SIMPLEX
org = (width // 2, height // 2)
fontScale = 1
color = (226, 170, 227)
thickness = 2
img = cv2.putText(img, '52000668', org, font,
				fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("Exercises 3", img)

filename = "image_output.jpg"
cv2.imwrite(filename, img)

cv2.waitKey(0)
cv2.destroyAllWindows()

