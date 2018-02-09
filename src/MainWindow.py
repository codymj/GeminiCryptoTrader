################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, icons, urllib
from urllib.request import urlopen
from urllib.error import URLError
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow import Ui_MainWindow
from AccountsDialog import AccountsDialog
from EncryptDialog import EncryptDialog
from PasswordSetupDialog import PasswordSetupDialog
from PasswordDialog import PasswordDialog
from BuyDialog import BuyDialog
from SellDialog import SellDialog
from ConditionalDialog import ConditionalDialog
from GenDepositAddrDialog import GenDepositAddrDialog
from WithdrawToDialog import WithdrawToDialog
from AboutDialog import AboutDialog
from EncryptFiles import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Class data
    accounts = []   # List of accounts
    account = {}    # Current account
    settings = {}   # Loaded settings
    password = ''   # Password in plaintext (never saved)

    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.startUp()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Status Bar
        self.statusBar.showMessage('Gemini CryptoTrader started...', msecs=3000)

        # Connect actions
        self.setupAction.triggered.connect(self.openAccountsDialog)
        self.buyAction.triggered.connect(self.openBuyDialog)
        self.sellAction.triggered.connect(self.openSellDialog)
        self.conditionalAction.triggered.connect(self.openConditionalDialog)
        self.genDepositAction.triggered.connect(self.openGenDepositAddrDialog)
        self.withdrawToAction.triggered.connect(self.openWithdrawToDialog)
        self.exitAction.triggered.connect(self.close)
        self.toggleStatusBarAction.triggered.connect(self.toggleStatusBar)
        self.aboutAction.triggered.connect(self.openAboutDialog)

    # Run start up processes
    ############################################################################
    def startUp(self):
        # Check internet connection
        self.checkConnectivity(self)

        # Load settings
        self.loadSettings()

        # Check if data files exist
        if os.path.exists('Accounts.json') or os.path.exists('Accounts.enc'):
            self.loadAccounts()
        else:
            self.openAccountsDialog()

    # When user closes program, save all data & encrypt if necessary
    ############################################################################
    def closeEvent(self, event):
        # Save data
        self.statusBar.showMessage('Saving data...')
        self.saveAccounts()

        # Encrypt data
        if self.settings['encrypted']:
            self.statusBar.showMessage('Encrypting data...')
            encryptFile(self.password, 'Accounts.json')

    # Loads settings
    ############################################################################
    def loadSettings(self):
        if not os.path.exists('Settings.json'):
            self.openEncryptDialog()

        with open('Settings.json', 'r') as f:
            self.settings = json.load(f)

        # Prompt for password if encryption is enabled
        if self.settings['encrypted']:
            self.openPasswordDialog()

    # Loads last used account data from Accounts.json file
    ############################################################################
    def loadAccounts(self):
        if self.settings['encrypted']:
            # Decrypt file
            self.statusBar.showMessage('Decrypting data...')
            decryptFile(self.password, 'Accounts.enc')
        else:
            self.statusBar.showMessage('Loading data...')

        # Open file to load
        with open('Accounts.json', 'r') as f:
                data = json.load(f)

        # Import most recently used account info and append all to accounts
        self.accounts.clear()
        for i in data:
            if i['lastUsed'] == True:
                self.account['accountId'] = i['accountId']
                self.account['apiKey'] = i['apiKey']
                self.account['privKey'] = i['privKey']
                self.account['sandbox'] = i['sandbox']
                self.accounts.append(i)
            else:
                self.accounts.append(i)

        self.statusBar.showMessage('Data loaded successfully.')

    # Saves accounts to file
    ############################################################################
    def saveAccounts(self):
        with open('Accounts.json', 'w') as f:
            json.dump(self.accounts, f)

    # Opens encryption dialog
    ############################################################################
    @pyqtSlot()
    def openEncryptDialog(self):
        ed = EncryptDialog(self)
        if ed.exec_():
            self.openPasswordAccountsDialog()

    # Opens password setup dialog
    ############################################################################
    @pyqtSlot()
    def openPasswordAccountsDialog(self):
        psd = PasswordAccountsDialog(self.settings, self)
        if psd.exec_():
            self.password = psd.getPassword()

    # Opens password dialog for decryption
    ############################################################################
    @pyqtSlot()
    def openPasswordDialog(self):
        pd = PasswordDialog(self.settings['password'], self)
        if pd.exec_():
            self.password = pd.getPassword()
        else:
            sys.exit()

    # Opens setup dialog
    ############################################################################
    @pyqtSlot()
    def openAccountsDialog(self):
        ad = AccountsDialog(self, self.accounts, self.settings, self.password)
        if ad.exec_():
            self.account = ad.getLastUsedAccount()
            self.accounts = ad.getAccounts()

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
    def checkConnectivity(self):
        connected = False
        try:
            urlopen('http://74.125.21.99', timeout=1)
            connected = True
        except URLError as err:
            connected = False
            print(err)

        # Set connectivity icon in status bar
        if connected:
            self.connectIconPM = QPixmap(':/orange-circle.png')
        else:
            self.connectIconPM = QPixmap(':/red-circle.png')

        self.connectIconLabel = QLabel(self)
        self.connectIconLabel.setPixmap(self.connectIconPM)
        self.statusBar.setToolTip('Green when connected to exchange')
        self.statusBar.addPermanentWidget(self.connectIconLabel)
