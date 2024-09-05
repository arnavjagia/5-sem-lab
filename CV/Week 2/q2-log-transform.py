"""
Implement log transform s = c log(1 + r)

where,
    s -> output image
    r -> input image
    c -> constant

https://www.slideshare.net/slideshow/log-transformation-in-image-processing-with-example/168718438#6
https://medium.com/alphavision/image-enhancement-46f4b7fda5b4
"""

import cv2 as cv
import numpy as np

img = cv.imread('roger.jpg')
img = cv.resize(img, (600, 800))

# convert to float32
img = np.array(img, dtype=np.float32)
# compute value of c
c = 255 / np.log(1 + np.max(img))
# apply the transform
s = c * np.log(1 + img)
# convert back to int
s = np.array(s, dtype=np.uint8)

cv.imshow(f"inverted image for c = {c}", s)
cv.waitKey(0)
