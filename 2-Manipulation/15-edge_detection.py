# Definition:
# Edges are sudden changes in an image.
# They carry as much information as pixels.

import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Loads test image as grey scale
image = cv2.imread('../test.png', 0)

# Prepares the image -----------------------------------------
# Extracts image height and width
height, width = image.shape;

# If your image is noisy, removes the noise before proceeding
image = cv2.fastNlMeansDenoising(image, None, 6, 6, 7)

# Sobel Edge Detection Algorithm -----------------------------
# Extracts Sobel horizontal edges
sobelX = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Extracts Sobel vertical edges
sobelY = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

# Displays original image
cv2.imshow('Original image ', image)

# Displays Edge Detection with Sobel Algorithm applyied to X axis
cv2.imshow('Sobel Edge Detection X ', sobelX)

# Displays Edge Detection with Sobel Algorithm applyied to Y axis
cv2.imshow('Sobel Edge Detection Y ', sobelY)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Adds both Sobel edge detections together using bitwise operations
sobelOr = cv2.bitwise_or(sobelX, sobelY)

# Displays Sobel Algorithm Edge Detection with both X and Y axes
cv2.imshow('Sobel OR ', sobelOr)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Laplacian Edge Detection Algorithm -----------------------------
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian Edge Detection Algorithm ', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Canny Edge Detection Algorithm ---------------------------------
# Two threshold values: threshold1 and threshold2.
# Any values larger than threshold2 is considered to be an edge.
# Any value smaller than threshold1 is considered no to be an edge.
# Values in between are either considered to be edges or not based 
# on their intensities.
canny = cv2.Canny(image, 20, 170)
cv2.imshow('Canny Edge Detection Algorithm ', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()