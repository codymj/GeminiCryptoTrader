# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PasswordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PasswordDialog(object):
    def setupUi(self, PasswordDialog):
        PasswordDialog.setObjectName("PasswordDialog")
        PasswordDialog.resize(320, 130)
        PasswordDialog.setMinimumSize(QtCore.QSize(320, 130))
        PasswordDialog.setMaximumSize(QtCore.QSize(320, 130))
        self.gridLayout = QtWidgets.QGridLayout(PasswordDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(PasswordDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.passwordLE = QtWidgets.QLineEdit(PasswordDialog)
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setObjectName("passwordLE")
        self.verticalLayout.addWidget(self.passwordLE)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.exitButton = QtWidgets.QPushButton(PasswordDialog)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.decryptButton = QtWidgets.QPushButton(PasswordDialog)
        self.decryptButton.setObjectName("decryptButton")
        self.horizontalLayout.addWidget(self.decryptButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(PasswordDialog)

    def retranslateUi(self, PasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        PasswordDialog.setWindowTitle(_translate("PasswordDialog", "Decrypt data"))
        self.label.setText(_translate("PasswordDialog", "Enter password to decrypt data:"))
        self.exitButton.setText(_translate("PasswordDialog", "&Exit"))
        self.decryptButton.setText(_translate("PasswordDialog", "&Decrypt"))

