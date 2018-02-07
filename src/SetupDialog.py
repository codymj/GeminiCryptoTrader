################################################################################
#                                                                              #
#  SetupDialog.py                                                              #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path
from ui_SetupDialog import Ui_SetupDialog
from ManageDialog import ManageDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

class SetupDialog(QtWidgets.QDialog, Ui_SetupDialog):
    # Class data
    accountsData = []
    settings = {}

    # Initializer
    def __init__(self, settings, parent):
        super(SetupDialog, self).__init__(parent)
        self.initUI()
        self.loadAccountInfoFromFile()
        self.settings = settings
        print(self.settings)

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.doneButton.clicked.connect(self.accept)
        self.addButton.clicked.connect(self.saveAccountInfoToFile)
        self.updateButton.clicked.connect(self.updateAccountInfo)
        self.manageButton.clicked.connect(self.openManageDialog)

    # Save account information to file
    ############################################################################
    @pyqtSlot()
    def saveAccountInfoToFile(self):
        data = self.inputToJson()

        # Check for invalid input
        if not self.validInput(data, False):
            return

        # Append new data to rest of account data
        self.accountsData.append(data)

        # Write to file
        with open('AccountData.json', 'w') as f:
            json.dump(self.accountsData, f)

    # Update saved account information
    ############################################################################
    @pyqtSlot()
    def updateAccountInfo(self):
        data = self.inputToJson()

        # Check for valid input
        if not self.validInput(data, True):
            return

        # Search through account data to edit
        for i in self.accountsData:
            if i['accountId'] == data['accountId']:
                i['apiKey'] = data['apiKey']
                i['privKey'] = data['privKey']
                i['sandbox'] = data['sandbox']

        # Write updates to file
        with open('AccountData.json', 'w') as f:
            json.dump(self.accountsData, f)

    # Open the manage accounts dialog
    ############################################################################
    @pyqtSlot()
    def openManageDialog(self):
        md = ManageDialog(self, self.accountsData)
        if md.exec_():
            self.loadAccountInfoFromFile()

    # Translate input data into a JSON object
    ############################################################################
    def inputToJson(self):
        data = {
            'lastUsed':     True,
            'accountId':    self.accountIdLE.text(),
            'apiKey':       self.apiKeyLE.text(),
            'privKey':      self.privateKeyLE.text(),
            'sandbox':      self.sandboxCB.isChecked()
        }
        return data

    # Validate input, _forUpdate is flag for updating already saved account
    ############################################################################
    def validInput(self, _data, _forUpdate):
        # Check for duplicates
        if not _forUpdate:
            for i in self.accountsData:
                if i['accountId'] == _data['accountId']:
                    msg = QMessageBox()
                    msg.setText('This Account ID already exists.')
                    msg.exec()
                    return False
                if i['apiKey'] == _data['apiKey']:
                    msg = QMessageBox()
                    msg.setText('This API key already exists.')
                    msg.exec()
                    return False
                if i['privKey'] == _data['privKey']:
                    msg = QMessageBox()
                    msg.setText('This private key already exists.')
                    msg.exec()
                    return False

        # Ensure account ID and API key are provided
        if (_data['accountId'] == '' or _data['apiKey'] == ''):
            msg = QMessageBox()
            msg.setText('Account ID and API Key are required.')
            msg.exec()
            return False

        # Ensure last used account is unique
        for i in self.accountsData:
            if i['lastUsed'] == True and i['accountId'] != _data['accountId']:
                i['lastUsed'] = False

        # Return input is valid
        return True

    # Loads account information from file
    ############################################################################
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
