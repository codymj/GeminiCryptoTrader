################################################################################
#                                                                              #
#  SellDialog.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_SellDialog import Ui_SellDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class SellDialog(QtWidgets.QDialog, Ui_SellDialog):
    # Initializer
    def __init__(self, parent):
        super(SellDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.cancelButton.clicked.connect(self.close)
