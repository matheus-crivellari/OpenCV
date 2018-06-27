# Obtaining the perspective of Affine Transforms

import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test2.png')
height, width, channels = image.shape
cv2.waitKey(0)

# Coordinates of original image's 4 corners
rectA = np.float32([
	[158,  65], # First top corner
	[403, 186], # Second top corner
	[81,  526], # First bottom corner
	[320, 516], # Second bottom corner
])

# Coordinates of desired output's 4 corners
rectB = np.float32([
	[0,0], 			 # First top corner
	[width, 0], 	 # Second top corner
	[0,height], 	 # First bottom corner
	[width, height], # Second bottom corner
])

# The sequence of vertices above doesn't matter
# as long as both rects have their vertices 
# set in the same sequence.

M = cv2.getPerspectiveTransform(rectA, rectB)

warped = cv2.warpPerspective(image, M, (width, height))

cv2.imshow('Original ', image)
cv2.imshow('Warped Perspective ', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()