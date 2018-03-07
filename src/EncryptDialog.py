################################################################################
#                                                                              #
#  EncryptDialog.py                                                            #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path
from ui_EncryptDialog import Ui_EncryptDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import pyqtSlot

class EncryptDialog(QtWidgets.QDialog, Ui_EncryptDialog):
    # Initializer
    ############################################################################
    def __init__(self, parent):
        super(EncryptDialog, self).__init__(parent)
        self.initUI()
        self.loadSettings()
        self.centerOnScreen()

    # Initialize UI
    ############################################################################
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.yesButton.clicked.connect(self.accept)
        self.noButton.clicked.connect(self.reject)

    # Centers dialog on the screen
    ############################################################################
    def centerOnScreen(self):
        desktopSize = QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (self.height() / 2)
        left = (desktopSize.width() / 2) - (self.width() / 2)
        self.move(left, top)
