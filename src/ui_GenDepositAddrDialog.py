# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/GenDepositAddrDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenDepositAddrDialog(object):
    def setupUi(self, GenDepositAddrDialog):
        GenDepositAddrDialog.setObjectName("GenDepositAddrDialog")
        GenDepositAddrDialog.resize(240, 240)
        GenDepositAddrDialog.setMinimumSize(QtCore.QSize(240, 240))
        GenDepositAddrDialog.setMaximumSize(QtCore.QSize(240, 240))
        self.gridLayout = QtWidgets.QGridLayout(GenDepositAddrDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.generateButton = QtWidgets.QPushButton(GenDepositAddrDialog)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout_2.addWidget(self.generateButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(GenDepositAddrDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelLE = QtWidgets.QLineEdit(GenDepositAddrDialog)
        self.labelLE.setObjectName("labelLE")
        self.horizontalLayout_3.addWidget(self.labelLE)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(GenDepositAddrDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.addressLE = QtWidgets.QLineEdit(GenDepositAddrDialog)
        self.addressLE.setObjectName("addressLE")
        self.verticalLayout_2.addWidget(self.addressLE)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.closeButton = QtWidgets.QPushButton(GenDepositAddrDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)

        self.retranslateUi(GenDepositAddrDialog)
        QtCore.QMetaObject.connectSlotsByName(GenDepositAddrDialog)

    def retranslateUi(self, GenDepositAddrDialog):
        _translate = QtCore.QCoreApplication.translate
        GenDepositAddrDialog.setWindowTitle(_translate("GenDepositAddrDialog", "Generate Deposit Address"))
        self.generateButton.setText(_translate("GenDepositAddrDialog", "&Generate"))
        self.label.setText(_translate("GenDepositAddrDialog", "Label (optional):"))
        self.label_2.setText(_translate("GenDepositAddrDialog", "New Address:"))
        self.closeButton.setText(_translate("GenDepositAddrDialog", "&Close"))

