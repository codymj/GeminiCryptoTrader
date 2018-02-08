# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountsDialog(object):
    def setupUi(self, AccountsDialog):
        AccountsDialog.setObjectName("AccountsDialog")
        AccountsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AccountsDialog.resize(420, 250)
        AccountsDialog.setMinimumSize(QtCore.QSize(420, 250))
        AccountsDialog.setMaximumSize(QtCore.QSize(420, 250))
        AccountsDialog.setBaseSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(AccountsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AccountsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.accountIdLE = QtWidgets.QLineEdit(AccountsDialog)
        self.accountIdLE.setObjectName("accountIdLE")
        self.verticalLayout.addWidget(self.accountIdLE)
        self.label_2 = QtWidgets.QLabel(AccountsDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.apiKeyLE = QtWidgets.QLineEdit(AccountsDialog)
        self.apiKeyLE.setObjectName("apiKeyLE")
        self.verticalLayout.addWidget(self.apiKeyLE)
        self.label_3 = QtWidgets.QLabel(AccountsDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.privateKeyLE = QtWidgets.QLineEdit(AccountsDialog)
        self.privateKeyLE.setObjectName("privateKeyLE")
        self.verticalLayout.addWidget(self.privateKeyLE)
        self.sandboxCB = QtWidgets.QCheckBox(AccountsDialog)
        self.sandboxCB.setObjectName("sandboxCB")
        self.verticalLayout.addWidget(self.sandboxCB)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.manageButton = QtWidgets.QPushButton(AccountsDialog)
        self.manageButton.setObjectName("manageButton")
        self.horizontalLayout.addWidget(self.manageButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.updateButton = QtWidgets.QPushButton(AccountsDialog)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.addButton = QtWidgets.QPushButton(AccountsDialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.doneButton = QtWidgets.QPushButton(AccountsDialog)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout.addWidget(self.doneButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(AccountsDialog)
        QtCore.QMetaObject.connectSlotsByName(AccountsDialog)

    def retranslateUi(self, AccountsDialog):
        _translate = QtCore.QCoreApplication.translate
        AccountsDialog.setWindowTitle(_translate("AccountsDialog", "Setup Account"))
        self.label.setText(_translate("AccountsDialog", "Account ID:"))
        self.label_2.setText(_translate("AccountsDialog", "API Key:"))
        self.label_3.setText(_translate("AccountsDialog", "Private Key:"))
        self.sandboxCB.setText(_translate("AccountsDialog", "Sandbox Account?"))
        self.manageButton.setText(_translate("AccountsDialog", "&Manage"))
        self.updateButton.setText(_translate("AccountsDialog", "&Update"))
        self.addButton.setText(_translate("AccountsDialog", "&Add"))
        self.doneButton.setText(_translate("AccountsDialog", "&Done"))

