import cv2 as cv
import numpy as np
from utils import plot_images

image = cv.imread("roger.jpg", 0)

box_filtered = cv.blur(image, (51, 51))
gaussian = cv.GaussianBlur(image, (51, 51), 0)

plot_images(image, 'original', box_filtered, 'box filtered', gaussian, 'gaussian')