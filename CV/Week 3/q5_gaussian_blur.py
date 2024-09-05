import cv2 as cv

image = cv.imread('roger.jpg')
image = cv.resize(image, (600, 800))

kernel_size = (15, 15)
sigma = 0

blurred_image = cv.GaussianBlur(image, kernel_size, sigma)

res = cv.hconcat([image, blurred_image])
cv.imshow('Gaussian Blur Image', res)
cv.imwrite('blurred_image.jpg', blurred_image)
cv.waitKey(0)
