################################################################################
#                                                                              #
#  BuyDialog.py                                                                #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_BuyDialog import Ui_BuyDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class BuyDialog(QtWidgets.QDialog, Ui_BuyDialog):
    # Initializer
    def __init__(self, parent):
        super(BuyDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.cancelButton.clicked.connect(self.close)
