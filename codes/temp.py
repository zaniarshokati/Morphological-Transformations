
import cv2 

# image1 = cv2.imread('input1.jpeg') 
   

# img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

  
# thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

# cv2.imwrite("thresh2.jpg",thresh2)

img = cv2.imread('thresh2.jpg')

# define the kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# perform erosion
erosion = cv2.erode(img, kernel, iterations=1)

# # display the result
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)