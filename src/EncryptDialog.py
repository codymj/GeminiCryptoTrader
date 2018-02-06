################################################################################
#                                                                              #
#  EncryptDialog.py                                                            #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path
from ui_EncryptDialog import Ui_EncryptDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class EncryptDialog(QtWidgets.QDialog, Ui_EncryptDialog):
    # Class variables
    settings = {}

    # Initializer
    ############################################################################
    def __init__(self, parent):
        super(EncryptDialog, self).__init__(parent)
        self.initUI()
        self.loadSettings()

    # Initialize UI
    ############################################################################
    def initUI(self):
        self.setupUi(self)

        # Connect actions
        self.yesButton.clicked.connect(self.accept)
        self.noButton.clicked.connect(self.reject)

    # Creates Settings.json file on first run
    ############################################################################
    def loadSettings(self):
        # If file doesn't exist, create one with basic info
        if not os.path.exists('Settings.json'):
            self.settings = {
                'firstRun':   False,
                'password':   '',
            }
            with open('Settings.json', 'w') as f:
                    json.dump(self.settings, f)
        else:
            # Clear temp data to reload
            self.settings.clear()

            # Load file
            with open('Settings.json', 'r') as f:
                self.settings = json.load(f)
