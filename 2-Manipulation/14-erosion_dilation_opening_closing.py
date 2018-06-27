import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png', 0)

# As our original image is a pretty complex GBR image
# lets do some preparations before going to the point.
# Lets remove noise by applying gaussian blur
# and Otsu's thresholding so we have a more binary image.
# It's also possible to ignore preparation steps to see what's
# the effect of erosion, dilation, opening and closing on BGR images.

# Preparations: 
# Good practive to blur images as it removes noise
image = cv2.GaussianBlur(image, (3, 3), 0)

# Otsu's Thresholding 
_, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Displays original image
cv2.imshow('Original image ', image)

# Creates the kernel for erosion
kernel = np.ones((5, 5), np.uint8)

# Erodes the image:
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow('Erosion ', erosion)

# Dilates the image (same kernel):
dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilation ', dilation)

# Opens the image (same kernel):
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening ', opening)

# Closes the image (same kernel):
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing ', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()