import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Lets make our image displaying 
# easier by declaring a function
def display(image, title='Masking '):
	cv2.imshow(title, image)
	cv2.waitKey()
	cv2.destroyAllWindows()

# Makes a square
square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
display(square)

# Makes an ellipse
ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
display(ellipse)

# Shows only where both images intersect
And = cv2.bitwise_and(square, ellipse)
display(And, 'And Operation (Intersection)')

# Shows both images combined
Or = cv2.bitwise_or(square, ellipse)
display(Or, 'Or Operation (Combine)')

# Shows only the part not intersecting between both images
Xor = cv2.bitwise_xor(square, ellipse)
display(Xor, 'Xor Operation (Exclusion)')

# Shows inverted square colors
Not = cv2.bitwise_not(square)
display(Not, 'Not Square (Inverted square)')

# Shows inverted ellipse colors
Not = cv2.bitwise_not(ellipse)
display(Not, 'Not Ellipse (Inverted ellipse)')
