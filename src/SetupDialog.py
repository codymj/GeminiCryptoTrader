################################################################################
#                                                                              #
#  SetupDialog.py                                                              #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json
import os.path
from ui_SetupDialog import Ui_SetupDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

class SetupDialog(QtWidgets.QDialog, Ui_SetupDialog):
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

    # Slots
    @pyqtSlot()
    def saveAccountInfoToFile(self):
        if (self.apiKeyLE.text() == ''):
            msg = QMessageBox()
            msg.setText('API Key is required.')
            msg.exec()
            return

        data = {
            'accountId':    self.accountIdLE.text(),
            'apiKey':       self.apiKeyLE.text(),
            'privKey':      self.privateKeyLE.text(),
            'sandbox':      self.sandboxCB.isChecked()
        }
        with open('AccountData.json', 'w') as f:
            json.dump(data, f)

        self.close()

    # Functions
    def loadAccountInfoFromFile(self):
        if not os.path.exists('AccountData.json'):
            data = {
                'accountId':    '',
                'apiKey':       '',
                'privKey':      '',
                'sandbox':      False
            }
            with open('AccountData.json', 'w') as f:
                json.dump(data, f)
        else:
            with open('AccountData.json', 'r') as f:
                data = json.load(f)

            self.accountIdLE.setText(data['accountId'])
            self.apiKeyLE.setText(data['apiKey'])
            self.privateKeyLE.setText(data['privKey'])
            self.sandboxCB.setChecked(data['sandbox'])
