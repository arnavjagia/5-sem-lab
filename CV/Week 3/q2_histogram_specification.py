"""
Q2. Write a program to read an input image, reference image, and perform histogram specification.

https://www.youtube.com/watch?v=fZn0dSkS28I

Histogram Matching
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('roger.jpg')
image = cv.resize(image, (600, 800))
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Calculate the histogram
hist, bins = np.histogram(image.flatten(), 256, (0, 256))
# Compute the cumulative distribution function
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Plot histogram and C.D.F.
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# Show the image in grayscale
axs[0].imshow(image_rgb, cmap="gray", vmin=0, vmax=255)
axs[0].axis("off")
# Plot the histogram and the CDF
axs[1].plot(cdf_normalized, color="black", linestyle="--", linewidth=1)
axs[1].hist(image.flatten(), 256, [0, 256], color="r", alpha=0.5)
axs[1].set_xlim([0, 256])
axs[1].legend(("CDF", "Histogram"), loc="upper left")
plt.show()
