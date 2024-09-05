import cv2 as cv
import numpy as np

from utils import plot_images

image = cv.imread("roger.jpg", 0)

kernel_A = np.array([[0, 0, 0], [0, -1, 0], [0, 0, 1]])
A = cv.filter2D(image, kernel=kernel_A, ddepth=cv.CV_32F)

kernel_B = np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
B = cv.filter2D(image, kernel=kernel_B, ddepth=cv.CV_32F)

robert_edges = abs(A) + abs(B)

plot_images(image, 'original', robert_edges, 'roberts cross edges')