################################################################################
#                                                                              #
#  GenDepositAddrDialog.py                                                     #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_GenDepositAddrDialog import Ui_GenDepositAddrDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class GenDepositAddrDialog(QtWidgets.QDialog):
    # Initializer
    def __init__(self, parent):
        super(GenDepositAddrDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        ui = Ui_GenDepositAddrDialog()
        ui.setupUi(self)

        # Connect actions
        ui.closeButton.clicked.connect(self.close)
