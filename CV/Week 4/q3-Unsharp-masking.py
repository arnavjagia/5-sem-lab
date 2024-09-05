import cv2 as cv
import numpy as np
from utils import plot_images

image = cv.imread("roger.jpg", 0)

k = 0.15
mask = image - cv.GaussianBlur(image, (11, 11), 0)
unsharped = image + k * mask

plot_images(image, 'original', mask, 'mask', unsharped, 'output')