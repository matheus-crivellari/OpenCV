import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png')

# Before thresholding, convert to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Values below 127 goes 0, values above 127 goes 255
ret, tresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Threshold ', tresh1)

# Good practive to blur images as it removes noise
image = cv2.GaussianBlur(image, (3, 3), 0)

# Adaptive thresholding
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
cv2.imshow('Adaptive Mean Threshold ', thresh)

# Otsu's Thresholding 
_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu\'s Thresholding ', th2)

# Gaussian Otsu's Thresholding 
# Otsu's and Gaussian Otsu's thresholding are good for increasing readability of texts contained in images (e.g.: Scanned documents)
blur = cv2.GaussianBlur(image, (5 ,5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Gaussian Otsu\'s Thresholding ', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
