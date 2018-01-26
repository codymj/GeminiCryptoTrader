################################################################################
#                                                                              #
#  AboutDialog.py                                                              #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_AboutDialog import Ui_AboutDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class AboutDialog(QtWidgets.QDialog, Ui_AboutDialog):
    # Initializer
    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.closeButton.clicked.connect(self.close)
