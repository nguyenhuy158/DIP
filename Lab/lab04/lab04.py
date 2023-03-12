import cv2 as cv
import numpy as np

# img = cv.imread(r'C:\Users\THC\Desktop\XLA\Src\4_sudoku.png', 0)
# img = cv.medianBlur(img, 5)

# ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
# th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)

# titles = ['Original and blurred Image', 'Global Thresholding (v = 127)',
            # 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in range(4):
    # cv.imshow(titles[i], images[i])

# cv.waitKey(0)

# import cv2 as cv

# img = cv.imread(r'C:\Users\THC\Desktop\XLA\Src\4_sudoku.png', 0)

# ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# cv.imshow("Global Thresholding (v = 127)", th1)
# cv.imshow("Otsu's thresholding", th2)
# cv.waitKey(0)

# import cv2
# import numpy as np

# img = cv2.imread(r'C:\Users\THC\Desktop\XLA\Src\j.png',0)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)
# dilation = cv2.dilate(img,kernel,iterations = 1)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# cv2.imshow("J", img)
# cv2.imshow("J new", blackhat)
# cv.waitKey(0)

import cv2
#2
img = cv2.imread(r'C:\Users\THC\Desktop\XLA\Src\threshold.png')
img_gray = cv2.imread(r'C:\Users\THC\Desktop\XLA\Src\threshold.png',0)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY)
kernel = np.ones((27,27),np.uint8)dillation = cv2.dilate(thresh, kernel,iterations = 1)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=dillation, mode=cv2.RETR_TREE, 
							method=cv2.CHAIN_APPROX_NONE)  
# draw contours on the original image
image_copy = img.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, 
				color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

for cnt in contours:
	x,y,w,h = cv.boundingRect(cnt)
	cv.rectangle(image_copy,(x,y),(x+w,y+h),(0,255,0),2)

#cv2.imshow('dillation', dillation)
cv2.imshow('Ex2. Drawed contours', image_copy)

#3
img = cv2.imread(r'C:\Users\THC\Desktop\XLA\Src\4_digits.png')
img_gray = cv2.imread(r'C:\Users\THC\Desktop\XLA\Src\4_digits.png',0)
#img_denoised = cv.medianBlur(img_gray, 5)
img_denoised =  cv.GaussianBlur(img_gray,(9,9),0)
#img_denoised = cv.bilateralFilter(img_gray,9,75,75)

#thresh = cv2.adaptiveThreshold(img_denoised,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,9,2)
ret, thresh = cv2.threshold(img_denoised, 80, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3),np.uint8)
opening = cv2.dilate(thresh, kernel)
opening = cv2.erode(opening, kernel)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=opening, mode=cv2.RETR_TREE, 
							method=cv2.CHAIN_APPROX_NONE)  

for cnt in contours:
	x,y,w,h = cv.boundingRect(cnt)
	cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                           
#cv2.imshow('denoised', img_denoised)
cv2.imshow('thresh', thresh)
#cv2.imshow('opening', opening)
cv2.imshow('Drawed contours', img) 

cv2.waitKey(0)


