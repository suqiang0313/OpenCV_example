#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<opencv2/opencv.hpp>
#include<QDir>
#include<iostream>
using namespace std;
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    cv::Mat inputImage = cv::imread("/Users/suqiang/myproject/opencv/test/test/1.jpg");
//    cv::Mat inputImage=cv::imread("1.jpg");

    if(!inputImage.empty())
            cv::imshow("Display Image", inputImage);

    else
    {
        std::cout<<"error"<<std::endl;
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}
