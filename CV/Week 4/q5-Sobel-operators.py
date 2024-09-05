import cv2 as cv
import numpy as np

from utils import plot_images

image = cv.imread("roger.jpg", 0)

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

grad_x = cv.filter2D(image, ddepth=cv.CV_32F, kernel=sobel_x)
grad_y = cv.filter2D(image, ddepth=cv.CV_32F, kernel=sobel_y)

grad = abs(grad_x) + abs(grad_y)

plot_images(image, 'orginal', grad, "sobel edges")
