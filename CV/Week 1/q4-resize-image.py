import cv2 as cv

base = "Week 1"

img = cv.imread(f'{base}/roger.jpg')
img = cv.resize(img, (600, 800))
cv.imshow('Resized image', img)
cv.waitKey(0)
