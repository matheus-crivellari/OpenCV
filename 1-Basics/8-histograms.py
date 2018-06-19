import sys
sys.path.append('C:\\Python27\\Lib\\site-packages')

import cv2
import numpy as np

# Import matplotlib in order to plot histograms
from matplotlib import pyplot as plt

image = cv2.imread('./../test.png')

# Calculates the actual histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plots a histogram, ravel() faltens our image array (converst to a single dimension array)
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# View separate color channels
color = ('b', 'g', 'r')

# Separates the colors and print each one in the histogram
for i, col in enumerate(color):
	histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
	plt.plot(histogram2, color = col)
	plt.xlim([0, 256])

plt.show()