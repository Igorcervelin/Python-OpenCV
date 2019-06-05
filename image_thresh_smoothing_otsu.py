import numpy as np
import cv2



img = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)		#carrega imagem
ret,otsu_ant = cv2.threshold(img,0,255,cv2.THRESH_OTSU) #threshold otsu sobre imagem original

median = cv2.blur(img,(5,5))	#suavizacao com media
ret,otsu_med = cv2.threshold(median,0,255,cv2.THRESH_OTSU)	#otsu sobre imagem suavizada

gaussian = cv2.GaussianBlur(img,(5,5),0)	#suavizacao com gaussian
ret,otsu_gaussian = cv2.threshold(gaussian,0,255,cv2.THRESH_OTSU)	#otsu sobre imagem suavizada com gaussian


edges = cv2.Canny(gaussian,50,200) #detecta bordas sobre imagem suavizada com o gaussian


cv2.imshow("Original", img)
cv2.imshow("Otsu Ant", otsu_ant)
cv2.imshow("Otsu Median", otsu_med)
cv2.imshow("Otsu Gaussian", otsu_gaussian)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
