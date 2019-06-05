import numpy as np
import cv2


# cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv.IMREAD_UNCHANGED : Loads image as such including alpha channel




img = cv2.imread("opencv_1.jpg", cv2.IMREAD_UNCHANGED)

blur_average = cv2.blur(img,(5,5))
blur_gaussian = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("Original", img)
cv2.imshow("Average", blur_average)
cv2.imshow("Gaussian", blur_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
