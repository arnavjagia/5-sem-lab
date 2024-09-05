"""
Implement Canny Edge Detection
"""

import cv2 as cv
import numpy as np

scale = 0.8
blur_sigma = 1.8

img = cv.imread("Week 5/roger.jpg")
img = cv.resize(img, (600, 800))

w = int(scale * img.shape[1])
h = int(scale * img.shape[0])
img = cv.resize(img, (w, h), cv.INTER_LINEAR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gaussian_blurred = cv.GaussianBlur(gray, (-1, -1), sigmaX=blur_sigma, sigmaY=blur_sigma)

sobelx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
sobely = sobelx.T

gx = cv.filter2D(gaussian_blurred, -1, sobelx)
gy = cv.filter2D(gaussian_blurred, -1, sobely)
gm = np.sqrt(gx**2 + gy**2).astype(img.dtype)
grad_angles = np.arctan2(gy, gx)

# Nonmaxsuppression
# for every pixel, if grad dir same as neighbour, and this pixel is not max in that dir, make 0.
def non_max_suppression(gradient_magnitude, gradient_direction):
    # Initialize output image
    output = np.zeros_like(gradient_magnitude, dtype=np.float32)
    print(gradient_magnitude.shape)
    height, width = gradient_magnitude.shape
    angle = gradient_direction * 180.0 / np.pi
    angle[angle < 0] += 180

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Get angle of the gradient
            current_angle = angle[i, j]
            # Determine neighbors based on angle
            if (0 <= current_angle < 22.5) or (157.5 <= current_angle <= 180):
                q = gradient_magnitude[i, j + 1]
                r = gradient_magnitude[i, j - 1]
            elif 22.5 <= current_angle < 67.5:
                q = gradient_magnitude[i + 1, j - 1]
                r = gradient_magnitude[i - 1, j + 1]
            elif 67.5 <= current_angle < 112.5:
                q = gradient_magnitude[i + 1, j]
                r = gradient_magnitude[i - 1, j]
            elif 112.5 <= current_angle < 157.5:
                q = gradient_magnitude[i - 1, j - 1]
                r = gradient_magnitude[i + 1, j + 1]

            # Suppression
            if gradient_magnitude[i, j] >= q and gradient_magnitude[i, j] >= r:
                output[i, j] = gradient_magnitude[i, j]

    return output


def double_threshold(image, low_threshold, high_threshold):
    high_threshold = np.max(image) * high_threshold
    low_threshold = high_threshold * low_threshold

    strong_edges = image >= high_threshold
    weak_edges = (image >= low_threshold) & (image < high_threshold)

    output = np.zeros_like(image, dtype=np.uint8)
    output[strong_edges] = 255
    output[weak_edges] = 75

    return output


def edge_tracking_by_hysteresis(image):
    height, width = image.shape
    strong_edges = image == 255
    weak_edges = image == 75

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if weak_edges[i, j]:
                if np.any(strong_edges[i - 1 : i + 2, j - 1 : j + 2]):
                    image[i, j] = 255
                else:
                    image[i, j] = 0

    return image


nms_image = non_max_suppression(gm, grad_angles)
thresholded_image = double_threshold(nms_image, 0.9999, 1)
final_edges = edge_tracking_by_hysteresis(thresholded_image)


low_threshold = 100
high_threshold = 200
edges = cv.Canny(gaussian_blurred, low_threshold, high_threshold)

res = cv.hconcat([gray, edges, final_edges])
cv.imshow("win", res)
cv.waitKey(0)
cv.destroyAllWindows()
