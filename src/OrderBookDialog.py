################################################################################
#                                                                              #
#  OrderBookDialog.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_OrderBookDialog import Ui_OrderBookDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class OrderBookDialog(QtWidgets.QDialog, Ui_OrderBookDialog):
    # Initializer
    def __init__(self, parent):
        super(OrderBookDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.closeButton.clicked.connect(self.close)
