import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2

input = cv2.imread('./../test.jpg')
print input.shape
print 'Image WIDTH: '  , int(input.shape[1]), ' pixels'
print 'Image HEIGHT: ' , int(input.shape[0]), ' pixels'

cv2.imshow('Imwrite test', input)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite('./output.png', input)
cv2.imwrite('./output.jpg', input)