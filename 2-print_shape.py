import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import numpy
import matplotlib
import cv2

input = cv2.imread('./teste.jpg')
print input.shape
print 'Image WIDTH: '  , int(input.shape[1]), ' pixels'
print 'Image HEIGHT: ' , int(input.shape[0]), ' pixels'
