################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, icons, urllib, time, datetime
import threading, requests, base64, hmac
from datetime import date, timedelta
from hashlib import sha384
from urllib.request import urlopen
from urllib.error import URLError
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QFileDialog
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
from OptionsDialog import OptionsDialog
from OrderBookDialog import OrderBookDialog
from AboutDialog import AboutDialog
from EncryptFiles import *
from GeminiPublicAPI import MarketData

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Class data
    accounts = []           # List of accounts
    account = {}            # Current account
    accountsDir = ''        # Path of Accounts file
    settings = {}           # Loaded settings
    settingsDir = ''        # Path of Settings file
    password = ''           # Password in plaintext (never saved)
    hasConnection = False   # Internet connection detected
    marketData = None       # MarketData object
    marketDataThread = None # Thread for updating marketData
    balances = []           # List of balance info from Gemini

    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.startUp()

        # Start threads
        self.marketDataThread.start()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Status Bar
        self.statusBar.showMessage('Gemini CryptoTrader started...')

        # Connect actions
        self.setupAction.triggered.connect(self.openAccountsDialog)
        self.buyAction.triggered.connect(self.openBuyDialog)
        self.sellAction.triggered.connect(self.openSellDialog)
        self.conditionalAction.triggered.connect(self.openConditionalDialog)
        self.genDepositAction.triggered.connect(self.openGenDepositAddrDialog)
        self.withdrawToAction.triggered.connect(self.openWithdrawToDialog)
        self.exitAction.triggered.connect(self.close)
        self.optionsAction.triggered.connect(self.openOptionsDialog)
        self.toggleStatusBarAction.triggered.connect(self.toggleStatusBar)
        self.showOrderBookAction.triggered.connect(self.openOrderBookDialog)
        self.aboutAction.triggered.connect(self.openAboutDialog)
        self.connectButton.clicked.connect(self.getTradeHistory)

    # Run start up processes
    ############################################################################
    def startUp(self):
        # Load settings
        self.loadSettings()

        # Load accounts
        self.loadAccounts()

        # Check internet connection & get market data if possible
        if self.internetUp(self):
            self.hasConnection = True
            self.marketData = MarketData(self.account)
        else:
            self.hasConnection = False
            self.statusBar.showMessage('No internet connection detected.')

        # Build threads
        self.marketDataThread = threading.Thread(target=self.marketDataLoop, args=())
        self.marketDataThread.daemon = True

    # When user closes program, save all data & encrypt if necessary
    ############################################################################
    def closeEvent(self, event):
        # Save data
        self.statusBar.showMessage('Saving data...')
        self.saveAccounts()
        self.saveSettings()

        # Encrypt data
        if self.settings['encrypted']:
            self.statusBar.showMessage('Encrypting data...')
            encryptFile(self.password, self.accountsDir)

    # Loads settings
    ############################################################################
    def loadSettings(self):
        if not os.path.exists('Settings.json'):
            msg = QMessageBox()
            msg.setText('No settings file found.')
            msg.setInformativeText('What would you like to do?')
            msg.setStandardButtons(QMessageBox.Open | QMessageBox.Ignore)
            returnVal = msg.exec_()

            # Browse for file
            if returnVal == QMessageBox.Open:
                fileName = QFileDialog.getOpenFileName(self,
                'Browse for Settings.json', '.', 'Settings.json')
                if os.path.exists(fileName[0]):
                    with open(fileName[0], 'r') as f:
                        self.settings = json.load(f)
                    self.settingsDir = fileName[0]
                else:
                    self.openEncryptDialog()
                    self.settingsDir = 'Settings.json'

            # Create new file
            elif returnVal == QMessageBox.Ignore:
                self.openEncryptDialog()
        else:
            with open('Settings.json', 'r') as f:
                self.settings = json.load(f)

        if self.settings['encrypted']:
            self.openPasswordDialog()

    # Updates settings
    ############################################################################
    def updateSettings(self, settings):
        self.settings = settings

    # Loads last used account data from Accounts.json file
    ############################################################################
    def loadAccounts(self):
        # No account files found. Browse or create new files
        if (not self.settings['encrypted'] and
        not os.path.exists('Accounts.json')):
            msg = QMessageBox()
            msg.setText('No Accounts.json file found.')
            msg.setInformativeText('What would you like to do?')
            msg.setStandardButtons(QMessageBox.Open | QMessageBox.Ignore)
            returnVal = msg.exec_()

            # Browse for file
            if returnVal == QMessageBox.Open:
                fileName = QFileDialog.getOpenFileName(self,
                'Browse for Accounts.json', '.', 'Accounts.json')
                if os.path.exists(fileName[0]):
                    with open(fileName[0], 'r') as f:
                        accounts = json.load(f)
                    self.accountsDir = fileName[0]
                    self.updateAccounts(accounts)
                else:
                    self.openAccountsDialog()

            # Create new file
            elif returnVal == QMessageBox.Ignore:
                self.openAccountsDialog()
        # No account files found. Browse or create new files
        elif self.settings['encrypted'] and not os.path.exists('Accounts.enc'):
            msg = QMessageBox()
            msg.setText('No Accounts.enc file found.')
            msg.setInformativeText('What would you like to do?')
            msg.setStandardButtons(QMessageBox.Open | QMessageBox.Ignore)
            returnVal = msg.exec_()

            # Browse for file
            if returnVal == QMessageBox.Open:
                fileName = QFileDialog.getOpenFileName(self,
                'Browse for Accounts.enc', '.', 'Accounts.enc')
                if os.path.exists(fileName[0]):
                    self.statusBar.showMessage('Decrypting data...')
                    decryptFile(self.password, fileName[0])
                    self.statusBar.showMessage('Loading data...')
                    newFileName = os.path.dirname(os.path.abspath(fileName[0]))
                    newFileName = newFileName + '/Accounts.json'
                    with open(newFileName, 'r') as f:
                        accounts = json.load(f)
                    self.accountsDir = newFileName
                    self.updateAccounts(accounts)
                else:
                    self.openAccountsDialog()

            # Create new file
            elif returnVal == QMessageBox.Ignore:
                self.openAccountsDialog()
        # Load accounts
        elif not self.settings['encrypted'] and os.path.exists('Accounts.json'):
            self.statusBar.showMessage('Loading data...')
            with open('Accounts.json', 'r') as f:
                accounts = json.load(f)
            self.updateAccounts(accounts)
        # Decrypt
        elif self.settings['encrypted'] and os.path.exists('Accounts.enc'):
            self.statusBar.showMessage('Decrypting data...')
            decryptFile(self.password, 'Accounts.enc')
            self.statusBar.showMessage('Loading data...')
            with open('Accounts.json', 'r') as f:
                accounts = json.load(f)
            self.updateAccounts(accounts)
        # Else ???
        else:
            print('ERROR: Account files missing.')
            return

        self.statusBar.showMessage('Data loaded successfully.')

    # Updates accounts and calls updateEnabledActions()
    ############################################################################
    def updateAccounts(self, accounts):
        self.accounts = accounts
        for i in accounts:
            if i['lastUsed'] == True:
                self.account = i

        self.updateEnabledActions()

    # Saves accounts to file
    ############################################################################
    def saveAccounts(self):
        if not self.accountsDir:
            self.accountsDir = 'Accounts.json'
        with open(self.accountsDir, 'w') as f:
            json.dump(self.accounts, f)

    # Saves settings to file
    ############################################################################
    def saveSettings(self):
        if not self.settingsDir:
            self.settingsDir = 'Settings.json'
        with open(self.settingsDir, 'w') as f:
            json.dump(self.settings, f)

    # Enables/disables actions based on roles in the account
    ############################################################################
    def updateEnabledActions(self):
        # No account loaded
        if not self.account:
            self.buyAction.setEnabled(False)
            self.sellAction.setEnabled(False)
            self.conditionalAction.setEnabled(False)
            self.genDepositAction.setEnabled(False)
            self.withdrawToAction.setEnabled(False)
            return

        # Account has trader role
        if not self.account['isTrader']:
            self.buyAction.setEnabled(False)
            self.sellAction.setEnabled(False)
            self.conditionalAction.setEnabled(False)
        else:
            self.buyAction.setEnabled(True)
            self.sellAction.setEnabled(True)
            self.conditionalAction.setEnabled(True)

        # Account has fund manager role
        if not self.account['isFundManager']:
            self.genDepositAction.setEnabled(False)
            self.withdrawToAction.setEnabled(False)
        else:
            self.genDepositAction.setEnabled(True)
            self.withdrawToAction.setEnabled(True)

    # Opens encryption dialog
    ############################################################################
    @pyqtSlot()
    def openEncryptDialog(self):
        if not self.settings:
            ed = EncryptDialog(self)
            if ed.exec_():
                self.openPasswordSetupDialog()
            else:
                self.openAccountsDialog()
        elif self.settings['encrypted']:
            msg = QMessageBox()
            msg.setText('Your files are already encrypted.')
            msg.exec()
            return
        else:
            ed = EncryptDialog(self)
            if ed.exec_():
                self.openPasswordSetupDialog()

    # Opens password setup dialog
    ############################################################################
    @pyqtSlot()
    def openPasswordSetupDialog(self):
        psd = PasswordSetupDialog(self, self.settings)
        if psd.exec_():
            self.password = psd.getPassword()
            self.updateSettings(psd.getSettings())

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
            self.updateAccounts(ad.getAccounts())

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

    # Opens options dialog
    ############################################################################
    def openOptionsDialog(self):
        od = OptionsDialog(self, self.settings)
        od.exec_()

    # Opens about dialog
    ############################################################################
    @pyqtSlot()
    def openAboutDialog(self):
        ad = AboutDialog(self)
        ad.exec_()

    # Opens the order book
    ############################################################################
    @pyqtSlot()
    def openOrderBookDialog(self):
        obd = OrderBookDialog(self)
        obd.exec_()

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
    def internetUp(self):
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

        return connected

    # Gets public market data from Gemini
    ############################################################################
    def marketDataLoop(self):
        while True:
            if not self.hasConnection:
                continue
            else:
                # Update market data
                self.marketData.updateTickers()

                # Update ticker labels
                self.updateTickerGui()

            # Wait
            time.sleep(5)

    # Receive trade history from Gemini
    ############################################################################
    def getTradeHistory(self):
        baseUrl = 'https://api.gemini.com/v1/trades/'

        # Time stamp for yesterday to receive trades from past 24h
        date24h = date.today() - timedelta(1)
        date24h = date24h.strftime('%s')

        # Get BTCUSD trades
        response = requests.request("GET", baseUrl+"btcusd?since=%s" % date24h)
        print(response.text)

    # Receive balances from Gemini
    ############################################################################
    def getBalances(self):
        baseUrl = 'https://api.gemini.com/v1/balances'
        nonce = int(round(time.time()*1000))
        apiKey = self.account.get('apiKey')
        secret = self.account.get('secretKey')
        request = '/v1/balances'

        payload = {'request': request, 'nonce': nonce}
        b64 = base64.b64encode(str.encode(json.dumps(payload)))

        signature = hmac.new(str.encode(secret), b64, hashlib.sha384).hexdigest()

        headers = {
            'Content-Type': "text/plain",
            'Content-Length': "0",
            'X-GEMINI-APIKEY': apiKey,
            'X-GEMINI-PAYLOAD': b64,
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", baseUrl, headers=headers)
        self.balances = json.loads(response.text)

        self.updateBalanceGui()

    # Updates the ticker labels
    ############################################################################
    def updateTickerGui(self):
        if not self.marketData.tickers[0]['last']:
            return
        if not self.marketData.tickers[1]['last']:
            return

        self.btcLastPriceLabel.setText('$'+self.marketData.tickers[0]['last'])
        self.ethLastPriceLabel.setText('$'+self.marketData.tickers[1]['last'])

    # Updates balance labels
    ############################################################################
    def updateBalanceGui(self):
        for item in self.balances:
            # Error
            if item == 'result':
                return

            if item['currency'] == 'BTC':
                self.btcBalanceLabel.setText(item['amount']+' BTC')
                self.btcAvailableLabel.setText(item['available']+' BTC')
            elif item['currency'] == 'USD':
                self.usdBalanceLabel.setText('$'+item['amount'])
                self.usdAvailableLabel.setText('$'+item['available'])
            elif item['currency'] == 'ETH':
                self.ethBalanceLabel.setText(item['amount']+' ETH')
                self.ethAvailableLabel.setText(item['available']+' ETH')

        self.statusBar.showMessage('Balances updated.')
