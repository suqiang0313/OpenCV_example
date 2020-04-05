import numpy as np 
import cv2 as cv 
src = cv.imread('Lena.jpg')
gray = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
print (gray)
#scale and shift by NORM_MINMAX
dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst = dst,alpha=0,beta=1.0,norm_type=cv.NORM_MINMAX)
print(dst)
cv.imshow("NORMAL_MINMAX",np.uint8(dst*255))
#sacle and shift by NORM_INF
dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst = dst,alpha = 1.0,beta = 0,norm_type=cv.NORM_INF)
print (dst)
cv.imshow("NORM_INF",np.uint8(dst*255))
cv.waitKey(0)

