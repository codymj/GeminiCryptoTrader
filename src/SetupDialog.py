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

class SetupDialog(QtWidgets.QDialog, Ui_SetupDialog):
    # Initializer
    def __init__(self, parent):
        super(SetupDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.cancelButton.clicked.connect(self.close)
        #self.okButton.clicked.connect(self.saveAccountInfoToFile)

    # Save account information to file
    #@pyqtSlot()
    #def saveAccountInfoToFile(self):
