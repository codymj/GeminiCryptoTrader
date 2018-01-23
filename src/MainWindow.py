################################################################################
#
#  MainWindow.py
#  Author: Cody Johnson <codyj@protonmail.com>
#
################################################################################

import sys
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow import Ui_MainWindow
from SetupDialog import SetupDialog

class MainWindow(QtWidgets.QMainWindow):
    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    # Initialize UI
    def initUI(self):
        ui = Ui_MainWindow()
        ui.setupUi(self)

        # Connect actions
        ui.setupAction.triggered.connect(self.openSetupDialog)
        ui.exitAction.triggered.connect(self.close)

    # Open SetupDialog
    @pyqtSlot()
    def openSetupDialog(self):
        sd = SetupDialog(self)
        sd.show()