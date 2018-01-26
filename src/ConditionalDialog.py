################################################################################
#
#  ConditionalDialog.py
#  Author: Cody Johnson <codyj@protonmail.com>
#
################################################################################

import sys
from ui_ConditionalDialog import Ui_ConditionalDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class ConditionalDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(ConditionalDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        ui = Ui_ConditionalDialog()
        ui.setupUi(self)

        # Connect actions
        ui.cancelButton.clicked.connect(self.close)
