import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2

input = cv2.imread('./../test.png')
print input
cv2.imshow('Imshow test', input)
cv2.waitKey()
cv2.destroyAllWindows()
