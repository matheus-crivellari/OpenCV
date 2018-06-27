import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Processes given input image, 
# computes grayscale, applies blur
# detect edges using Canny algorithm
# and returns a threshold using Inverted Binary algorithm
# Tresh 0 means Binarry Threshold, Thresh 1 means Adaptive Mean C Threshold
def sketch(image, thresh=0):
	output 		= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	output 		= cv2.GaussianBlur(output, (3, 3), 0)
	output 		= cv2.Canny(output, 10, 70)

	if(thresh == 0):
		ret, mask 	= cv2.threshold(output, 70, 255, cv2.THRESH_BINARY_INV)
	else:
		mask = cv2.adaptiveThreshold(output, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)

	return mask

# Tests sketch function operation
def test(image):
	image = cv2.imread('../test.png')
	cv2.imshow('Test ', sketch(image, thresh=1))
	cv2.waitKey(0)

def main():
	# Initializes the webcam
	vc = cv2.VideoCapture(0)

	# This is the main loop as we need to 
	# render multiple frames per second
	while True:
		ret, frame = vc.read()
		cv2.imshow('Live Sketch ', sketch(frame))

		# Leave the main loop if key 13 (ENTER) is pressed
		if(cv2.waitKey(1) == 13):
			break

	# Tests sketch function
	# test(cv2.imread('../test.png'))

	# Release the camera buffer and close all windows
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()