"""
Implement power law transform s = c.r^Y

where,
    s -> output image
    r -> input image
    Y -> gamma
    c -> constant
"""

import cv2 as cv
import numpy as np

img = cv.imread('roger.jpg')
img = cv.resize(img, (600, 800))

# Convert to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Now use cv.minMaxLoc on the grayscale image
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gray_img)

radius = 20
color = (255, 255, 255)  # Circle color
thickness = 2  # Circle thickness
cv.circle(img, max_loc, radius, color, thickness)  # Draw circle on the original image

cv.imshow('Display result', img)
cv.waitKey(0)
