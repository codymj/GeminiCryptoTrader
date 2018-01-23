################################################################################
#
#  MainWindow.py
#  Author: Cody Johnson <codyj@protonmail.com>
#
################################################################################

import sys
from PyQt5 import QtGui, QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWindow.ui', self)
        self.show()
