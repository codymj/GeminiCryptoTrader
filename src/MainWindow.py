################################################################################
#
#  MainWindow.py
#  Author: Cody Johnson <codyj@protonmail.com>
#
################################################################################

import sys
from ui_MainWindow import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.show()
