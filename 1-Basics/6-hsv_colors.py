import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2

image = cv2.imread('./../test.jpg')

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', image)
cv2.imshow('Hue Channel', image[:,:,0])
cv2.imshow('Sat. Channel', image[:,:,1])
cv2.imshow('Value(Brightness) Channel', image[:,:,2])

cv2.waitKey()
cv2.destroyAllWindows()