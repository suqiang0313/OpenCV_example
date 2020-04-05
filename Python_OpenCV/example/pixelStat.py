import cv2 as cv 
import numpy as np 
src = cv.imread("Adela.jpeg")
src = cv.resize(src,(500,800))
gray = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
min,max,minLoc,maxLoc = cv.minMaxLoc(gray)
print ("min:%.2f,max:%.2f,"%(min,max))
print ("min loc:",minLoc)
print ("max loc:",maxLoc)
means, stddev = cv.meanStdDev(gray)
src[np.where(gray<means)] = 0 
src[np.where(gray>means)] = 255
cv.imshow("binary",src)
cv.waitKey(0)