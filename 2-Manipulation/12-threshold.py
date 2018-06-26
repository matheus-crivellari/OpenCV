import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png')

# Before thresholding, convert to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original greyscale image ', image)

# Values below 127 goes 0 and everything above 127 goes 255
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('1 - Binary Threshold ', thresh1)

# Values below 127 goes 255 and everything above 127 goes 0
# Inverse of the previous one
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('2 - Binary Threshold Inverse', thresh2)

# Values above 127 are truncated
# Third argument (0 in this case) is unused
ret, thresh3 = cv2.threshold(image, 127, 0, cv2.THRESH_TRUNC)
cv2.imshow('3 - Binary Threshold Truncate', thresh3)

# Values below 127 goes 0 and everything above 127 are not changed
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('4 - Binary Threshold Inverse', thresh4)

# Values below 127 are not changed and everything above 127 goes 0
# Inverse of the previous one
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('5 - Binary Threshold Inverse', thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
