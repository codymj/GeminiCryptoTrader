################################################################################
#                                                                              #
#  OrderBookDialog.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, websocket, threading, time, asyncio, itertools
from websocket import create_connection
from ui_OrderBookDialog import Ui_OrderBookDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import pyqtSlot, QModelIndex

class OrderBookDialog(QtWidgets.QDialog, Ui_OrderBookDialog):
    # Class data
    btcusdThread = None     # Thread for updating btcusd data
    ethusdThread = None     # Thread for updating ethusd data
    ethbtcThread = None     # Thread for updating ethbtc data
    baseUrl = 'wss://api.gemini.com/v1/marketdata/'
    btcusdData = {}         # Data received
    ethusdData = {}         # Data received
    ethbtcData = {}         # Data received
    btcusdItems = []        # List of btcusd items parsed for table
    btcusdModel = None      # Model for displaying btcusd data
    btcusdModelIndex = None # Model index for centering data around spread
    btcusdList = []         # String list for model
    ethusdItems = []        # List of btcusd items parsed for table
    ethbtcItems = []        # List of ethusd items parsed for table

    # Initializer
    def __init__(self, parent):
        super(OrderBookDialog, self).__init__(parent)
        self.initUI()
        #self.buildThreads()
        #self.startThreads()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)
        self.btcusdModel = QStandardItemModel(self.btcusdListView)
        self.btcusdModelIndex = QModelIndex()
        self.btcusdListView.setModel(self.btcusdModel)

        # Connect actions
        self.updateButton.clicked.connect(self.doUpdate)
        self.closeButton.clicked.connect(self.close)

    # Build threads
    ############################################################################
    #def buildThreads(self):
        #btcusdLoop = asyncio.new_event_loop()
        #self.btcusdThread = threading.Thread(target=self.btcusdWorker,
            #args=(btcusdLoop,))
        #self.btcusdThread.daemon = True

        # ethusdLoop = asyncio.new_event_loop()
        # self.ethusdThread = threading.Thread(target=self.ethusdWorker,
            # args=(ethusdLoop,))
        # self.ethusdThread.daemon = True

        # ethbtcLoop = asyncio.new_event_loop()
        # self.ethbtcThread = threading.Thread(target=self.ethbtcWorker,
            # args=(ethbtcLoop,))
        # self.ethbtcThread.daemon = True

    # Start threads
    ############################################################################
    #def startThreads(self):
        #self.btcusdThread.start()
        #self.ethusdThread.start()
        #self.ethbtcThread.start()

    # Worker
    ############################################################################
    #def btcusdWorker(self, loop):
        #asyncio.set_event_loop(loop)
        #loop.run_until_complete(self.btcusdGetData())

    # Worker
    ############################################################################
    #def ethusdWorker(self, loop):
        #asyncio.set_event_loop(loop)
        #loop.run_until_complete(self.ethusdGetData())

    # Worker
    ############################################################################
    #def ethbtcWorker(self, loop):
        #asyncio.set_event_loop(loop)
        #loop.run_until_complete(self.ethbtcGetData())

    # Start update process
    ############################################################################
    def doUpdate(self):
        if self.orderBookTabs.currentIndex() == 0:
            self.updateButton.setEnabled(False)
            self.updateButton.setText('Updating...')
            self.btcusdGetData()
        elif self.orderBookTabs.currentIndex() == 1:
            return
        else:
            return

    # Data loop for getting btcusd data
    ############################################################################
    def btcusdGetData(self):
        btcusdSocket = create_connection(self.baseUrl+'BTCUSD')
        response = btcusdSocket.recv()
        self.btcusdData = json.loads(response)
        self.parseEvents()

    # Data loop for getting ethusd data
    ############################################################################
    def ethusdGetData(self):
        ethusdSocket = create_connection(self.baseUrl+'ETHUSD')
        response = ethusdSocket.recv()
        self.ethusdData = json.loads(response)
        self.parseEvents()

    # Data loop for getting ethbtc data
    ############################################################################
    def ethbtcGetData(self):
        ethbtcSocket = create_connection(self.baseUrl+'ETHBTC')
        response = ethbtcSocket.recv()
        self.ethbtcData = json.loads(response)
        self.parseEvents()

    # Updates remainders by price
    ############################################################################
    def updateData(self):
        # BTCUSD
        if self.orderBookTabs.currentIndex() == 0:
            # If no data, return
            if not self.btcusdData:
                return
            # Clear items for update
            self.btcusdItems.clear()
            # If data received is an update
            if self.btcusdData.get('type') == 'update':
                # Loop through new event data
                for event in self.btcusdData.get('events'):
                    # Parse new events
                    self.btcusdItems.append(event)
        # ETHUSD
        elif self.orderBookTabs.currentIndex() == 1:
            return
        # ETHBTC
        else:
            return

    # Return list of 'ask' items
    ############################################################################
    def separateAskBidItems(self):
        askItems = []
        bidItems = []

        # BTCUSD
        if self.orderBookTabs.currentIndex() == 0:
            # Separate
            for item in self.btcusdItems:
                if item.get('side') == 'ask':
                    askItems.append(item)
                elif item.get('side') == 'bid':
                    bidItems.append(item)
                else:
                    continue
            # Sort
            askItems.sort(key=lambda k: float(k.get('price')))
            bidItems.sort(key=lambda k: float(k.get('price')), reverse=True)
            # Return
            return askItems, bidItems
            # ETHUSD
        elif self.orderBookTabs.currentIndex() == 1:
            return
        # ETHBTC
        else:
            return

    # Calculates table cutoff values
    ############################################################################
    def calcCutoffs(self, askItems, bidItems):
        # n trades showing on both sides of spread
        cutoff = 50

        # Get spread
        minAsk = float(askItems[0].get('price'))
        maxBid = float(bidItems[0].get('price'))
        spread = minAsk - maxBid

        # Create cutoffs
        askCutoffItems = askItems[cutoff:]
        bidCutoffItems = bidItems[cutoff:]

        # Update visible table items
        askItems = askItems[:cutoff]
        askItems.sort(key=lambda k: float(k.get('price')), reverse=True)
        bidItems = bidItems[:cutoff]
        bidItems.sort(key=lambda k: float(k.get('price')), reverse=True)

        # Return
        return askItems, askCutoffItems, bidItems, bidCutoffItems, spread

    # Parses events from Gemini
    ############################################################################
    def parseEvents(self):
        # Update data
        self.updateData()

        # Separate asks and bids
        askItems, bidItems = self.separateAskBidItems()

        # Calculate cutoffs and spread
        tupledItems = self.calcCutoffs(askItems, bidItems)

        # Update the order book table
        self.updateOrderBook(tupledItems)

    # Generates string for data model
    ############################################################################
    def formatItem(self, json):
        priceStr = json.get('price')
        remainStr = json.get('remaining')

        width = 15
        priceStr = "{0:<{1}}".format(priceStr[:width], width)
        priceStr.ljust(width)
        remainStr = "{0:<{1}}".format(remainStr[:width], width)
        remainStr.ljust(width)

        item = QStandardItem()
        s = priceStr + remainStr
        item.setText(s)
        return item

    # Update the order book depending on which tab is currently viewed
    ############################################################################
    def updateOrderBook(self, tupledItems):
        cutoff = 50
        self.btcusdModelIndex = self.btcusdModel.createIndex(cutoff + 1, 0)
        askItems, askCutoffItems, bidItems, bidCutoffItems, spread = tupledItems

        # Generate ask cutoff JSON object
        askCutoffSum = 0.0
        for item in askCutoffItems:
            askCutoffSum = askCutoffSum + float(item.get('remaining'))
        askCutoffJson = {'price': '>' + askItems[0].get('price'),
                         'remaining': str(askCutoffSum)}
        # Generate bid cutoff JSON object
        bidCutoffSum = 0.0
        for item in bidCutoffItems:
            bidCutoffSum = bidCutoffSum + float(item.get('remaining'))
        bidCutoffJson = {'price': '<' + bidItems[-1].get('price'),
                         'remaining': str(bidCutoffSum)}
        # Generate spread JSON object
        spreadJson = {'price': str("%.2f" % round(spread, 2)),
                      'remaining': 'SPREAD'}

        # BTCUSD
        if self.orderBookTabs.currentIndex() == 0:
            # Clear model's string list
            self.btcusdModel.clear()
            # Insert ask cutoff items
            self.btcusdModel.appendRow(self.formatItem(askCutoffJson))
            # Insert ask items
            for item in askItems:
                self.btcusdModel.appendRow(self.formatItem(item))
            # Insert spread item
            self.btcusdModel.appendRow(self.formatItem(spreadJson))
            # Insert bid items
            for item in bidItems:
                self.btcusdModel.appendRow(self.formatItem(item))
            # Insert bid cutoff item
            self.btcusdModel.appendRow(self.formatItem(bidCutoffJson))
            # Scroll to spread
            self.btcusdListView.setCurrentIndex(self.btcusdModelIndex)
            self.btcusdListView.scrollTo(self.btcusdModelIndex, 3)
            self.updateButton.setText('&Update')
            self.updateButton.setEnabled(True)
        # ETHUSD
        elif self.orderBookTabs.currentIndex() == 1:
            return
        # ETHBTC
        else:
            return
