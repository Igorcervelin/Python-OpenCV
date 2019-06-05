import numpy as np
import cv2

captura = cv2.VideoCapture(0)
#captura = cv2.VideoCapture("video.mp4")
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 25., (640,480))	#Arquivo para saida do video a ser gravado
while(1):
	ret, frame = captura.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	edges = cv2.Canny(gray,50,200)
	
	out.write(edges)	#escreve o frame no arquivo
	
	cv2.imshow("Original", frame)
	cv2.imshow("Grayscale", edges)
	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
		
captura.release
out.release
cv2.destroyAllWindows()
