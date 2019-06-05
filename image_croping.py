import cv2
import numpy as np

img = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape



y = 10		#origem de inicio do corte na altura
h = 200		#tamanho do corte de altura
x = 20		#origem do corte na largura
w = 100		#tamanho do corte da largura

dst = img[y:y+h, x:x+w]

cv2.imshow("Original", img)
cv2.imshow("Cropped", dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
