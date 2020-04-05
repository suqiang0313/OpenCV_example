import numpy as np 
import cv2 as cv 
print (cv.__version__)
src = cv.imread("Lena.jpg")
cv.imshow('src',src)
dst = cv.flip(src,0)
cv.imshow('x',dst)
dst = cv.flip(src,1)
cv.imshow('y',dst)
dst = cv.flip(src,-1)
cv.imshow('xy',dst)
cv.waitKey(0)
