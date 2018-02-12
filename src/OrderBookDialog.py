################################################################################
#                                                                              #
#  OrderBookDialog.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, websocket, threading, time, asyncio
from websocket import create_connection
from ui_OrderBookDialog import Ui_OrderBookDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

class OrderBookDialog(QtWidgets.QDialog, Ui_OrderBookDialog):
    # Class data
    btcusdThread = None # Thread for updating btcusd data
    ethusdThread = None # Thread for updating ethusd data
    ethbtcThread = None # Thread for updating ethbtc data
    baseUrl = 'wss://api.gemini.com/v1/marketdata/'
    btcusdData = {}     # Data received
    ethusdData = {}     # Data received
    ethbtcData = {}     # Data received
    currentTabIndex = 0 # Current tab viewed
    btcusdRowCount = 0  # Row count for btcusdTable
    ethusdRowCount = 0  # Row count for ethusdTable
    ethbtcRowCount = 0  # Row count for ethbtcTable

    # Initializer
    def __init__(self, parent):
        super(OrderBookDialog, self).__init__(parent)
        self.initUI()
        self.buildThreads()
        self.startThreads()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)
        self.setHeaderLabels()

        # Connect actions
        self.closeButton.clicked.connect(self.close)

    # Set header labels
    ############################################################################
    def setHeaderLabels(self):
        btcusdHeaders = ['Price (USD)', 'Quantity (BTC)',
        'CML Quantity (BTC)', 'Notional (USD)']
        ethusdHeaders = ['Price (USD)', 'Quantity (ETH)',
        'CML Quantity (ETH)', 'Notional (USD)']
        ethbtcHeaders = ['Price (BTC)', 'Quantity (ETH)',
        'CML Quantity (ETH)', 'Notional (BTC)']

        self.btcusdTable.setHorizontalHeaderLabels(btcusdHeaders)
        self.ethusdTable.setHorizontalHeaderLabels(ethusdHeaders)
        self.ethbtcTable.setHorizontalHeaderLabels(ethbtcHeaders)

    # Build threads
    ############################################################################
    def buildThreads(self):
        btcusdLoop = asyncio.new_event_loop()
        self.btcusdThread = threading.Thread(target=self.btcusdWorker, args=(btcusdLoop,))
        self.btcusdThread.daemon = True

        ethusdLoop = asyncio.new_event_loop()
        self.ethusdThread = threading.Thread(target=self.ethusdWorker, args=(ethusdLoop,))
        self.ethusdThread.daemon = True

        ethbtcLoop = asyncio.new_event_loop()
        self.ethbtcThread = threading.Thread(target=self.ethbtcWorker, args=(ethbtcLoop,))
        self.ethbtcThread.daemon = True

    # Start threads
    ############################################################################
    def startThreads(self):
        self.btcusdThread.start()
        self.ethusdThread.start()
        self.ethbtcThread.start()

    # Worker
    ############################################################################
    def btcusdWorker(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.btcusdDataLoop())

    # Worker
    ############################################################################
    def ethusdWorker(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.ethusdDataLoop())

    # Worker
    ############################################################################
    def ethbtcWorker(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.ethbtcDataLoop())

    # Data loop for getting btcusd data
    ############################################################################
    def btcusdDataLoop(self):
        btcusdSocket = create_connection(self.baseUrl+'BTCUSD')
        while True:
            response = btcusdSocket.recv()
            self.btcusdData = json.loads(response)
            self.updateOrderBook()
            time.sleep(5)

    # Data loop for getting ethusd data
    ############################################################################
    def ethusdDataLoop(self):
        ethusdSocket = create_connection(self.baseUrl+'ETHUSD')
        while True:
            response = ethusdSocket.recv()
            self.ethusdData = json.loads(response)
            self.updateOrderBook()
            time.sleep(5)

    # Data loop for getting ethbtc data
    ############################################################################
    def ethbtcDataLoop(self):
        ethbtcSocket = create_connection(self.baseUrl+'ETHBTC')
        while True:
            response = ethbtcSocket.recv()
            self.ethbtcData = json.loads(response)
            self.updateOrderBook()
            time.sleep(5)

    # Update the order book depending on which tab is currently viewed
    ############################################################################
    def updateOrderBook(self):
        currentTabIndex = self.orderBookTabs.currentIndex()

        if currentTabIndex == 0:   # Update BTCUSD
            if self.btcusdData['type'] == 'update':
                for item in self.btcusdData['events']:
                    if item['type'] == 'change':
                        # Need to search table here for same price items later
                        itemPrice = QTableWidgetItem(item['price'])
                        itemRemaining = QTableWidgetItem(item['remaining'])
                        self.btcusdTable.setItem(0, 0, itemPrice)
                        self.btcusdTable.setItem(0, 1, itemRemaining)
            return
        elif currentTabIndex == 1: # Update ETHUSD
            if self.ethusdData['type'] == 'update':
                for item in self.ethusdData['events']:
                    if item['type'] == 'change':
                        # Need to search table here for same price items later
                        itemPrice = QTableWidgetItem(item['price'])
                        itemRemaining = QTableWidgetItem(item['remaining'])
                        self.ethusdTable.setItem(0, 0, itemPrice)
                        self.ethusdTable.setItem(0, 1, itemRemaining)
            return
        elif currentTabIndex == 2: # Update ETHBTC
            if self.ethbtcData['type'] == 'update':
                for item in self.ethbtcData['events']:
                    if item['type'] == 'change':
                        # Need to search table here for same price items later
                        itemPrice = QTableWidgetItem(item['price'])
                        itemRemaining = QTableWidgetItem(item['remaining'])
                        self.ethbtcTable.setItem(0, 0, itemPrice)
                        self.ethbtcTable.setItem(0, 1, itemRemaining)
            return
