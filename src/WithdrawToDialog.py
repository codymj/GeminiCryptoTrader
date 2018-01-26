################################################################################
#                                                                              #
#  WithdrawToDialog.py                                                      #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_WithdrawToDialog import Ui_WithdrawToDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class WithdrawToDialog(QtWidgets.QDialog, Ui_WithdrawToDialog):
    # Initializer
    def __init__(self, parent):
        super(WithdrawToDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.btcRB.clicked.connect(self.btcRBClicked)
        self.ethRB.clicked.connect(self.ethRBClicked)
        self.cancelButton.clicked.connect(self.close)

    # Slots
    @pyqtSlot()
    def btcRBClicked(self):
        if self.btcRB.isChecked():
            self.amountUnitLabel.setText('BTC')
    @pyqtSlot()
    def ethRBClicked(self):
        if self.ethRB.isChecked():
            self.amountUnitLabel.setText('ETH')