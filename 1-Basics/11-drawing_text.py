import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np



image = np.zeros((512, 512, 3), np.uint8) # Draws a black background
cv2.putText(
	image, 						# Actual image where we're going to draw
	'Hello world!', 			# Desired text to be displayed
	(50, 290), 					# Bottom left text starting coordinate
	cv2.FONT_HERSHEY_COMPLEX, 	# Desired font to display text
	2, 							# Font size
	(100, 170, 0), 				# Font color
	3 							# Font thickness
)

# Other fonts supported by OpenCV
# FONT_HERSHEY_SIMPLEX,
# FONT_HERSHEY_PLAIN
# FONT_HERSHEY_DUPLEX
# FONT_HERSHEY_COMPLEX
# FONT_HERSHEY_TRIPLEX
# FONT_HERSHEY_COMPLEX_SMALL
# FONT_HERSHEY_SCRIPT_SIMPLEX
# FONT_HERSHEY_SCRIPT_COMPLEX

cv2.imshow('Hello world!', image)

cv2.waitKey(0)
cv2.destroyAllWindows()