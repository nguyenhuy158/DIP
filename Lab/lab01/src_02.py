
import cv2
import os

directory = r"D:\open-cv"
path = r"D:\open-cv\image_input.jpg"
img = cv2.imread(path)

print("Before")  
filtered = filter(lambda image: image.endswith(('.jpg', '.png', 'jpeg')), os.listdir(directory))
print(list(filtered))

filename = "image_output.jpg"
cv2.imwrite(filename, img)

print("After")  
filtered = filter(lambda image: image.endswith(('.jpg', '.png', 'jpeg')), os.listdir(directory))
print(list(filtered))