import cv2 as cv
import numpy as np 
src = cv.imread("Lena.jpg")
h,w = src.shape[:2]
m1 = np.copy(src)
m2 = src
src[100:200,200:300,:] = 0
cv.imshow("lena",src)
m3 = np.zeros(src.shape,src.dtype)
cv.imshow("m3",m3)
m4 = np.zeros([512,512],np.uint8)
cv.imshow("m4",m4)
m5 = np.ones([256,256,3],np.uint8)
m5[:,:,0] = 255
cv.imshow("m5",m5)
cv.waitKey(0)
cv.destroyAllWindows()
