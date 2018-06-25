import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Lets make our image displaying 
# easier by declaring a function
def display(image, title='Scalling, Re-sizing and Transposition '):
	cv2.imshow(title, image)
	cv2.waitKey()
	cv2.destroyAllWindows()

# Declares a scalling factor
scalling_factor = 0.5

# Load image
original = cv2.imread('../test.png')

display(original) # Displays the original iamge

# Resizes image down by .5, that is: make it 50% of its original size
image = cv2.resize(original, None, fx=scalling_factor, fy=scalling_factor)
display(image, title='Linear Interpolation Scalling ') # Displays the resized image

# Resizes image up double its original size (Cubic Interpolation)
scalling_factor = 2
image = cv2.resize(original, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_CUBIC)
display(image, title='Cubic Interpolation Scalling ') # Displays the resized image

# Resize image by setting exact dimensions
image = cv2.resize(original, (128, 256), interpolation=cv2.INTER_AREA)
display(image, title='Scalling - Skewed size ')