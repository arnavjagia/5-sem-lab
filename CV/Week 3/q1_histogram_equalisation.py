"""
Q1. Write a program to read an image and perform histogram equalization.

https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
https://en.wikipedia.org/wiki/Histogram_equalization

Adaptive HE
Histogram Matching
Smoothing/ Sharpening/ median/ max/ min
Gaussian blur
"""
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('roger.jpg', 0)
image = cv.resize(image, (600, 800))

eq = cv.equalizeHist(image)

hist1 = cv.calcHist([image], [0], None, [256], [0, 256])
hist2 = cv.calcHist([eq], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.axis("off")
plt.imshow(cv.cvtColor(image, cv.COLOR_GRAY2RGB))

plt.subplot(2, 2, 2)
plt.title("Original Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist1, label='Original Image', color='blue')
plt.legend(loc='upper left')
plt.xlim([0, 256])

plt.subplot(2, 2, 3)
plt.title("Equalized Image")
plt.axis("off")
plt.imshow(cv.cvtColor(eq, cv.COLOR_GRAY2RGB))

plt.subplot(2, 2, 4)
plt.title("Equalized Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist2, label='Equalized Image', color='red')
plt.legend()
plt.xlim([0, 256])

# Show the plot
plt.tight_layout()
plt.show()
