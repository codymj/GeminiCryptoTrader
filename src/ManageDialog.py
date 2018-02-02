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
    # Class variables
    accountsData = []

    # Initializer
    def __init__(self, parent, _accountsData):
        super(ManageDialog, self).__init__(parent)
        self.initUI()
        self.accountsData = _accountsData
        self.refreshList()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.okButton.clicked.connect(self.saveAccountInfoToFile)
        self.loadButton.clicked.connect(self.loadAccount)
        self.removeButton.clicked.connect(self.removeAccount)

    # Slots
    @pyqtSlot()
    def saveAccountInfoToFile(self):
        with open('AccountData.json', 'w') as f:
            json.dump(self.accountsData, f)
        self.close()

    # Functions
    def loadAccount(self):
        idToLoad = self.accountList.currentItem().text().rstrip()

        # Ensure loaded account is last used
        for i in self.accountsData:
            if i['lastUsed'] == True and i['accountId'] != idToLoad:
                i['lastUsed'] = False
            if i['accountId'] == idToLoad:
                i['lastUsed'] = True

        # Save file and return to parent
        self.saveAccountInfoToFile()
        self.accept()

    def removeAccount(self):
        idToRemove = self.accountList.currentItem().text()
        for i in self.accountsData:
            if idToRemove == i['accountId']:
                self.accountsData.remove(i)
                break
        self.refreshList()

    def refreshList(self):
        self.accountList.clear()
        for i in self.accountsData:
            QListWidgetItem(i['accountId'], self.accountList)
        self.checkEmptyList()

    def checkEmptyList(self):
        if self.accountList.count() == 0:
            self.loadButton.setEnabled(False)
            self.removeButton.setEnabled(False)
        else:
            self.loadButton.setEnabled(True)
            self.removeButton.setEnabled(True)
