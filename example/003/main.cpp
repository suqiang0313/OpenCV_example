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
    Mat gray;
    cvtColor(src,gray,COLOR_BGR2GRAY);
    imshow("gray color",gray);
    waitKey(0);
    return 0;
}
