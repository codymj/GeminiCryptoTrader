# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/WithdrawToDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WithdrawToDialog(object):
    def setupUi(self, WithdrawToDialog):
        WithdrawToDialog.setObjectName("WithdrawToDialog")
        WithdrawToDialog.resize(480, 420)
        WithdrawToDialog.setMinimumSize(QtCore.QSize(480, 420))
        WithdrawToDialog.setMaximumSize(QtCore.QSize(480, 420))
        self.gridLayout = QtWidgets.QGridLayout(WithdrawToDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(WithdrawToDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(WithdrawToDialog)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 231))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btcRB = QtWidgets.QRadioButton(WithdrawToDialog)
        self.btcRB.setChecked(True)
        self.btcRB.setObjectName("btcRB")
        self.buttonGroup = QtWidgets.QButtonGroup(WithdrawToDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btcRB)
        self.horizontalLayout_2.addWidget(self.btcRB)
        self.ethRB = QtWidgets.QRadioButton(WithdrawToDialog)
        self.ethRB.setObjectName("ethRB")
        self.buttonGroup.addButton(self.ethRB)
        self.horizontalLayout_2.addWidget(self.ethRB)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(WithdrawToDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.addressLE = QtWidgets.QLineEdit(WithdrawToDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressLE.sizePolicy().hasHeightForWidth())
        self.addressLE.setSizePolicy(sizePolicy)
        self.addressLE.setObjectName("addressLE")
        self.verticalLayout.addWidget(self.addressLE)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(WithdrawToDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.amountLE = QtWidgets.QLineEdit(WithdrawToDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amountLE.sizePolicy().hasHeightForWidth())
        self.amountLE.setSizePolicy(sizePolicy)
        self.amountLE.setObjectName("amountLE")
        self.horizontalLayout_3.addWidget(self.amountLE)
        self.amountUnitLabel = QtWidgets.QLabel(WithdrawToDialog)
        self.amountUnitLabel.setObjectName("amountUnitLabel")
        self.horizontalLayout_3.addWidget(self.amountUnitLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(WithdrawToDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.withdrawButton = QtWidgets.QPushButton(WithdrawToDialog)
        self.withdrawButton.setObjectName("withdrawButton")
        self.horizontalLayout.addWidget(self.withdrawButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.retranslateUi(WithdrawToDialog)
        QtCore.QMetaObject.connectSlotsByName(WithdrawToDialog)

    def retranslateUi(self, WithdrawToDialog):
        _translate = QtCore.QCoreApplication.translate
        WithdrawToDialog.setWindowTitle(_translate("WithdrawToDialog", "Withdraw To"))
        self.label.setText(_translate("WithdrawToDialog", "Disclaimer:"))
        self.textEdit.setHtml(_translate("WithdrawToDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans Semi-Condensed\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Before you can withdraw cryptocurrency funds to a whitelisted address, you need three things:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Cryptocurrency address whitelists needs to be enabled for your account</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. The address you want to withdraw funds to needs to already be on that whitelist</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. An API key with the Fund Manager role added</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Contact <a href=\"mailto:institutional@gemini.com\"><span style=\" text-decoration: underline; color:#0000ff;\">institutional@gemini.com</span></a> for information on setting up whitelists and adding addresses. See Roles for more information on how to add the Fund Manager role to the API key you want to use.</p></body></html>"))
        self.btcRB.setText(_translate("WithdrawToDialog", "BTC"))
        self.ethRB.setText(_translate("WithdrawToDialog", "ETH"))
        self.label_2.setText(_translate("WithdrawToDialog", "Destination Address:"))
        self.label_3.setText(_translate("WithdrawToDialog", "Amount:"))
        self.amountUnitLabel.setText(_translate("WithdrawToDialog", "BTC"))
        self.cancelButton.setText(_translate("WithdrawToDialog", "&Cancel"))
        self.withdrawButton.setText(_translate("WithdrawToDialog", "&Withdraw"))

