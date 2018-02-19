# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrderBookDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OrderBookDialog(object):
    def setupUi(self, OrderBookDialog):
        OrderBookDialog.setObjectName("OrderBookDialog")
        OrderBookDialog.resize(640, 480)
        OrderBookDialog.setMinimumSize(QtCore.QSize(640, 480))
        OrderBookDialog.setMaximumSize(QtCore.QSize(640, 480))
        self.gridLayout_2 = QtWidgets.QGridLayout(OrderBookDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.orderBookTabs = QtWidgets.QTabWidget(OrderBookDialog)
        self.orderBookTabs.setObjectName("orderBookTabs")
        self.btcusdTab = QtWidgets.QWidget()
        self.btcusdTab.setObjectName("btcusdTab")
        self.gridLayout = QtWidgets.QGridLayout(self.btcusdTab)
        self.gridLayout.setObjectName("gridLayout")
        self.btcusdListView = QtWidgets.QListView(self.btcusdTab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.btcusdListView.setFont(font)
        self.btcusdListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.btcusdListView.setDragDropOverwriteMode(False)
        self.btcusdListView.setAlternatingRowColors(True)
        self.btcusdListView.setObjectName("btcusdListView")
        self.gridLayout.addWidget(self.btcusdListView, 0, 0, 1, 1)
        self.orderBookTabs.addTab(self.btcusdTab, "")
        self.ethusdTab = QtWidgets.QWidget()
        self.ethusdTab.setObjectName("ethusdTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ethusdTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ethusdListView = QtWidgets.QListView(self.ethusdTab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.ethusdListView.setFont(font)
        self.ethusdListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ethusdListView.setDragDropOverwriteMode(False)
        self.ethusdListView.setAlternatingRowColors(True)
        self.ethusdListView.setObjectName("ethusdListView")
        self.gridLayout_3.addWidget(self.ethusdListView, 0, 0, 1, 1)
        self.orderBookTabs.addTab(self.ethusdTab, "")
        self.ethbtcTab = QtWidgets.QWidget()
        self.ethbtcTab.setObjectName("ethbtcTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ethbtcTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ethbtcListView = QtWidgets.QListView(self.ethbtcTab)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.ethbtcListView.setFont(font)
        self.ethbtcListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ethbtcListView.setDragDropOverwriteMode(False)
        self.ethbtcListView.setAlternatingRowColors(True)
        self.ethbtcListView.setObjectName("ethbtcListView")
        self.gridLayout_4.addWidget(self.ethbtcListView, 0, 0, 1, 1)
        self.orderBookTabs.addTab(self.ethbtcTab, "")
        self.verticalLayout.addWidget(self.orderBookTabs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(OrderBookDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(OrderBookDialog)
        self.orderBookTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OrderBookDialog)

    def retranslateUi(self, OrderBookDialog):
        _translate = QtCore.QCoreApplication.translate
        OrderBookDialog.setWindowTitle(_translate("OrderBookDialog", "Order Book"))
        self.orderBookTabs.setTabText(self.orderBookTabs.indexOf(self.btcusdTab), _translate("OrderBookDialog", "BTCUSD"))
        self.orderBookTabs.setTabText(self.orderBookTabs.indexOf(self.ethusdTab), _translate("OrderBookDialog", "ETHUSD"))
        self.orderBookTabs.setTabText(self.orderBookTabs.indexOf(self.ethbtcTab), _translate("OrderBookDialog", "ETHBTC"))
        self.closeButton.setText(_translate("OrderBookDialog", "&Close"))

