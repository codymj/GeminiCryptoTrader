################################################################################
#                                                                              #
#  SetupDialog.py                                                              #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json
import os.path
from ui_SetupDialog import Ui_SetupDialog
from ManageDialog import ManageDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

class SetupDialog(QtWidgets.QDialog, Ui_SetupDialog):
    # Class data
    accountsData = []

    # Initializer
    def __init__(self, parent):
        super(SetupDialog, self).__init__(parent)
        self.initUI()
        self.loadAccountInfoFromFile()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.saveAccountInfoToFile)
        self.manageButton.clicked.connect(self.openManageDialog)

    # Slots
    @pyqtSlot()
    def saveAccountInfoToFile(self):
        # Check for duplicates
        for i in self.accountsData:
            if i['accountId'] == self.accountIdLE.text():
                msg = QMessageBox()
                msg.setText('This Account ID already exists.')
                msg.exec()
                return
            if i['apiKey'] == self.apiKeyLE.text():
                msg = QMessageBox()
                msg.setText('This API key already exists.')
                msg.exec()
                return
            if i['privKey'] == self.privateKeyLE.text():
                msg = QMessageBox()
                msg.setText('This private key already exists.')
                msg.exec()
                return

        # Check for invalid input
        if (self.apiKeyLE.text() == '' or self.accountIdLE.text() == ''):
            msg = QMessageBox()
            msg.setText('Account ID and API Key are required.')
            msg.exec()
            return

        # Structure input into JSON
        data = {
            'lastUsed':     True,
            'accountId':    self.accountIdLE.text(),
            'apiKey':       self.apiKeyLE.text(),
            'privKey':      self.privateKeyLE.text(),
            'sandbox':      self.sandboxCB.isChecked()
        }

        # Ensure last used account is unique
        for i in self.accountsData:
            if i['lastUsed'] == True and i['accountId'] != data['accountId']:
                i['lastUsed'] = False

        # Append new data to rest of account data
        self.accountsData.append(data)

        # Write to file
        with open('AccountData.json', 'w') as f:
            json.dump(self.accountsData, f)
        self.close()

    @pyqtSlot()
    def openManageDialog(self):
        md = ManageDialog(self, self.accountsData)
        if md.exec_():
            self.loadAccountInfoFromFile()

    # Functions
    def loadAccountInfoFromFile(self):
        # If file doesn't exist, create one with basic info
        if not os.path.exists('AccountData.json'):
            data = [
            {
                'lastUsed':     True,
                'accountId':    '',
                'apiKey':       '',
                'privKey':      '',
                'sandbox':      False
            }]
            with open('AccountData.json', 'w') as f:
                json.dump(data, f)
        else:
            # Clear temp data to reload
            self.accountsData.clear()

            # Load file
            with open('AccountData.json', 'r') as f:
                data = json.load(f)

            # Import most recently used account info and append all to temp list
            for i in data:
                if i['lastUsed'] == True:
                    self.accountIdLE.setText(i['accountId'])
                    self.apiKeyLE.setText(i['apiKey'])
                    self.privateKeyLE.setText(i['privKey'])
                    self.sandboxCB.setChecked(i['sandbox'])
                    self.accountsData.append(i)
                else:
                    self.accountsData.append(i)
