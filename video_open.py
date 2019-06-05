import numpy as np
import cv2













captura = cv2.VideoCapture(0)
#captura = cv2.VideoCapture("video.mp4")

while(1):
	ret, frame = captura.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	edges = cv2.Canny(gray,50,200)
	
	cv2.imshow("Original", frame)
	cv2.imshow("Grayscale", edges)
	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
		
captura.release
cv2.destroyAllWindows()
