# In Affine Transforms we only need 3 coordinates
# to obtain the correct transform

import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png')
height, width, ch = image.shape

cv2.imshow('Original ', image)

# Coordinates of original image's 4 corners
pointsA = np.float32([
	[158,  65], # First top corner
	[403, 186], # Second top corner
	[81,  526], # First bottom corner
])

# Coordinates of desired output's 4 corners
pointsB = np.float32([
	[0,0], 			 # First top corner
	[width, 0], 	 # Second top corner
	[0,height], 	 # First bottom corner
])

# Use tow sets of points to compute
# Perspective Transformation Matrix, M
M = cv2.getAffineTransform(pointsA, pointsB)

warped = cv2.warpAffine(image, M, (width, height))

cv2.imshow('Warped Perspective ', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()