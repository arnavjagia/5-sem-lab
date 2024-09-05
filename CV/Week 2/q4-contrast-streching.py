"""
Implement contrast stretching

https://samirkhanal35.medium.com/contrast-stretching-f25e7c4e8e33
https://theailearner.com/2019/01/30/contrast-stretching/
"""

import cv2 as cv
import numpy as np
from utils import plot_images

img = cv.imread('roger.jpg', 0)  # Load the image in grayscale
img = cv.resize(img, (600, 800))  # Resize the image

# Convert to float32 for accurate division and multiplication
img_float = img.astype(np.float32)

# Calculate the global minimum and maximum pixel values
min_val = np.min(img_float)
max_val = np.max(img_float)

# Apply the Min-Max formula using vectorized computation
minmax_img = 255 * (img_float - min_val) / (max_val - min_val)

# Convert the stretched image back to uint8
minmax_img_uint8 = minmax_img.astype(np.uint8)

# Display the stretched image
plot_images(img, 'original', minmax_img_uint8, 'contrast stretched')