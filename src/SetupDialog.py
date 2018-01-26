################################################################################
#                                                                              #
#  SetupDialog.py                                                              #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_SetupDialog import Ui_SetupDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class SetupDialog(QtWidgets.QDialog):
    # Initializer
    def __init__(self, parent):
        super(SetupDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        ui = Ui_SetupDialog()
        ui.setupUi(self)

        # Connect actions
        ui.cancelButton.clicked.connect(self.close)
        #ui.okButton.clicked.connect(self.saveAccountInfoToFile)

    # Save account information to file
    #@pyqtSlot()
    #def saveAccountInfoToFile(self):
