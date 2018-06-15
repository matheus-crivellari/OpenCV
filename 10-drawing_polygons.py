import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8) # Draws a black background

# Defines four vertexes
pts = np.array([
		[10, 50], 
		[400, 50], 
		[90, 200], 
		[50, 500]
	],
	np.int32
)

# Reshapes the vertexes in form (required by polylines function)
pts = pts.reshape((-1, 1, 2))

cv2.polylines(
	image,  		# Actual image where we're going to draw
	[pts],  		# Array of shapes representing our polygon's vertexes
	True,  			# Wheather the polygon is supposed to close itself or not 
	(0, 0, 255),  	# B, G, R line/fill color
	1 				# Polygon's outline thickness
)
cv2.imshow('Polygon', image)

cv2.waitKey()
cv2.destroyAllWindows()