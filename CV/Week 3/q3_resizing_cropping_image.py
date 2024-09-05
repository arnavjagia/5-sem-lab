import cv2 as cv
from utils import plot_images


image = cv.imread('roger.jpg', 1)
image = cv.resize(image, (600, 800))

cropped = image[200: 600, 150: 450]  # cropping the image
resized = cv.resize(image, (225, 200))  # resizing the image

plot_images(image, "original", cropped, "cropped", resized, "resized")