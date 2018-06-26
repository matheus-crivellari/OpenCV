import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png')

# Creates a matrix filled with ones 
# with the same dimensions of the image
# and multiply it by a scaler of 100
M = np.ones(image.shape, dtype='uint8') * 175

# Increases britghtness by adding the matrix to the original image
added = cv2.add(image, M)
cv2.imshow('Added ', added)

# Decreases britghtness by subtracting the matrix to the original image
subtracted = cv2.subtract(image, M)
cv2.imshow('Subtracted ', subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
