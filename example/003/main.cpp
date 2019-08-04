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
    Mat m1 = src.clone();
    Mat m2;
    src.copyTo(m2);
    // m3 and src have same address
    Mat m3 = src;
    Mat m4 = Mat::zeros(src.size(),src.type());
    cout << m4.size()<<endl;
    // new Mat with zeros
    Mat m5 = Mat::zeros(Size(512,512),CV_8UC3);
    // new Mat with ones
    Mat m6 = Mat::ones(Size(512,512),CV_8UC3);
//    imshow("zeros",255);
    // new kernel
    Mat kernel = (Mat_<char>(3, 3) << 0, -1, 0,
        -1, 5, -1,
        0, -1, 0);
    waitKey(0);
    return 0;
}
