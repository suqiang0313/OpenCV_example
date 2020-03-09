#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
using namespace cv;
using namespace std;

int main() {
    string url = "/Users/suqiang/myproject/opencv/OpenCV_example/example/img/Lena.jpg";
    Mat src = imread(url,IMREAD_COLOR);

    if (src.empty())
    {
        printf("could not load image...\n");
        return -1;
    }
    namedWindow("input", CV_WINDOW_AUTOSIZE);
    imshow("input", src);
    int  height = src.rows;
    int width = src.cols;
    int ch = src.channels();
    // read every pixel in image
    for(int row = 0;row < height; row++)
    {
        for(int col = 0;col < width; col++)
        {
            if(ch == 3)
            {
                Vec3b bgr = src.at<Vec3b>(row, col);
                bgr[0] = 255 - bgr[0];
                bgr[1] = 255 - bgr[1];
                bgr[2] = 255 - bgr[2];
                src.at<Vec3b>(row, col) = bgr;

            }
            if(ch ==1)
            {
                int gray = src.at<uchar>(row, col);
                src.at<uchar>(row, col) = 255 - gray;
            }

        }

    }
    imshow("output", src);
    //
    Mat result = Mat::zeros(src.size(), src.type());
    int blue = 0, green = 0, red = 0;
    int gray;

    for (int row = 0; row < height; row++) {
        uchar* curr_row = src.ptr<uchar>(row);
        uchar* result_row = result.ptr<uchar>(row);
        for (int col = 0; col < width; col++) {
            if (ch == 3) {
                blue = *curr_row++;
                green = *curr_row++;
                red = *curr_row++;

                *result_row++ = blue;
                *result_row++ = green;
                *result_row++ = red;
            }
            else if (ch == 1) {
                gray = *curr_row++;
                *result_row++ = gray;
            }
        }
    }

    imshow("result", result);

    waitKey(0);
    return 0;
}
