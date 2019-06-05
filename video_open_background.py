import numpy as np
import cv2


captura = cv2.VideoCapture(0)
#captura = cv2.VideoCapture("video.mp4")
mog = cv2.createBackgroundSubtractorMOG2(history=2000, varThreshold=16, detectShadows=True)

while(1):
	ret, frame = captura.read()
	img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	fgmask = mog.apply(img)
	
	cv2.imshow("Original", frame)
	cv2.imshow("Brackground", fgmask)
	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
		
captura.release
cv2.destroyAllWindows()
