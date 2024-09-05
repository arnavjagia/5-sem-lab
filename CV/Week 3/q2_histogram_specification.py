"""
Q2. Write a program to read an input image, reference image, and perform histogram specification.

https://www.youtube.com/watch?v=fZn0dSkS28I

Histogram Matching
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from utils import plot_with_histogram

image = cv.imread('roger.jpg', 0)
image = cv.resize(image, (600, 800))

def equalisation(img):
    """Returns the T in s = T[r]."""
    hist, bins = np.histogram(img, 256, (0, 256))
    cdf = hist.cumsum()
    T = 255 * cdf / cdf[-1]
    return T.astype(np.uint8)

def match_histograms(src, ref):
    T = equalisation(src)
    G = equalisation(ref)
    return np.interp(T[src], G, range(256))

road = cv.imread("road.jpg", 0)
eqz = match_histograms(src=road, ref=image)
plot_with_histogram(road, "original", image, "reference", eqz, "matched")
