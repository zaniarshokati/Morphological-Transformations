import cv2
import numpy as np
from matplotlib import pyplot as plt

# read an image
img = cv2.imread('coin.jpeg',cv2.IMREAD_GRAYSCALE)

img = cv2.bitwise_not(img)
# define the kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) 

# perform erosion
erosion = cv2.erode(img, kernel, iterations=1)

# perform dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Apply opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Apply closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Apply gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# perform top hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# perform black hat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# titles = ['Original Image', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient', 'Top Hat', 'Black Hat']
# images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]
titles = ['Original Image', 'Black Hat']
images = [img, blackhat]


for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],cmap='Greys_r')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


# cv2.imwrite("erosion.jpg",erosion)
# cv2.imwrite("dilation.jpg",dilation)
# cv2.imwrite("opening.jpg",opening)
# cv2.imwrite("closing.jpg",closing)
# cv2.imwrite("gradient.jpg",gradient)
# cv2.imwrite("tophat.jpg",tophat)
# cv2.imwrite("blackhat.jpg",blackhat)
# # display the result
# cv2.imshow('Erosion', erosion)
# cv2.waitKey(0)