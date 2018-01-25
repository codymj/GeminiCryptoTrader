################################################################################
#
#  SellDialog.py
#  Author: Cody Johnson <codyj@protonmail.com>
#
################################################################################

import sys
from ui_SellDialog import Ui_SellDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class SellDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(SellDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        ui = Ui_SellDialog()
        ui.setupUi(self)

        # Connect actions
        ui.cancelButton.clicked.connect(self.close)
        #ui.okButton.clicked.connect(self.saveAccountInfoToFile)
