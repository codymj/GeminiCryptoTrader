################################################################################
#                                                                              #
#  OptionsDialog.py                                                            #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_OptionsDialog import Ui_OptionsDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from EncryptDialog import EncryptDialog
from PasswordSetupDialog import PasswordSetupDialog

class OptionsDialog(QtWidgets.QDialog, Ui_OptionsDialog):
    # Class data
    settings = {}
    password = ''

    # Initializer
    def __init__(self, parent, settings):
        super(OptionsDialog, self).__init__(parent)
        self.initUI()
        self.settings = settings
        # Load settings here

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.doneButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
        self.encryptButton.clicked.connect(self.parent().openEncryptDialog)

    # Return password
    ############################################################################
    def getPassword(self):
        return self.password

    # Return settings
    ############################################################################
    def getSettings(self):
        return self.settings
