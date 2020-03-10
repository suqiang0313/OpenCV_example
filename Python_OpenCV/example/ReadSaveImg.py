import cv2 as cv
import numpy as np 

def get_image_info(image):
    print (type(image))
    print (image.shape)
    print (image.size)
    print (image.dtype)
    pixel_data = np.array(image)
    print (pixel_data)
    cv.imwrite('lena.png',image)
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    cv.imwrite('lena_gray.png',gray)

def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame,1)
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            break


src = cv.imread("../../CPP_OpenCV/img/Lena.jpg")
get_image_info(src)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()
