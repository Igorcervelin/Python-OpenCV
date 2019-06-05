import numpy as np
import cv2


# cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv.IMREAD_UNCHANGED : Loads image as such including alpha channel

img = cv2.imread("lena.jpeg", cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

cv2.destroyAllWindows()
