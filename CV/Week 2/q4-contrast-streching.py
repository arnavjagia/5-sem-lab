"""
Implement contrast stretching

https://samirkhanal35.medium.com/contrast-stretching-f25e7c4e8e33
https://theailearner.com/2019/01/30/contrast-stretching/
"""

import cv2 as cv
import numpy as np

img = cv.imread('roger.jpg')
img = cv.resize(img, (600, 800))

img = np.array(img, dtype=np.float32)
min_val = np.min(img)
max_val = np.max(img)

if min_val != max_val:
    res = 255 * ((img - min_val) / (max_val - min_val))
else:
    res = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)

res = np.array(res, dtype=np.uint8)
img = np.array(img, dtype=np.uint8)

cv.imshow('Display result', cv.hconcat([img, res]))
cv.waitKey(0)
