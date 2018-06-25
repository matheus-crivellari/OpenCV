import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png')
height, width = image.shape[:2]

startX, startY 	= int(height * .25), int(width * .25)
endX, endY 		= int(height * .75), int(height * .75)

cropped = image[startX:endX, startY:endY]

cv2.imshow('Original image ', image)
cv2.waitKey(0)
cv2.imshow('Cropped image ', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
