import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

image = cv2.imread('../test.png')

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow('Fast Means Denoising ', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()