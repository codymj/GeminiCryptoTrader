################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, icons, urllib, datetime
import threading, requests, base64, hmac, time
from datetime import datetime
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
from GeminiPublicAPI import Ticker
from CryptoCompareAPI import TradeHistory
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Class data
    accounts = []           # List of accounts
    account = {}            # Current account
    accountsDir = ''        # Path of Accounts file
    settings = {}           # Loaded settings
    settingsDir = ''        # Path of Settings file
    password = ''           # Password in plaintext (never saved)
    hasConnection = False   # Internet connection detected
    tickerThread = None     # Thread for updating tickers
    plotThread = None       # Thread for updating plots
    balances = []           # List of balance info from Gemini
    btcusdPlotData = []     # Trade history for btcusd
    ethusdPlotData = []     # Trade history for ethusd

    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

        # Create graph widgets
        self.btcFigure = plt.figure()
        self.btcCanvas = FigureCanvas(self.btcFigure)
        self.ethFigure = plt.figure()
        self.ethCanvas = FigureCanvas(self.ethFigure)
        self.btcLayout.addWidget(self.btcCanvas)
        self.ethLayout.addWidget(self.ethCanvas)


        self.startUp()

        # Start threads
        self.tickerThread.start()
        self.plotThread.start()

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
        #self.connectButton.clicked.connect(self.getTradeHistory)

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
        else:
            self.hasConnection = False
            self.statusBar.showMessage('No internet connection detected.')

        # Build threads
        self.tickerThread = threading.Thread(target=self.tickerLoop, args=())
        self.tickerThread.daemon = True
        self.plotThread = threading.Thread(target=self.plotLoop, args=())
        self.plotThread.daemon = True

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
    def tickerLoop(self):
        while True:
            if not self.hasConnection:
                continue
            else:
                ticker = Ticker()
                btcusdTicker, ethusdTicker = ticker.getData()
                self.updateTickerGui(btcusdTicker, ethusdTicker)

            # Wait 15 seconds
            time.sleep(15)

    # Gets trade data from CryptoCompare
    ############################################################################
    def plotLoop(self):
        while True:
            if not self.hasConnection:
                continue
            else:
                tradeHistory = TradeHistory()
                btcusdTuple, ethusdTuple = tradeHistory.getData()
                self.updatePlots(btcusdTuple, ethusdTuple)

            # Wait 15 seconds
            time.sleep(15)

    # Updates plots for trade history
    ############################################################################
    def updatePlots(self, btcusdTuple, ethusdTuple):
        # times = [0], closes = [1], range = [2], delta = [3]

        # Update range and delta
        self.btcDeltaLabel.setText(btcusdTuple[2])
        self.btcRangeLabel.setText(btcusdTuple[3])
        self.ethDeltaLabel.setText(ethusdTuple[2])
        self.ethRangeLabel.setText(ethusdTuple[3])

        # Clear plot for new data
        self.btcFigure.clear()
        self.ethFigure.clear()

        # Add axis
        btcAx = self.btcFigure.add_subplot(111)
        ethAx = self.ethFigure.add_subplot(111)

        # Customize axis
        btcXTicks = btcusdTuple[0][::240]
        btcXTicks = [
            datetime.fromtimestamp(i).strftime('%H:%M') for i in btcXTicks]
        ethXTicks = ethusdTuple[0][::240]
        ethXTicks = [
            datetime.fromtimestamp(i).strftime('%H:%M') for i in ethXTicks]

        btcAx.xaxis.grid(b=None, which='major', linestyle=':')
        btcAx.yaxis.grid(b=None, which='major', linestyle=':')
        ethAx.xaxis.grid(b=None, which='major', linestyle=':')
        ethAx.yaxis.grid(b=None, which='major', linestyle=':')

        btcAx.set_xticklabels(btcXTicks)
        ethAx.set_xticklabels(ethXTicks)

        # Plot data
        btcAx.plot(btcusdTuple[0], btcusdTuple[1], '-', color='k', linewidth=1)
        ethAx.plot(ethusdTuple[0], ethusdTuple[1], '-', color='k', linewidth=1)

        # Refresh
        self.btcCanvas.draw()
        self.ethCanvas.draw()

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

        signature = hmac.new(str.encode(secret),
            b64, hashlib.sha384).hexdigest()

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
    def updateTickerGui(self, btcusdTicker, ethusdTicker):
        if not btcusdTicker['last']:
            return
        if not ethusdTicker['last']:
            return

        self.btcLastPriceLabel.setText('$' + btcusdTicker['last'])
        self.ethLastPriceLabel.setText('$' + ethusdTicker['last'])

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
