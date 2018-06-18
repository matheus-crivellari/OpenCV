import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2

input = cv2.imread('./../test.jpg')
print input.shape
print 'Image WIDTH: '  , int(input.shape[1]), ' pixels'
print 'Image HEIGHT: ' , int(input.shape[0]), ' pixels'

cv2.imshow('BGR', input)
cv2.waitKey()
cv2.destroyAllWindows()

grayscale = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', grayscale)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite('grayscale.jpg', grayscale)