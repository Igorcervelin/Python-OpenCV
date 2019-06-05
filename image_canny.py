import numpy as np
import cv2

img = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img,100,200)

cv2.imshow("Original", img)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
