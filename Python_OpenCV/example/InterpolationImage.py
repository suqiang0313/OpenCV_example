#https://blog.csdn.net/wgx571859177/article/details/78963267
import numpy as np
import cv2 as cv
print (cv.__version__)
src = cv.imread("Lena.jpg")
h,w = src.shape[:2]
print (h,w)
img = cv.resize(src, (w/2, h/2),interpolation=cv.INTER_CUBIC)
linear_img = cv.resize(img,(w,h),interpolation=cv.INTER_LINEAR)
near_img = cv.resize(img,(w,h),interpolation=cv.INTER_NEAREST)
cub_img = cv.resize(img,(w,h),interpolation=cv.INTER_CUBIC)
cv.imshow("img",img)
cv.imshow('linear_img',linear_img)
cv.imshow('near_img',near_img)
cv.imshow('cub_img',cub_img)
cv.waitKey(0)