import cv2 as cv
import numpy as np
from utils import plot_images

image = cv.imread("roger.jpg", 0)

# Increase the kernel size for more blurring
# Manually set the sigma values for more control over the blurring effect
gaussian = cv.GaussianBlur(image, (31, 31), 10)  # Using a larger kernel size

plot_images(image, "Original", gaussian, "Gaussian blur")