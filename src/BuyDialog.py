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

class BuyDialog(QtWidgets.QDialog):
    # Initializer
    def __init__(self, parent):
        super(BuyDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        ui = Ui_BuyDialog()
        ui.setupUi(self)

        # Connect actions
        ui.cancelButton.clicked.connect(self.close)
