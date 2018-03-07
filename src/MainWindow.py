################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path, urllib, datetime, threading, time, websocket
import resources
from datetime import datetime as dt
from urllib.request import urlopen
from urllib.error import URLError
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QFontDatabase
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal
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
from EncryptDecryptData import *
from LoadSaveData import *
from GeminiPublicAPI import *
from GeminiPrivateAPI import *
from CryptoCompareAPI import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.dates as md

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Create signals
    netStatusSignal = pyqtSignal(bool)

    # Class data
    connectIcon = None      # QPixmap for connection icon in status bar
    connectIconLabel = None # Label for QPixmap
    accounts = []           # List of accounts
    account = {}            # Current account
    accountsPath = ''       # Path of Accounts file
    settings = {}           # Loaded settings
    settingsPath = ''       # Path of Settings file
    password = ''           # Password in plaintext (never saved)
    internetUp = False      # Internet connection status
    connected = False       # True if connected to Gemini exchange
    tickerThread = None     # Thread for updating tickers
    plotThread = None       # Thread for updating plots
    tradesThread = None     # Thread for updating trades
    balancesThread = None   # Thread for updating balances
    tradesModel = None      # Item model for tradesListView

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
        self.internetThread.start()
        self.tickerThread.start()
        self.plotThread.start()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Set fixed-width font for list views
        fixedFont = QFontDatabase.systemFont(1)
        self.tradesListView.setFont(fixedFont)

        # Setup models
        self.tradesModel = QStandardItemModel(self.tradesListView)
        self.tradesListView.setModel(self.tradesModel)

        # Status Bar
        self.statusBar.showMessage('Gemini CryptoTrader started...')

        # Set connectivity icon in status bar
        self.connectIcon = QPixmap(':/red-circle.png')
        self.connectIconLabel = QLabel(self)
        self.connectIconLabel.setPixmap(self.connectIcon)
        self.statusBar.addPermanentWidget(self.connectIconLabel)

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

        # Connect buttons
        self.connectButton.clicked.connect(self.startPrivateThreads)

        # Connect custom signals
        self.netStatusSignal.connect(self.updateInternetStatus)

    # Run start up processes
    ############################################################################
    def startUp(self):
        # Load settings
        self.settings, self.settingsPath = loadSettings()
        if self.settings['encrypted']:
            self.openPasswordDialog()

        # Load accounts, last used account and update enabled actions
        self.accounts, self.accountsPath = loadAccounts(self.settings, self.password)
        if self.accounts:
            self.account = getLastUsedAccount(self.accounts)
        self.updateEnabledActions()

        # Build threads
        self.internetThread = threading.Thread(target=self.checkInternet, args=())
        self.internetThread.daemon = True
        self.tickerThread = threading.Thread(target=self.tickerLoop, args=())
        self.tickerThread.daemon = True
        self.plotThread = threading.Thread(target=self.plotLoop, args=())
        self.plotThread.daemon = True
        self.tradesThread = threading.Thread(target=self.tradesLoop, args=())
        self.tradesThread.daemon = True
        self.balancesThread = threading.Thread(target=self.balancesLoop, args=())
        self.balancesThread.daemon = True

    # Starts private threads
    ############################################################################
    def startPrivateThreads(self):
        if self.internetUp:
            self.tradesThread.start()
            self.balancesThread.start()
        else:
            print('No internet detected. Check connection.')

    # When user closes program, save all data & encrypt if necessary
    ############################################################################
    def closeEvent(self, event):
        # Save data
        self.statusBar.showMessage('Saving data...')
        saveAccounts(self.accounts, self.accountsPath, self.settings, self.password)
        saveSettings(self.settings, self.settingsPath)

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
            self.connectButton.setEnabled(False)
            self.disconnectButton.setEnabled(False)
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
        if self.settings['encrypted']:
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
            self.settings = psd.getSettings()

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
        ad = AccountsDialog(self, self.accounts, self.settings)
        if ad.exec_():
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

    # Opens options dialog
    ############################################################################
    @pyqtSlot()
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
    def checkInternet(self):
        while True:
            status = False
            try:
                urlopen('http://74.125.21.99', timeout=1)
                status = True
            except URLError as err:
                status = False

            self.netStatusSignal.emit(status)
            time.sleep(5)

    # Updates internet status
    ############################################################################
    def updateInternetStatus(self, status):
        if status and self.connected:
            self.connectIcon = QPixmap(':/green-circle.png')
        elif status and not self.connected:
            self.connectIcon = QPixmap(':/orange-circle.png')
        else:
            self.connectIcon = QPixmap(':/red-circle.png')
            self.statusBar.showMessage('No internet connection detected.')

            # Clear data from main window
            self.clearAllData()

        self.connectIconLabel.setPixmap(self.connectIcon)

        self.internetUp = status

    # Clears all GUI data from main window
    ############################################################################
    def clearAllData(self):
        # Plots
        self.btcFigure.clear()
        self.ethFigure.clear()

        # Ticker
        self.btcLastPriceLabel.setText('')
        self.btcDeltaLabel.setText('')
        self.btcRangeLabel.setText('')
        self.ethLastPriceLabel.setText('')
        self.ethDeltaLabel.setText('')
        self.ethRangeLabel.setText('')

        # Balances
        self.usdBalanceLabel.setText('')
        self.btcBalanceLabel.setText('')
        self.ethBalanceLabel.setText('')

        # Available for trading
        self.usdAvailableLabel.setText('')
        self.btcAvailableLabel.setText('')
        self.ethAvailableLabel.setText('')

        # Clear list view models
        self.tradesModel.clear()


    # Gets public market data from Gemini
    ############################################################################
    def tickerLoop(self):
        while True:
            if self.internetUp:
                tickerList = GeminiPublicAPI().getTickers()
                self.updateTickerGui(tickerList)
            else:
                continue

            time.sleep(15)

    # Gets trade data from CryptoCompare
    ############################################################################
    def plotLoop(self):
        while True:
            if self.internetUp:
                tupleList = CryptoCompareAPI().getTradeHistory()
                self.updatePlots(tupleList)
            else:
                continue

            time.sleep(15)

    # Gets user trades from Gemini
    ############################################################################
    def tradesLoop(self):
        while True:
            trades = GeminiPrivateAPI(self.account).getTrades('btcusd')

            if isinstance(trades, list):
                self.connected = True
            else:
                self.connected = False

            self.updateTradeGUI(trades)
            time.sleep(15)

    # Gets user balance and available for trade
    ############################################################################
    def balancesLoop(self):
        while True:
            balances = GeminiPrivateAPI(self.account).getBalances()
            self.updateBalanceGui(balances)
            time.sleep(15)

    # Updates plots for trade history
    ############################################################################
    def updatePlots(self, tupleList):
        # times = [0], closes = [1], range = [2], delta = [3]

        btcusdTuple = tupleList[0]
        ethusdTuple = tupleList[1]

        # Update range and delta
        self.btcRangeLabel.setText(btcusdTuple[2])
        self.btcDeltaLabel.setText(btcusdTuple[3])
        self.ethRangeLabel.setText(ethusdTuple[2])
        self.ethDeltaLabel.setText(ethusdTuple[3])

        # Clear plot for new data
        self.btcFigure.clear()
        self.ethFigure.clear()

        # Add axis
        btcAx = self.btcFigure.add_subplot(111)
        ethAx = self.ethFigure.add_subplot(111)

        # Customize axis
        btcAx.xaxis.grid(b=None, which='major', linestyle=':')
        btcAx.yaxis.grid(b=None, which='major', linestyle=':')
        ethAx.xaxis.grid(b=None, which='major', linestyle=':')
        ethAx.yaxis.grid(b=None, which='major', linestyle=':')

        btcXTicks = [dt.fromtimestamp(i) for i in btcusdTuple[0]]
        ethXTicks = [dt.fromtimestamp(i) for i in ethusdTuple[0]]

        xfmt = md.DateFormatter('%H:%M')
        btcAx.xaxis.set_major_formatter(xfmt)
        ethAx.xaxis.set_major_formatter(xfmt)
        xloc = md.HourLocator(interval=4)
        btcAx.xaxis.set_major_locator(xloc)
        ethAx.xaxis.set_major_locator(xloc)

        # Plot data
        btcAx.plot(btcXTicks, btcusdTuple[1], '-', color='k', linewidth=1)
        ethAx.plot(ethXTicks, ethusdTuple[1], '-', color='k', linewidth=1)

        # Refresh
        self.btcCanvas.draw()
        self.ethCanvas.draw()

    # Updates trades in trades list view
    ############################################################################
    def updateTradeGUI(self, trades):
        sList = []
        width = 15

        self.tradesModel.clear()

        orderID = 'Order ID'
        orderID = "{0:<{1}}".format(orderID[:width], width)

        tradeType = 'Type'
        tradeType = "{0:<{1}}".format(tradeType[:7], 7)

        time = 'Date + Time'
        time = "{0:<{1}}".format(time[:25], 25)

        amount = 'Amount'
        amount = "{0:<{1}}".format(amount[:width], width)

        price = 'Price'
        price = "{0:<{1}}".format(price[:width], width)

        fee = 'Fee'
        fee = "{0:<{1}}".format(fee[:5], 5)

        s = orderID + tradeType + time + amount + price + fee
        sList.append(s)
        hline = '-' * 87
        sList.append(hline)

        for trade in trades:
            orderID = "{0:<{1}}".format(str(trade.get('order_id'))[:width], width)
            orderID.ljust(width)

            tradeType = "{0:<{1}}".format(str(trade.get('type'))[:7], 7)
            tradeType.ljust(7)

            time = trade.get('timestampms')
            time = dt.fromtimestamp(time/1000.0).strftime("%Y-%m-%d %H:%M:%S")
            time = "{0:<{1}}".format(str(time)[:25], 25)
            time.ljust(25)

            amount = "{0:<{1}}".format(str(trade.get('amount'))[:width], width)
            amount.ljust(width)

            price = str('$' + '%.2f' % float(trade.get('price')))
            price = "{0:<{1}}".format(price[:width], width)
            price.ljust(width)

            if trade.get('fee_currency') == 'USD':
                fee = str('$' + '%.2f' % float(trade.get('fee_amount')))
                fee = "{0:<{1}}".format(fee[:5], 5)
                fee.ljust(5)
            else:
                fee = "{0:<{1}}".format(str(trade.get('fee'))[:width], width)
                fee.ljust(width)

            s = orderID + tradeType + time + amount + price + fee
            sList.append(s)

        for s in sList:
            item = QStandardItem()
            item.setText(s)
            self.tradesModel.appendRow(item)

    # Updates the ticker labels
    ############################################################################
    def updateTickerGui(self, tickerList):
        # Make sure there are ticker values for last price
        for ticker in tickerList:
            if not ticker['last']:
                return

        self.btcLastPriceLabel.setText('$' + tickerList[0]['last'])
        self.ethLastPriceLabel.setText('$' + tickerList[1]['last'])

    # Updates balance labels
    ############################################################################
    def updateBalanceGui(self, balances):
        # Handle error which is returned as a string from Gemini
        if isinstance(balances, str):
            msg = QMessageBox()
            msg.setText(balances)
            msg.exec()
            return

        # Update balances
        for item in balances:
            if item['currency'] == 'BTC':
                self.btcBalanceLabel.setText(item['amount'])
                self.btcAvailableLabel.setText(item['available'])
            elif item['currency'] == 'USD':
                self.usdBalanceLabel.setText('$'+item['amount'])
                self.usdAvailableLabel.setText('$'+item['available'])
            elif item['currency'] == 'ETH':
                self.ethBalanceLabel.setText(item['amount'])
                self.ethAvailableLabel.setText(item['available'])
