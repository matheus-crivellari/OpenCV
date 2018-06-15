import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2

image = cv2.imread('./test.jpg')

# BGR values for the first pixel
# OpenCV is always Blue, Green and Red instead of Red, Green and Blue as usual.
B, G, R = image[0,0]
print 'BGR image:\n'
print image.shape
print B,G,R # This will print values from 0 to 255 for each Blue Green and Red amount (three dimensions) for the first pixel

# Grayscale value for the first pixel
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print 'Grayscale image:\n'
print image.shape
G = image[0,0]
print G # This will print value from 0 to 255 for White amount (only one dimension) for the first pixel

