import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Read the image
image = cv2.imread('./../test.png')

# Transpose the image
rotated_image = cv2.transpose(image)

cv2.imshow('Tranposed image (Rotated 90 degress by transposing matrix) ', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()