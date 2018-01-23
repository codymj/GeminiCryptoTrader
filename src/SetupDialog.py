################################################################################
#
#  SetupDialog.py
#  Author: Cody Johnson <codyj@protonmail.com>
#
################################################################################

import sys
from ui_SetupDialog import Ui_SetupDialog
from PyQt5 import QtGui, QtWidgets, uic

class SetupDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(SetupDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        ui = Ui_SetupDialog()
        ui.setupUi(self)

        # Connect actions
        ui.cancelButton.clicked.connect(self.close)
