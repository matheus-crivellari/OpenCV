import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Read the image
image = cv2.imread('./../test.jpg')

# Stores the image's width and height 
height, width = image.shape[:2]

# Creates a rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(
    (width/2, height/2),    # Rotation pivot at the center of the image
    90,                     # Rotation degrees
    .5                       # Scale factor
)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated image ', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()