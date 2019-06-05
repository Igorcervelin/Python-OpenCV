import numpy as np
import cv2

img = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)

rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Original", img)
cv2.imshow("Result", dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
