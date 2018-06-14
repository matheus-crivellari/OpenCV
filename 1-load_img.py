import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import numpy
import matplotlib
import cv2

input = cv2.imread('./teste.jpg')
print input
cv2.imshow('Imshow test', input)
cv2.waitKey()
cv2.destroyAllWindows()
