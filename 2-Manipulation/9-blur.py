import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

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
kernel_50x50 = np.ones((50, 50), np.float32) / (50 * 50)
blurred = cv2.filter2D(image, -1, kernel)
cv2.imshow('50x50 Kernel blurring ', blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()
