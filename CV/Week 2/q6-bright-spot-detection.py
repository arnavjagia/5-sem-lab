"""
Bright spot detection
"""

# import cv2 as cv
# import numpy as np

# img = cv.imread('roger.jpg')
# img = cv.resize(img, (600, 800))

# # Convert to grayscale
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Now use cv.minMaxLoc on the grayscale image
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gray_img)

# radius = 20
# color = (255, 255, 255)  # Circle color
# thickness = 2  # Circle thickness
# cv.circle(img, max_loc, radius, color, thickness)  # Draw circle on the original image

# cv.imshow('Display result', img)
# cv.waitKey(0)


import cv2 as cv
import numpy as np

# Load and resize image
img = cv.imread('roger.jpg')
img = cv.resize(img, (600, 800))

# Convert to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Find the maximum pixel value
max_val = np.max(gray_img)

# Find the location of the maximum pixel value using basic NumPy operations
# This will give a tuple of arrays representing the indices where the max value occurs
max_loc = np.where(gray_img == max_val)

# Get the first occurrence of the max value
print(max_loc)
max_loc = (int(max_loc[1][0]), int(max_loc[0][0]))
print(max_loc)

# Draw a circle at the brightest spot
radius = 20
color = (255, 255, 255)  # White circle
thickness = 2  # Circle thickness
cv.circle(img, max_loc, radius, color, thickness)  # Draw circle on the original image

# Display the result
cv.imshow('Display result', img)
cv.waitKey(0)
cv.destroyAllWindows()