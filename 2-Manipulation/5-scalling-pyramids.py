import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2

image = cv2.imread('../test.png')

smaller = cv2.pyrDown(image)
larger  = cv2.pyrUp(smaller)

cv2.imshow('Original', 	image)
cv2.imshow('Smaller', 	smaller)
cv2.imshow('Larger', 	larger)
cv2.waitKey()
cv2.destroyAllWindows()
