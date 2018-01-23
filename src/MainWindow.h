/*******************************************************************************
 *
 *  MainWindow.h
 *  Author: Cody Johnson <codyj@protonmail.com>
 *
 ******************************************************************************/

#ifndef _MAINWINDOW_H_
#define _MAINWINDOW_H_

#include "ui_MainWindow.h"

class MainWindow : public QMainWindow, public Ui::MainWindow {
    Q_OBJECT

public:
    MainWindow();
};

#endif  // _MAINWINDOW_H_
