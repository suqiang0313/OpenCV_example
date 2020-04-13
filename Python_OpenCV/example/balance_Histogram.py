import cv2 as cv 
import numpy as np 
def equal_histogram(image):
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("global_equal_histogram",dst)


def clahe_equal_histogram(image):
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    clache =  cv.createCLAHE(clipLimit=5.0,tileGridSize=(3,3))
    dst = clache.apply(gray)
    cv.imshow('clahe_equal_histogram',dst)

src = cv.imread('rice.jpg')
cv.imshow('src',src)
equal_histogram(src)
clahe_equal_histogram(src)
cv.waitKey(0)


