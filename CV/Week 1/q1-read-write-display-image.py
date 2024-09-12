"""
cv.imread() -> returns ndarray or None
that ndarray contains (num_rows, num_cols, num_channels) if the image is colored
and (num_rows, num_cols) if the image is grayscale
"""

# import the cv2 library
import cv2 as cv

base = "Week 1"

# The function cv2.imread() is used to read an image.
img_grayscale = cv.imread(f'{base}/roger.jpg', 0)

# The function cv2.resize() is used to resize an image.
img_grayscale = cv.resize(img_grayscale, (600, 800))

# The function cv2.imshow() is used to display an image in a window.
cv.imshow('grayscale image', img_grayscale)

# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv.destroyAllWindows()

# The function cv2.imwrite() is used to write an image.
cv.imwrite('grayscale.jpg', img_grayscale)