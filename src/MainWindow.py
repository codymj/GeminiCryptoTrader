################################################################################
#                                                                              #
#  MainWindow.py                                                               #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from ui_MainWindow import Ui_MainWindow
from SetupDialog import SetupDialog
from BuyDialog import BuyDialog
from SellDialog import SellDialog
from ConditionalDialog import ConditionalDialog
from GenDepositAddrDialog import GenDepositAddrDialog

class MainWindow(QtWidgets.QMainWindow):
    # Initializer
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    # Initialize UI
    def initUI(self):
        ui = Ui_MainWindow()
        ui.setupUi(self)

        # Connect actions
        ui.setupAction.triggered.connect(self.openSetupDialog)
        ui.buyAction.triggered.connect(self.openBuyDialog)
        ui.sellAction.triggered.connect(self.openSellDialog)
        ui.conditionalAction.triggered.connect(self.openConditionalDialog)
        ui.genDepositAction.triggered.connect(self.openGenDepositAddrDialog)
        ui.exitAction.triggered.connect(self.close)

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
