################################################################################
#                                                                              #
#  OrderBookDialog.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, threading, time, urllib
from urllib.request import urlopen
from ui_OrderBookDialog import Ui_OrderBookDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFontDatabase
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QModelIndex, QThread, QObject

class Worker(QObject):
    baseUrl = 'https://api.gemini.com/v1/book/'
    nAsks = None                            # Number of ask trades to retrieve
    nBids = None                            # Number of bid trades to retrieve
    flag = None                             # 'BTCUSD', 'ETHUSD', 'ETHBTC'
    cutoff = None                           # Number of asks and bids to display
    width = None                            # Width of data fields
    data = {}                               # Data received
    stringList = []                         # Data strings for QListView
    stopWorking = False                     # Flag to stop work
    dataReady = pyqtSignal(str, list)       # Signal GUI update

    # Initializer
    def __init__(self, flag, cutoff=9, width=15, nAsks=200, nBids=200):
        super(QObject, self).__init__()
        self.flag = flag
        self.cutoff = cutoff
        self.width = width
        self.nAsks = nAsks
        self.nBids = nBids

    # Stops working
    ############################################################################
    def stopWork(self):
        self.stopWorking = True

    # Run function
    ############################################################################
    @pyqtSlot()
    def work(self):
        while True:
            if self.stopWorking:
                print('Exiting thread')
                break
            print('Getting '+self.flag+' data')
            self.getData()
            askList, bidList = self.parseData()
            tupled = self.computeCutoffs(askList, bidList)
            self.generateStringList(tupled)
            self.dataReady.emit(self.flag, self.stringList)
            if self.stopWorking:
                print('Exiting thread')
                break
            time.sleep(5)

    # Receive JSON data from Gemini
    ############################################################################
    def getData(self):
        paramStr = '?limit_bids='+str(self.nBids)+'&limit_asks='+str(self.nAsks)
        response = urlopen(self.baseUrl+self.flag.lower()+paramStr)
        self.data = json.loads(response.read())

    # Parse JSON data
    ############################################################################
    def parseData(self):
        # If no data, return
        if not self.data:
            return

        askList = self.data.get('asks')
        bidList = self.data.get('bids')
        # Format trailing decimals
        for item in askList:
            item['amount'] = str("%.8f" % float(item['amount']))
        for item in bidList:
            item['amount'] = str("%.8f" % float(item['amount']))

        #return items
        return (askList, bidList)

    # Compute cutoff values
    ############################################################################
    def computeCutoffs(self, askList, bidList):
        # Sort
        askList.sort(key=lambda k: float(k.get('price')))
        bidList.sort(key=lambda k: float(k.get('price')), reverse=True)

        # Get spread
        minAsk = float(askList[0].get('price'))
        maxBid = float(bidList[0].get('price'))
        spread = minAsk - maxBid

        # Create cutoffs
        askCutoffList = askList[self.cutoff:]
        bidCutoffList = bidList[self.cutoff:]

        # Update visible table items
        askList = askList[:self.cutoff]
        askList.sort(key=lambda k: float(k.get('price')), reverse=True)
        bidList = bidList[:self.cutoff]

        return (askList, askCutoffList, bidList, bidCutoffList, spread)

    # Generates string for data model
    ############################################################################
    def formatItemString(self, json):
        # Unformated data strings
        priceStr = json.get('price')
        remainStr = json.get('amount')

        # Format strings
        priceStr = "{0:<{1}}".format(priceStr[:self.width], self.width)
        priceStr.ljust(self.width)
        remainStr = "{0:<{1}}".format(remainStr[:self.width], self.width)
        remainStr.ljust(self.width)
        s = priceStr + remainStr

        return s

    # Generate item list
    ############################################################################
    def generateStringList(self, tupled):
        askList, askCutoffList, bidList, bidCutoffList, spread = tupled

        # Clear string list
        self.stringList.clear()

        # Generate ask cutoff JSON object, format and append to stringList
        askCutoffSum = 0.0
        for item in askCutoffList:
            askCutoffSum = askCutoffSum + float(item.get('amount'))
        askCutoffJson = {'price': '>' + askList[0].get('price'),
                         'amount': str(askCutoffSum)}
        self.stringList.append(self.formatItemString(askCutoffJson))

        # Format and append ask items to stringList
        for item in askList:
            self.stringList.append(self.formatItemString(item))

        # Generate spread JSON object, format and append to stringList
        if (self.flag == 'ETHBTC'):
            spreadJson = {'price': str("%.5f" % spread),
                          'amount': 'SPREAD'}
            self.stringList.append(self.formatItemString(spreadJson))
        else:
            spreadJson = {'price': str("%.2f" % spread),
                          'amount': 'SPREAD'}
            self.stringList.append(self.formatItemString(spreadJson))

        # Format and append bid items to stringList
        for item in bidList:
            self.stringList.append(self.formatItemString(item))

        # Generate bid cutoff JSON object, format and append to stringList
        bidCutoffSum = 0.0
        for item in bidCutoffList:
            bidCutoffSum = bidCutoffSum + float(item.get('amount'))
        bidCutoffJson = {'price': '<' + bidList[-1].get('price'),
                         'amount': str(bidCutoffSum)}
        self.stringList.append(self.formatItemString(bidCutoffJson))


class OrderBookDialog(QtWidgets.QDialog, Ui_OrderBookDialog):
    # Class data
    cutoff = None               # Number of asks and bids to display
    width = None                # Width of data fields
    btcusdWorker = None         # Worker for updating btcusd data
    btcusdThread = QThread()    # Thread for worker
    ethusdWorker = None         # Worker for updating ethusd data
    ethusdThread = QThread()    # Thread for worker
    ethbtcWorker = None         # Worker for updating ethbtc data
    ethbtcThread = QThread()    # Thread for worker
    btcusdModel = None          # Model for displaying btcusd data
    btcusdModelIndex = None     # Model index for centering data around spread
    ethusdModel = None          # Model for displaying ethusd data
    ethusdModelIndex = None     # Model index for centering data around spread
    ethbtcModel = None          # Model for displaying ethbtc data
    ethbtcModelIndex = None     # Model index for centering data around spread

    # Initializer
    def __init__(self, parent, cutoff=9, width=15):
        super(OrderBookDialog, self).__init__(parent)
        self.cutoff = cutoff
        self.width = width
        self.initUI()
        self.buildThreads()
        self.startThreads()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)
        self.btcusdModel = QStandardItemModel(self.btcusdListView)
        self.btcusdModelIndex = QModelIndex()
        self.btcusdModelIndex = self.btcusdModel.createIndex(self.cutoff + 1, 0)
        self.btcusdListView.setModel(self.btcusdModel)
        self.ethusdModel = QStandardItemModel(self.ethusdListView)
        self.ethusdModelIndex = QModelIndex()
        self.ethusdModelIndex = self.ethusdModel.createIndex(self.cutoff + 1, 0)
        self.ethusdListView.setModel(self.ethusdModel)
        self.ethbtcModel = QStandardItemModel(self.ethbtcListView)
        self.ethbtcModelIndex = QModelIndex()
        self.ethbtcModelIndex = self.ethbtcModel.createIndex(self.cutoff + 1, 0)
        self.ethbtcListView.setModel(self.ethbtcModel)

        # Set fixed-width font
        fixedFont = QFontDatabase.systemFont(1)
        self.btcusdListView.setFont(fixedFont)
        self.ethusdListView.setFont(fixedFont)
        self.ethbtcListView.setFont(fixedFont)

        # Connect actions
        self.closeButton.clicked.connect(self.close)

    # Build threads
    ############################################################################
    def buildThreads(self):
        self.btcusdWorker = Worker('BTCUSD', self.cutoff, self.width)
        self.btcusdWorker.moveToThread(self.btcusdThread)
        self.btcusdWorker.dataReady.connect(self.updateGui)
        self.btcusdThread.started.connect(self.btcusdWorker.work)

        self.ethusdWorker = Worker('ETHUSD', self.cutoff, self.width)
        self.ethusdWorker.moveToThread(self.ethusdThread)
        self.ethusdWorker.dataReady.connect(self.updateGui)
        self.ethusdThread.started.connect(self.ethusdWorker.work)

        self.ethbtcWorker = Worker('ETHBTC', self.cutoff, self.width)
        self.ethbtcWorker.moveToThread(self.ethbtcThread)
        self.ethbtcWorker.dataReady.connect(self.updateGui)
        self.ethbtcThread.started.connect(self.ethbtcWorker.work)

    # Start threads
    ############################################################################
    def startThreads(self):
        self.btcusdThread.start()
        self.ethusdThread.start()
        self.ethbtcThread.start()

    # Updates QListViews
    ############################################################################
    @pyqtSlot(str, list)
    def updateGui(self, flag: str, stringList: list):
        if flag == 'BTCUSD':
            self.btcusdModel.clear()
            for string in stringList:
                item = QStandardItem()
                item.setText(string)
                self.btcusdModel.appendRow(item)
            self.btcusdListView.setCurrentIndex(self.btcusdModelIndex)
            self.btcusdListView.scrollTo(self.btcusdModelIndex, 3)
        elif flag == 'ETHUSD':
            self.ethusdModel.clear()
            for string in stringList:
                item = QStandardItem()
                item.setText(string)
                self.ethusdModel.appendRow(item)
            self.ethusdListView.setCurrentIndex(self.ethusdModelIndex)
            self.ethusdListView.scrollTo(self.ethusdModelIndex, 3)
        elif flag == 'ETHBTC':
            self.ethbtcModel.clear()
            for string in stringList:
                item = QStandardItem()
                item.setText(string)
                self.ethbtcModel.appendRow(item)
            self.ethbtcListView.setCurrentIndex(self.ethbtcModelIndex)
            self.ethbtcListView.scrollTo(self.ethbtcModelIndex, 3)

    # When user closes order book, stop threads
    ############################################################################
    def closeEvent(self, event):
        self.btcusdWorker.stopWork()
        self.ethusdWorker.stopWork()
        self.ethbtcWorker.stopWork()
        self.btcusdThread.quit()
        self.ethusdThread.quit()
        self.ethbtcThread.quit()
