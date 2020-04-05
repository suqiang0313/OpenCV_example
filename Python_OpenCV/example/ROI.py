import cv2 as cv
import numpy as np 
src2 = cv.imread("tina_green.png")
cv.imshow("src2", src2)
hsv = cv.cvtColor(src2, cv.COLOR_RGB2HSV)
mask = cv.inRange(hsv, (35, 43, 46), (77, 255, 255))
mask = cv.bitwise_not(mask)
person = np.zeros(src2.shape)
person = cv.bitwise_and(src2, src2, person, mask=mask)
cv.imshow('person',person)
result = np.zeros(src2.shape,src2.dtype)
result[:,:,0] = 255
mask = cv.bitwise_not(mask)
dst = cv.bitwise_or(person,result,mask=mask)
dst = cv.add(dst,person)
cv.imshow('dst',dst)
cv.waitKey(0)