import cv2 as cv
import numpy as np 
src = cv.imread("../../CPP_OpenCV/img/Lena.jpg")
h,w = src.shape[:2]
center = (w//2,h//2)
M = cv.getRotationMatrix2D(center,90,1)
src = cv.warpAffine(src, M, (w, h))
#cv.imwrite('Lena.jpg',src)
#cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("lena",src)
gray = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
cv.imshow("gray_lena",gray)
hsv = cv.cvtColor(src,cv.COLOR_RGB2HSV)
cv.imshow("hsv_lena",hsv)
cv.waitKey(0)
cv.destroyAllWindows()

