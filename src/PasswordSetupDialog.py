################################################################################
#                                                                              #
#  PasswordSetupDialog.py                                                      #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, bcrypt
from ui_PasswordSetupDialog import Ui_PasswordSetupDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class PasswordSetupDialog(QtWidgets.QDialog, Ui_PasswordSetupDialog):
    # Class variables
    settings = {}

    # Initializer
    ############################################################################
    def __init__(self, parent):
        super(PasswordSetupDialog, self).__init__(parent)
        self.initUI()

    # Initialize UI
    ############################################################################
    def initUI(self):
        self.setupUi(self)
        self.setPasswordButton.setEnabled(False)

        # Connect actions
        self.setPasswordButton.clicked.connect(self.setPassword)
        self.cancelButton.clicked.connect(self.reject)
        self.reEnterPasswordLE.textChanged.connect(self.checkPasswords)

    # Check if passwords match
    ############################################################################
    @pyqtSlot()
    def checkPasswords(self):
        firstPass = self.initialPasswordLE.text()
        secondPass = self.reEnterPasswordLE.text()

        if firstPass != secondPass:
            self.initialPasswordLE.setStyleSheet("QLineEdit{background: red;}");
            self.reEnterPasswordLE.setStyleSheet("QLineEdit{background: red;}");
            self.setPasswordButton.setEnabled(False)
        else:
            self.initialPasswordLE.setStyleSheet("QLineEdit{background: green;}");
            self.reEnterPasswordLE.setStyleSheet("QLineEdit{background: green;}");
            self.setPasswordButton.setEnabled(True)

    # Saves hashed password to file
    def setPassword(self):
        password = self.reEnterPasswordLE.text()
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        print(hashed)
        print(hashed.decode('utf-8'))
        self.settings['password'] = hashed.decode('utf-8')
        self.settings['encrypted'] = True
        self.saveSettings()

    # Loads settings
    ############################################################################
    def loadSettings(self):
        with open('Settings.json', 'r') as f:
            self.settings = json.load(f)

    # Save settings
    def saveSettings(self):
        # Write to file
        with open('Settings.json', 'w') as f:
            json.dump(self.settings, f)

        self.close()
