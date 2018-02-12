################################################################################
#                                                                              #
#  OrderBookDialog.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from ui_OrderBookDialog import Ui_OrderBookDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class OrderBookDialog(QtWidgets.QDialog, Ui_OrderBookDialog):
    # Initializer
    def __init__(self, parent):
        super(OrderBookDialog, self).__init__(parent)
        self.initUI()

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
