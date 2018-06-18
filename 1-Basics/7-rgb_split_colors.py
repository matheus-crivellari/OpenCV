import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2

# Loads the actual physical image from the disk
image = cv2.imread('./../test.jpg')

# Splits the image into each color index
B, G, R = cv2.split(image)

print B.shape

cv2.imshow('Red',   R) 	# These are going to display images in greyscale actually, because each splitted channel is only one dimension long
cv2.imshow('Green', G) 	# These are going to display images in greyscale actually, because each splitted channel is only one dimension long
cv2.imshow('Blue',  B) 	# These are going to display images in greyscale actually, because each splitted channel is only one dimension long

cv2.waitKey()
cv2.destroyAllWindows()

# Re-build the original image
merged = cv2.merge([B, G, R]) # Remember OpenCV is always Blue, Green and Red
cv2.imshow('Merged', merged)

cv2.waitKey()
cv2.destroyAllWindows()

# Amplifies the Blue color channel by the amount of 100
merged = cv2.merge([B+100, G, R])
cv2.imshow('Merged with Blue amplified', merged)

cv2.waitKey()
cv2.destroyAllWindows()

import numpy as np

zeroes = np.zeros(image.shape[:2], dtype="uint8")

# Displays each color channel actually tinted with it respective color
cv2.imshow('Red', 	cv2.merge([zeroes, zeroes, R])) # These are going to display each channel with respective tinted color.
cv2.imshow('Green', cv2.merge([zeroes, G, zeroes])) # These are going to display each channel with respective tinted color.
cv2.imshow('Blue', 	cv2.merge([B, zeroes, zeroes])) # These are going to display each channel with respective tinted color.

cv2.waitKey()
cv2.destroyAllWindows()