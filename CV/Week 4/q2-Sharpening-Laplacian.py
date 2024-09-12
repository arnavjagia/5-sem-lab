import cv2 as cv
import numpy as np

from utils import plot_images

image = cv.imread("roger.jpg", 0)

kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
edges = cv.filter2D(image, -1, kernel)
sharpened = image + 10 * edges

plot_images(image, "original", sharpened, "sharpened", 10 * edges, "edges")
