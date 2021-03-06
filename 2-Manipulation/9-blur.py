import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Displays the original image for comparison
image = cv2.imread('../test.png')
cv2.imshow('Original image ', image)
cv2.waitKey(0)

# Creates 3x3 Kernel
kernel_3x3 = np.ones((3, 3), np.float32) / (3 * 3)
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernel blurring ', blurred)
cv2.waitKey(0)

# Creates 7x7 Kernel
kernel_7x7 = np.ones((7, 7), np.float32) /  (7 * 7)
blurred = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernel blurring ', blurred)
cv2.waitKey(0)

# Creates 50x50 Kernel
# The bigger is the matrix 
# the more expensive is the 
# computional process
kernel_50x50 = np.ones((50, 50), np.float32) / (50 * 50)
blurred = cv2.filter2D(image, -1, kernel_50x50)
cv2.imshow('50x50 Kernel blurring ', blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Displays the original image again for comparison
image = cv2.imread('../test.png')
cv2.imshow('Original image ', image)
cv2.waitKey(0)

# Averages pixels by convolving image with a normalized box filter
blur = cv2.blur(image, (3, 3))
cv2.imshow('OpenCV Blur (Box Blur)', blur)
cv2.waitKey(0)

# Gaussian Kernel
gauss = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('OpenCV Blur (Gaussian Blur) ', gauss)
cv2.waitKey(0)

# Takes a median of all the pixels under kernel area
median = cv2.medianBlur(image, 5)
cv2.imshow('OpenCV Blur (Median Blur) ', median)
cv2.waitKey(0)

# This is very effective for noise removal
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('OpenCV Blur (Bilateral Filter) ', bilateral)
cv2.waitKey()

cv2.destroyAllWindows()
