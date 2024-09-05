"""
Color segmentation
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread("Week 5/roger.jpg")
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Convert BGR to RGB for displaying

# Convert the image from BGR to HSV color space
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Segmenting a specific shade of green
lower_bound = np.array([35, 100, 100])  # Lower bound of HSV range
upper_bound = np.array([85, 255, 255])  # Upper bound of HSV range

# Create a binary mask where the specified color range is white and everything else is black
mask = cv.inRange(image_hsv, lower_bound, upper_bound)

# Apply the mask to the original image
segmented_image = cv.bitwise_and(image, image, mask=mask)

# Convert images for displaying with matplotlib
mask_rgb = cv.cvtColor(mask, cv.COLOR_GRAY2RGB)
segmented_image_rgb = cv.cvtColor(segmented_image, cv.COLOR_BGR2RGB)

# Display the results
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(image_rgb)
axs[0].set_title("Original Image")
axs[0].axis("off")

axs[1].imshow(mask_rgb)
axs[1].set_title("Mask")
axs[1].axis("off")

axs[2].imshow(segmented_image_rgb)
axs[2].set_title("Segmented Image")
axs[2].axis("off")

plt.tight_layout()
plt.show()
