################################################################################
#                                                                              #
#  ManageDialog.py                                                             #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json
from ui_ManageDialog import Ui_ManageDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QListWidgetItem

class ManageDialog(QtWidgets.QDialog, Ui_ManageDialog):
    # Class data
    accounts = []

    # Initializer
    def __init__(self, parent, accounts):
        super(ManageDialog, self).__init__(parent)
        self.initUI()
        self.accounts = accounts
        self.refreshList()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.okButton.clicked.connect(self.accept)
        self.loadButton.clicked.connect(self.loadAccount)
        self.removeButton.clicked.connect(self.removeAccount)

    # Saves account information to file
    ############################################################################
    @pyqtSlot()
    def getAccounts(self):
        return self.accounts

    # Loads account from file into the setup dialog
    ############################################################################
    def loadAccount(self):
        idToLoad = self.accountList.currentItem().text().rstrip()

        # Ensure loaded account is last used
        for i in self.accounts:
            if i['lastUsed'] == True and i['accountId'] != idToLoad:
                i['lastUsed'] = False
            if i['accountId'] == idToLoad:
                i['lastUsed'] = True

        self.accept()

    # Removes account from file
    ############################################################################
    def removeAccount(self):
        idToRemove = self.accountList.currentItem().text()
        for i in self.accounts:
            if idToRemove == i['accountId']:
                self.accounts.remove(i)
                break

        self.refreshList()

    # Refreshes the account list
    ############################################################################
    def refreshList(self):
        self.accountList.clear()
        if not self.accounts:
            self.checkEmptyList()

        for i in self.accounts:
            QListWidgetItem(i['accountId'], self.accountList)
        self.checkEmptyList()

    # Checks for empty list to prevent invalid actions
    ############################################################################
    def checkEmptyList(self):
        if self.accountList.count() == 0:
            self.loadButton.setEnabled(False)
            self.removeButton.setEnabled(False)
        else:
            self.loadButton.setEnabled(True)
            self.removeButton.setEnabled(True)
