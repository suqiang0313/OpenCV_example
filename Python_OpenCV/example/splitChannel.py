import cv2 as cv
import numpy as np 
src = cv.imread("../../CPP_OpenCV/img/Lena.jpg")
dst = np.zeros(src.shape, dtype=np.uint8)
mv = cv.split(src)
mv[0][:,:] = 0
mv[1][:,:] = 0
mv[2][:,:] = 0
merged = cv.merge(mv)
cv.imshow("merged",merged)
cv.mixChannels([src],[dst],[0,0,1,1,2,2])
cv.imshow("mixChannel",dst)
cv.waitKey(0)


