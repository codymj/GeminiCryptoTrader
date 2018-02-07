################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path
import icons
import urllib
from urllib.request import urlopen
from urllib.error import URLError
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow import Ui_MainWindow
from SetupDialog import SetupDialog
from EncryptDialog import EncryptDialog
from PasswordSetupDialog import PasswordSetupDialog
from BuyDialog import BuyDialog
from SellDialog import SellDialog
from ConditionalDialog import ConditionalDialog
from GenDepositAddrDialog import GenDepositAddrDialog
from WithdrawToDialog import WithdrawToDialog
from AboutDialog import AboutDialog

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Class data
    apiData = {}
    settings = {}

    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.onStart()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Status Bar
        self.statusBar.showMessage('Gemini CryptoTrader started...', msecs=3000)

        # Connect actions
        self.setupAction.triggered.connect(self.openSetupDialog)
        self.buyAction.triggered.connect(self.openBuyDialog)
        self.sellAction.triggered.connect(self.openSellDialog)
        self.conditionalAction.triggered.connect(self.openConditionalDialog)
        self.genDepositAction.triggered.connect(self.openGenDepositAddrDialog)
        self.withdrawToAction.triggered.connect(self.openWithdrawToDialog)
        self.exitAction.triggered.connect(self.close)
        self.toggleStatusBarAction.triggered.connect(self.toggleStatusBar)
        self.aboutAction.triggered.connect(self.openAboutDialog)

    # Check internet connection and check for AccountData.json to import last
    # used account information
    ############################################################################
    def onStart(self):
        # Check internet connection
        if self.internetAvailable(self):
            self.connectIconPM = QPixmap(':/orange-circle.png')
        else:
            self.connectIconPM = QPixmap(':/red-circle.png')
        self.connectIconLabel = QLabel(self)
        self.connectIconLabel.setPixmap(self.connectIconPM)
        self.statusBar.setToolTip('Green when connected to exchange')
        self.statusBar.addPermanentWidget(self.connectIconLabel)

        # Check for Settings.json, if not created, this is the first run
        if not os.path.exists('Settings.json'):
            self.openEncryptDialog()
        else:
            self.loadSettings()

        # Check for AccountData.json and run SetupDialog if not created
        if not os.path.exists('AccountData.json'):
            self.openSetupDialog()
        else:
            self.loadApiData()

    # Loads settings
    ############################################################################
    def loadSettings(self):
        with open('Settings.json', 'r') as f:
            self.settings = json.load(f)

    # Loads last used account data from Accounts.json file
    ############################################################################
    def loadApiData(self):
        # Load file
        with open('AccountData.json', 'r') as f:
            data = json.load(f)

        # Import most recently used account info and append all to temp list
        for i in data:
            if i['lastUsed'] == True:
                self.apiData['accountId'] = i['accountId']
                self.apiData['apiKey'] = i['apiKey']
                self.apiData['privKey'] = i['privKey']
                self.apiData['sandbox'] = i['sandbox']

    # Opens encryption dialog
    ############################################################################
    @pyqtSlot()
    def openEncryptDialog(self):
        ed = EncryptDialog(self)
        if ed.exec_():
            self.openPasswordSetupDialog()

    # Opens password setup dialog
    ############################################################################
    @pyqtSlot()
    def openPasswordSetupDialog(self):
        psd = PasswordSetupDialog(self)
        psd.exec_()
        self.loadSettings()

    # Opens setup dialog
    ############################################################################
    @pyqtSlot()
    def openSetupDialog(self):
        sd = SetupDialog(self.settings, self)
        if sd.exec_():
            self.loadApiData()

    # Opens buy dialog
    ############################################################################
    @pyqtSlot()
    def openBuyDialog(self):
        bd = BuyDialog(self)
        bd.exec_()

    # Opens sell dialog
    ############################################################################
    @pyqtSlot()
    def openSellDialog(self):
        sd = SellDialog(self)
        sd.exec_()

    # Opens conditional dialog
    ############################################################################
    @pyqtSlot()
    def openConditionalDialog(self):
        cd = ConditionalDialog(self)
        cd.exec_()

    # Opens dialog to generate new deposit address
    ############################################################################
    @pyqtSlot()
    def openGenDepositAddrDialog(self):
        gd = GenDepositAddrDialog(self)
        gd.exec_()

    # Opens withdraw dialog
    ############################################################################
    @pyqtSlot()
    def openWithdrawToDialog(self):
        wd = WithdrawToDialog(self)
        wd.exec_()

    # Opens about dialog
    ############################################################################
    @pyqtSlot()
    def openAboutDialog(self):
        ad = AboutDialog(self)
        ad.exec_()

    # Toggles status bar on or off
    ############################################################################
    @pyqtSlot()
    def toggleStatusBar(self):
        if self.statusBar.isVisible():
            self.statusBar.hide()
            self.toggleStatusBarAction.setText('Show Statusbar')
        else:
            self.statusBar.show()
            self.toggleStatusBarAction.setText('Hide Statusbar')

    # Checks internet connection using Google IP
    ############################################################################
    @staticmethod
    def internetAvailable(arg):
        try:
            urlopen('http://74.125.21.99', timeout=1)
            return True
        except URLError as err:
            return False
