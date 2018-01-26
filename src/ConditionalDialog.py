################################################################################
#                                                                              #
#  ConditionalDialog.py                                                        #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_ConditionalDialog import Ui_ConditionalDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class ConditionalDialog(QtWidgets.QDialog, Ui_ConditionalDialog):
    # Initializer
    def __init__(self, parent):
        super(ConditionalDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.cancelButton.clicked.connect(self.close)
