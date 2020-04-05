# extract color channel
import cv2 as cv
import numpy as np 
src = cv.imread("Adela.jpeg")
src = cv.resize(src,(500,500))
cv.imshow("lena",src)
gray = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
cv.imshow("gray",gray)
hsv = cv.cvtColor(src,cv.COLOR_RGB2HSV)
cv.imshow("hsv",hsv)
yuv  = cv.cvtColor(src,cv.COLOR_RGB2YUV)
cv.imshow("yuv",yuv)
YCrCb = cv.cvtColor(src,cv.COLOR_BGR2YCrCb)
cv.imshow("YCrCb",YCrCb)
src2 = cv.imread("tina_green.png")
cv.imshow("src2",src2)
hsv = cv.cvtColor(src2,cv.COLOR_RGB2HSV)
mask = cv.inRange(hsv,(35,43,46),(77,255,255))
dst = np.zeros(src2.shape)
dst = cv.bitwise_and(src2,src2,dst,mask=mask)
cv.imshow("dst",dst)
cv.waitKey(0)

