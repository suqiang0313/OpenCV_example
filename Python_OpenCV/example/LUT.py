import cv2 as cv
src = cv.imread("../../CPP_OpenCV/img/Lena.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
dst = cv.applyColorMap(src,cv.COLORMAP_AUTUMN)
cv.imshow("output image",dst)
cv.waitKey(0)
cv.destroyAllWindows()
