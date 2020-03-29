import cv2 as cv
src = cv.imread("../../CPP_OpenCV/img/Lena.jpg")
h,w,ch = src.shape
print("h,w,chr",h,w,ch)
for row in range(h):
    for col in range(w):
        b,g,r = src[row,col]
        b = 255 - b
        g = 255 - g
        r = 255 - r 
        src[row,col] = [b,g,r]
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
