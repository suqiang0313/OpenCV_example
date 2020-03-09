//demo : OpenCV cvtColor
//
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
using namespace cv;
using namespace std;

int main() {
    string url = "/Users/suqiang/myproject/opencv/OpenCV_example/example/img/Lena.jpg";
    Mat src = imread(url,IMREAD_COLOR);

    if (src.empty()) {
        printf("could not load image...\n");
        return -1;
    }
    namedWindow("input", CV_WINDOW_AUTOSIZE);
    imshow("input", src);
    Mat hsv;
    cvtColor(src,hsv,COLOR_BGR2HSV);// COLOR_GRAY2BGR,COLOR_BGR2HSV,COLOR_HSV2BGR
    imshow("hsv color",hsv);
    waitKey(0);
    return 0;
}
