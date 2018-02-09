################################################################################
#                                                                              #
#  PasswordSetupDialog.py                                                      #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, bcrypt
from ui_PasswordSetupDialog import Ui_PasswordSetupDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import pyqtSlot

class PasswordSetupDialog(QtWidgets.QDialog, Ui_PasswordSetupDialog):
    # Class variables
    settings = {}
    password = ''

    # Initializer
    ############################################################################
    def __init__(self, parent, settings):
        super(PasswordSetupDialog, self).__init__(parent)
        self.initUI()
        self.settings = settings
        self.centerOnScreen()

    # Initialize UI
    ############################################################################
    def initUI(self):
        self.setupUi(self)
        self.setPasswordButton.setEnabled(False)
        self.setPasswordButton.setDefault(True)

        # Connect actions
        self.setPasswordButton.clicked.connect(self.setPassword)
        self.cancelButton.clicked.connect(self.reject)
        self.secondPassLE.textChanged.connect(self.checkPasswords)

    # Check if passwords match
    ############################################################################
    @pyqtSlot()
    def checkPasswords(self):
        firstPass = self.firstPassLE.text()
        secondPass = self.secondPassLE.text()

        if firstPass != secondPass:
            self.firstPassLE.setStyleSheet("QLineEdit{background: red;}")
            self.secondPassLE.setStyleSheet("QLineEdit{background: red;}")
            self.setPasswordButton.setEnabled(False)
        else:
            self.firstPassLE.setStyleSheet("QLineEdit{background: green;}")
            self.secondPassLE.setStyleSheet("QLineEdit{background: green;}")
            self.setPasswordButton.setEnabled(True)

    # Sets password
    ############################################################################
    def setPassword(self):
        password = self.secondPassLE.text()
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        self.settings['password'] = hashed.decode('utf-8')
        self.settings['encrypted'] = True
        self.password = password
        self.accept()

    # Return settings
    ############################################################################
    def getSettings(self):
        return self.settings

    # Return password
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
