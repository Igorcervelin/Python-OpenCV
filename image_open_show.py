# -*- coding: utf-8 -*-

import numpy as np
import cv2

# cv.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv.IMREAD_UNCHANGED : Loads image as such including alpha channel







try:
	img = cv2.imread("lena.jpeg", cv2.IMREAD_UNCHANGED)
	cv2.imshow("image", img)
except:
	print ("Não foi possivel abrir imagem!")

	
cv2.waitKey(0)
cv2.destroyAllWindows()
