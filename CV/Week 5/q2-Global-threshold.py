"""
Global Thresholding
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Read and resize the image
img = cv.imread("Week 5/roger.jpg", 0)
img = cv.resize(img, (600, 800))
orig = img.copy()  # Create a copy for displaying the original image

# Calculate the histogram
histg_c = cv.calcHist([img], [0], None, [256], [0, 256])


def global_thresholding(histg_c, starting_thres):
    print("Starting threshold: ", starting_thres)

    # Flatten histogram
    histg_c = histg_c.flatten()

    # Compute class sums and counts
    below_threshold_count = np.sum(histg_c[:starting_thres])
    above_threshold_count = np.sum(histg_c[starting_thres:])

    # Avoid division by zero
    if below_threshold_count == 0 or above_threshold_count == 0:
        print("No pixels in one of the classes.")
        return starting_thres

    below_threshold_sum = np.sum(np.arange(starting_thres) * histg_c[:starting_thres])
    above_threshold_sum = np.sum(
        np.arange(starting_thres, 256) * histg_c[starting_thres:]
    )

    # Calculate means
    m1 = below_threshold_sum / below_threshold_count
    m2 = above_threshold_sum / above_threshold_count

    print("m1, m2: ", m1, m2)

    # Calculate new threshold
    new_t = int((m1 + m2) / 2)
    print("New threshold: ", new_t)

    if abs(new_t - starting_thres) < 10:
        print("No updates required.")
        return new_t
    else:
        return global_thresholding(
            histg_c, new_t
        )  # Return the result of the recursive call


# Initialize the thresholding
initial_threshold = 50
final_T = global_thresholding(histg_c, initial_threshold)

print("Final threshold:", final_T)

# Apply thresholding to the image
thresholded_img = np.where(img < final_T, 0, img)  # Use np.where for efficiency

# Plot the original and thresholded images
fig, axs = plt.subplots(1, 2, figsize=(10, 8))

axs[0].imshow(orig, cmap="gray")
axs[0].set_title("Original Image")
axs[0].axis("off")

axs[1].imshow(thresholded_img, cmap="gray")
axs[1].set_title("Thresholded Image")
axs[1].axis("off")

plt.tight_layout()
plt.show()
