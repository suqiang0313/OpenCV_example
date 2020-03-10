import cv2 as cv
import numpy as np 

def access_pixels(img):
    print (img.shape)
    height = img.shape[0]
    width = img.shape[1]
    channel = img.shape[2]

    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = img[row][col][c]
                img[row][col][c] = 255 - pv
    cv.imshow('converted_lena',img)


def create_img():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400]) * 255
    cv.imshow('create_img',img)






src = cv.imread("../../CPP_OpenCV/img/Lena.jpg")
img = src
#access_pixels(img)
create_img()
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
