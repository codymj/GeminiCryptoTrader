################################################################################
#                                                                              #
#  AccountsDialog.py                                                              #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, base64
from EncryptFiles import *
from ui_AccountsDialog import Ui_AccountsDialog
from ManageDialog import ManageDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget

class AccountsDialog(QtWidgets.QDialog, Ui_AccountsDialog):
    # Class data
    accounts = []
    lastUsedAccount = {}
    settings = {}
    password = ''

    # Initializer
    def __init__(self, parent, accounts, settings, password):
        super(AccountsDialog, self).__init__(parent)
        self.initUI()
        self.accounts = accounts
        self.settings = settings
        self.password = password
        self.setLastUsedAccount()
        self.centerOnScreen()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.doneButton.clicked.connect(self.accept)
        self.addButton.clicked.connect(self.addAccount)
        self.updateButton.clicked.connect(self.updateAccount)
        self.manageButton.clicked.connect(self.openManageDialog)

    # Return account list
    ############################################################################
    @pyqtSlot()
    def getAccounts(self):
        return self.accounts

    # Adds a new account
    ############################################################################
    def addAccount(self):
        data = self.toJson()
        self.accounts.append(data)

    # Update saved account information
    ############################################################################
    @pyqtSlot()
    def updateAccount(self):
        data = self.toJson()

        # Search through account data to edit
        for i in self.accounts:
            if i['accountId'] == data['accountId']:
                i['apiKey'] = data['apiKey']
                i['privKey'] = data['privKey']
                i['sandbox'] = data['sandbox']

        # Write updates to file
        with open('Accounts.json', 'w') as f:
            json.dump(self.accounts, f)

    # Open the manage accounts dialog
    ############################################################################
    @pyqtSlot()
    def openManageDialog(self):
        md = ManageDialog(self, self.accounts)
        if md.exec_():
            self.accounts = md.getAccounts()
            self.setLastUsedAccount()

    # Translate input data into a JSON object
    ############################################################################
    def toJson(self):
        # Get data from input
        data = {
            'lastUsed':     True,
            'accountId':    self.accountIdLE.text(),
            'apiKey':       self.apiKeyLE.text(),
            'privKey':      self.privateKeyLE.text(),
            'sandbox':      self.sandboxCB.isChecked()
        }

        # Check for valid input
        if not self.validateInput(data, True):
            return

        return data

    # Validate input; forUpdate is a flag for updating already saved account
    ############################################################################
    def validateInput(self, data, forUpdate):
        # Check for duplicates
        if not forUpdate:
            for i in self.accounts:
                if i['accountId'] == data['accountId']:
                    msg = QMessageBox()
                    msg.setText('This Account ID already exists.')
                    msg.exec()
                    return False
                if i['apiKey'] == data['apiKey']:
                    msg = QMessageBox()
                    msg.setText('This API key already exists.')
                    msg.exec()
                    return False
                if i['privKey'] == data['privKey']:
                    msg = QMessageBox()
                    msg.setText('This private key already exists.')
                    msg.exec()
                    return False

        # Ensure account ID and API key are provided
        if (data['accountId'] == '' or data['apiKey'] == ''):
            msg = QMessageBox()
            msg.setText('Account ID and API Key are required.')
            msg.exec()
            return False

        # Ensure last used account is unique
        for i in self.accounts:
            if i['lastUsed'] == True and i['accountId'] != data['accountId']:
                i['lastUsed'] = False

        # Return input is valid
        return True

    # Loads account information from file
    ############################################################################
    def setLastUsedAccount(self):
        if not self.accounts:
            self.accountIdLE.setText('')
            self.apiKeyLE.setText('')
            self.privateKeyLE.setText('')
            self.sandboxCB.setChecked(False)
            self.lastUsedAccount = {}
        else:
            for i in self.accounts:
                if i['lastUsed'] == True:
                    self.accountIdLE.setText(i['accountId'])
                    self.apiKeyLE.setText(i['apiKey'])
                    self.privateKeyLE.setText(i['privKey'])
                    self.sandboxCB.setChecked(i['sandbox'])
                    self.lastUsedAccount = i
                    break

    # Returns last used account
    ############################################################################
    def getLastUsedAccount(self):
        return self.lastUsedAccount

    # Centers dialog on the screen
    ############################################################################
    def centerOnScreen(self):
        desktopSize = QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (self.height() / 2)
        left = (desktopSize.width() / 2) - (self.width() / 2)
        self.move(left, top)
