################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
import icons
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow import Ui_MainWindow
from SetupDialog import SetupDialog
from BuyDialog import BuyDialog
from SellDialog import SellDialog
from ConditionalDialog import ConditionalDialog
from GenDepositAddrDialog import GenDepositAddrDialog
from WithdrawToDialog import WithdrawToDialog

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    # Initialize UI
    def initUI(self):
        self.setupUi(self)

        # Status Bar
        self.statusBar.showMessage('Gemini CryptoTrader started...', msecs=3000)

        self.dataIconLabel = QLabel(self)
        self.dataIconPM = QPixmap(':/red-circle.png')
        self.dataIconLabel.setPixmap(self.dataIconPM)
        self.dataIconLabel.setToolTip('Flashes when data is received')
        self.statusBar.addPermanentWidget(self.dataIconLabel)

        self.connectIconLabel = QLabel(self)
        self.connectIconPM = QPixmap(':/red-circle.png')
        self.connectIconLabel.setPixmap(self.connectIconPM)
        self.statusBar.setToolTip('Green when connected to exchange')
        self.statusBar.addPermanentWidget(self.connectIconLabel)

        # Connect actions
        self.setupAction.triggered.connect(self.openSetupDialog)
        self.buyAction.triggered.connect(self.openBuyDialog)
        self.sellAction.triggered.connect(self.openSellDialog)
        self.conditionalAction.triggered.connect(self.openConditionalDialog)
        self.genDepositAction.triggered.connect(self.openGenDepositAddrDialog)
        self.withdrawToAction.triggered.connect(self.openWithdrawToDialog)
        self.exitAction.triggered.connect(self.close)

    # Slots
    @pyqtSlot()
    def openSetupDialog(self):
        sd = SetupDialog(self)
        sd.show()
    @pyqtSlot()
    def openBuyDialog(self):
        bd = BuyDialog(self)
        bd.show()
    @pyqtSlot()
    def openSellDialog(self):
        sd = SellDialog(self)
        sd.show()
    @pyqtSlot()
    def openConditionalDialog(self):
        cd = ConditionalDialog(self)
        cd.show()
    @pyqtSlot()
    def openGenDepositAddrDialog(self):
        gd = GenDepositAddrDialog(self)
        gd.show()
    @pyqtSlot()
    def openWithdrawToDialog(self):
        wd = WithdrawToDialog(self)
        wd.show()
