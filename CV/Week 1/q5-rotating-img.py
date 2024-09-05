import cv2 as cv

base = "Week 1"

img = cv.imread(f'{base}/roger.jpg')
img = cv.resize(img, (600, 800))
img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imshow('Rotated image', img)
cv.waitKey(0)
