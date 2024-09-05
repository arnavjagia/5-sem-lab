import cv2 as cv
# https://sharmaji27.medium.com/how-to-generate-a-negative-image-in-python-using-opencv-interesting-project-439da0c19544

img = cv.imread('roger.jpg', 0)
img = cv.resize(img, (600, 800))

negative_img = abs(255 - img)
cv.imshow('Negative image', negative_img)

# cv.imshow('Display', img)
cv.waitKey(0)
