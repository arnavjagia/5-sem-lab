"""
Color segmentation
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from utils import plot_images

image = cv.imread("Week 5/roger.jpg")
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Convert BGR to RGB for displaying
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # Convert BGR to HSV for color segmentation

# Setting bounds to segment green color
lower_bound = np.array([35, 100, 100])  # Lower bound of HSV range
upper_bound = np.array([85, 255, 255])  # Upper bound of HSV range

mask = cv.inRange(image_hsv, lower_bound, upper_bound)  # Binary mask where only green portion is white
segmented_image = cv.bitwise_and(image, image, mask=mask)  # Apply mask

# Convert images for displaying with matplotlib
mask_rgb = cv.cvtColor(mask, cv.COLOR_GRAY2RGB)
segmented_image_rgb = cv.cvtColor(segmented_image, cv.COLOR_BGR2RGB)

plot_images(image_rgb, 'Original Image', mask_rgb, 'Mask', segmented_image_rgb, 'Segmented Image')  # Display
