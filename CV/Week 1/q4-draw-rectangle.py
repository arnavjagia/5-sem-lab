import cv2 as cv

base = "Week 1"

img = cv.imread(f"{base}/roger.jpg")
img = cv.resize(img, (600, 800))
cv.rectangle(img, (0, 0), (600, 800), color=(0, 255, 0), thickness=3)
cv.imshow("Rect image", img)
cv.waitKey(0)
