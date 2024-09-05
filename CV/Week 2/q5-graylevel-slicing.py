"""
Implement gray level slicing

All transforms blog: https://www.dynamsoft.com/blog/insights/image-processing/image-processing-101-point-operations/
https://in.mathworks.com/matlabcentral/answers/240232-why-grey-level-slicing-image-with-background-is-not-showing-any-image-in-this-code
https://medium.com/@koushikc2000/basic-operations-on-images-using-opencv-python-cb0d60d11911
"""

import cv2 as cv
import numpy as np
from utils import plot_images

img = cv.imread("roger.jpg", 0)
img = cv.resize(img, (600, 800))

minPixel = 100
maxPixel = 200

mask = (img >= minPixel) & (img <= maxPixel)  # Create a mask for pixels within the specified range
res = np.zeros(img.shape, dtype=np.uint8)  # Initialize a result image with zeros (black)

res[mask] = img[mask]  # Apply the mask to the original image, highlighting the range

plot_images(img, "Original image", res, "Gray level slicing")
