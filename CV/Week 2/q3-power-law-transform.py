"""
Implement power law transform s = c.r^Y

where,
    s -> output image
    r -> input image
    Y -> gamma
    c -> constant

https://theailearner.com/2019/01/26/power-law-gamma-transformations/
"""

import cv2 as cv
import numpy as np

img = cv.imread('roger.jpg')
img = cv.resize(img, (500, 800))

c = 255
gamma = 2.2
gamma22 = np.array(c * (img / 255) ** gamma, dtype=np.uint8)
gamma = 0.4
gamma04 = np.array(c * (img / 255) ** gamma, dtype=np.uint8)

res = cv.hconcat([img, gamma22, gamma04])

cv.imshow('Display result', res)
cv.waitKey(0)
