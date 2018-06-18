import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Draws a black RGB image
rgb_img = np.zeros((512, 512, 3), np.uint8)

# Draws a black Grayscale image
gray_img = np.zeros((512, 512), np.uint8)

cv2.imshow('Black image (RGB)', rgb_img)
cv2.imshow('Black image (Grayscale)', gray_img)

cv2.waitKey()
cv2.destroyAllWindows()

# ------------------------------------------------------

# Draws a diagonal blue line of 5pixels thick
image = np.zeros((512, 512, 3), np.uint8) # Draws a black background
cv2.line(
	image, 			# Actual image where we're going to draw
	(10,10), 		# X and y line beginning coordinates
	(501, 501), 	# X and y line ending coordinates
	(255, 127, 0), 	# B, G, R line color
	5 				# Line thickness
	)
cv2.imshow('Blue diagonal line', image)

cv2.waitKey()
cv2.destroyAllWindows()

# Draws a purple line rectangle (not filled)
image = np.zeros((512, 512, 3), np.uint8) # Draws a black background
cv2.rectangle(
	image, 				# Actual image where we're going to draw
	(100, 100), 		# X and y rectangle's origin vertex coordinates
	(300, 250), 		# X and y rectangle's opposite vertex coordinates
	(127, 50, 127), 	# B, G, R line/fill color
	1 					# Rectangle's outline thickness (negative value for filled rect)
)

cv2.imshow('Purple rectangle', image)

cv2.waitKey()
cv2.destroyAllWindows()

# Draws a green filled circle
image = np.zeros((512, 512, 3), np.uint8) # Draws a black background
cv2.circle(
	image, 				# Actual image where we're going to draw
	(256, 256), 		# X and Y circle's center coordinate
	128, 				# Circle's radius
	(0, 232, 127), 		# B, G, R line/fill color
	-1 					# Circle's outline thickness (negative value for filled circle)
)

cv2.imshow('Purple circle', image)

cv2.waitKey()
cv2.destroyAllWindows()