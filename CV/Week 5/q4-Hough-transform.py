"""
Hough Transform
"""

import cv2 as cv
import numpy as np
from utils import plot_images

base = "Week 5"

image = cv.imread(f"{base}/road.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# get edges on applying Canny edge
edges = cv.Canny(gray, 50, 150, apertureSize=3)
lines = cv.HoughLinesP(
    edges, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=10
)  # Hough Transform

# Draw if lines are detected
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

plot_images(image, "Hough transform")
