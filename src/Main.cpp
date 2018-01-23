/*******************************************************************************
 *
 * Main.cpp
 * Author:  Cody Johnson <codyj@protonmail.com>
 *
 ******************************************************************************/

#include <QtWidgets/QApplication>
#include "MainWindow.h"

int main(int argc, char *argv[]) {

    QApplication app(argc, argv);

    MainWindow mainWin;
    mainWin.show();

    return app.exec();
}
