import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png')
cv2.imshow('Original ', image)

kernel_sharp = np.array([
	[-1, -1, -1],
	[-1,  9, -1],
	[-1, -1, -1]
])

shapened = cv2.filter2D(image, -1, kernel_sharp)

cv2.imshow('Image Sharpening ', shapened)
cv2.waitKey(0)
cv2.destroyAllWindows()