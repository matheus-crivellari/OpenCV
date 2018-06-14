import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import numpy
import matplotlib
import cv2

image = cv2.imread('./teste.png')

cv2.imshow('Image show', image)
cv2.waitKey()
cv2.destroyAllWindows()