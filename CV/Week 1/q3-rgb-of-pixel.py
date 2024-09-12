import cv2 as cv
import numpy as np

base = "Week 1"

img = cv.imread(f"{base}/roger.jpg")
img = cv.resize(img, (600, 800))

b, g, r = cv.split(img)
zeros = np.zeros(b.shape, np.uint8)
img_red = cv.merge((zeros, zeros, r))
img_green = cv.merge((zeros, g, zeros))
img_blue = cv.merge((b, zeros, zeros))

img_red = img.copy()
img_green = img.copy()
img_blue = img.copy()
img_red[:, :, (0, 1)] = 0
img_green[:, :, (0, 2)] = 0
img_blue[:, :, (1, 2)] = 0

cv.imshow("Red image", img_red)
cv.waitKey(0)
cv.imshow("Green image", img_green)
cv.waitKey(0)
cv.imshow("Blue show", img_blue)
cv.waitKey(0)

"""
# imread returns a 3 dim ndarray with BGR channels
# First you can access BGR channel , it is 0-indexed array
# Then you can access the pixel which contains BGR of the channel selected 
print(img[0])
print(img[0][0])
print(img[0][0][1])
print(img.shape)
"""
