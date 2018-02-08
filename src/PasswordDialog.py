################################################################################
#                                                                              #
#  PasswordDialog.py                                                           #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, bcrypt
from ui_PasswordDialog import Ui_PasswordDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import pyqtSlot

class PasswordDialog(QtWidgets.QDialog, Ui_PasswordDialog):
    # Class variables
    passwordHash = ''
    password = ''

    # Initializer
    def __init__(self, passwordHash, parent):
        super(PasswordDialog, self).__init__(parent)
        self.initUI()
        self.passwordHash = passwordHash
        self.centerOnScreen()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.decryptButton.clicked.connect(self.checkPassword)
        self.exitButton.clicked.connect(self.reject)

    # Check password for validity
    ############################################################################
    def checkPassword(self):
        password = self.passwordLE.text()
        if bcrypt.checkpw(password.encode('utf-8'),
        self.passwordHash.encode('utf-8')):
            self.password = password
            self.accept()
        else:
            self.passwordLE.setStyleSheet("QLineEdit{background: red;}");

    # Returns password
    ############################################################################
    def getPassword(self):
        return self.password

    # Centers dialog on the screen
    ############################################################################
    def centerOnScreen(self):
        desktopSize = QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (self.height() / 2)
        left = (desktopSize.width() / 2) - (self.width() / 2)
        self.move(left, top)
