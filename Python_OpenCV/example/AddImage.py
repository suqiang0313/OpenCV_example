import cv2 as cv
import numpy as np 
src1 = cv.imread("../../CPP_OpenCV/img/Lena.jpg")
src2 = cv.imread("Lena.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
#cv.imshow("input image", src1)
#cv.imshow("inout image", src2)
add_result = src1 + src2
cv.imshow("add_result",add_result)
cv.add(src1,src2,add_result)
cv.imshow("sub",add_result)
sub_result = np.zeros(src1.shape)
cv.subtract(src1,src2,sub_result)
cv.imshow("sub_result",sub_result)
cv.waitKey(0)
cv.destroyAllWindows()
