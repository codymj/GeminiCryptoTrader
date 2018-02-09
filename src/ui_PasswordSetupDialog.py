# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PasswordSetupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PasswordSetupDialog(object):
    def setupUi(self, PasswordSetupDialog):
        PasswordSetupDialog.setObjectName("PasswordSetupDialog")
        PasswordSetupDialog.resize(320, 200)
        PasswordSetupDialog.setMinimumSize(QtCore.QSize(320, 200))
        PasswordSetupDialog.setMaximumSize(QtCore.QSize(320, 200))
        self.gridLayout = QtWidgets.QGridLayout(PasswordSetupDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(PasswordSetupDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.firstPassLE = QtWidgets.QLineEdit(PasswordSetupDialog)
        self.firstPassLE.setAutoFillBackground(False)
        self.firstPassLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.firstPassLE.setClearButtonEnabled(False)
        self.firstPassLE.setObjectName("firstPassLE")
        self.verticalLayout.addWidget(self.firstPassLE)
        self.label_2 = QtWidgets.QLabel(PasswordSetupDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.secondPassLE = QtWidgets.QLineEdit(PasswordSetupDialog)
        self.secondPassLE.setAutoFillBackground(False)
        self.secondPassLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secondPassLE.setClearButtonEnabled(False)
        self.secondPassLE.setObjectName("secondPassLE")
        self.verticalLayout.addWidget(self.secondPassLE)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(PasswordSetupDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.setPasswordButton = QtWidgets.QPushButton(PasswordSetupDialog)
        self.setPasswordButton.setObjectName("setPasswordButton")
        self.horizontalLayout.addWidget(self.setPasswordButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PasswordSetupDialog)
        QtCore.QMetaObject.connectSlotsByName(PasswordSetupDialog)

    def retranslateUi(self, PasswordSetupDialog):
        _translate = QtCore.QCoreApplication.translate
        PasswordSetupDialog.setWindowTitle(_translate("PasswordSetupDialog", "Password Setup"))
        self.label.setText(_translate("PasswordSetupDialog", "Enter your password:"))
        self.label_2.setText(_translate("PasswordSetupDialog", "Re-enter password:"))
        self.cancelButton.setText(_translate("PasswordSetupDialog", "&Cancel"))
        self.setPasswordButton.setText(_translate("PasswordSetupDialog", "&Set Password"))

