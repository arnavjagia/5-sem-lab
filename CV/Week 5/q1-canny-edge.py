"""
Implement Canny Edge Detection

"""

import cv2 as cv

image = cv.imread('roger.jpg', 0)
image = cv.resize(image, (600, 800))
cv.imshow('Display', image)
cv.waitKey(0)

