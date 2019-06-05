import numpy as np
import cv2

img = cv2.imread("lena.jpeg", cv2.IMREAD_UNCHANGED)



res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR
height, width = img.shape[:2]


print img.shape

#res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)



cv2.imshow("Original", img)
cv2.imshow("Scaled", res)
cv2.waitKey(0)

cv2.destroyAllWindows()
