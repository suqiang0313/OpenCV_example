import cv2

def bi_demo(image): 
    dst = cv2.bilateralFilter(src=image, d=0, sigmaColor=50, sigmaSpace=15)
    cv2.namedWindow('bi_demo', 0)
    cv2.resizeWindow('bi_demo', 300, 400)
    cv2.imshow("bi_demo", dst)

def mean_shift_demo(image):  
    dst = cv2.pyrMeanShiftFiltering(src=image, sp=15, sr=20)
    cv2.namedWindow('mean_shift image', 0)
    cv2.resizeWindow('mean_shift image', 300, 400)
    cv2.imshow("mean_shift image", dst)


src = cv2.imread('tina_green.png')
src = cv2.resize(src,(500,500))
bi_demo(src)
#mean_shift_demo(src)
cv2.namedWindow('src', 0)
cv2.resizeWindow('src', 300, 400)
cv2.imshow('src', src)
cv2.waitKey(0)
