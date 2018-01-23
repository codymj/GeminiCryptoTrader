# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/SetupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetupDialog(object):
    def setupUi(self, SetupDialog):
        SetupDialog.setObjectName("SetupDialog")
        SetupDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SetupDialog.resize(320, 240)
        self.gridLayout = QtWidgets.QGridLayout(SetupDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SetupDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.accountIdLE = QtWidgets.QLineEdit(SetupDialog)
        self.accountIdLE.setObjectName("accountIdLE")
        self.verticalLayout.addWidget(self.accountIdLE)
        self.label_2 = QtWidgets.QLabel(SetupDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.apiKeyLE = QtWidgets.QLineEdit(SetupDialog)
        self.apiKeyLE.setObjectName("apiKeyLE")
        self.verticalLayout.addWidget(self.apiKeyLE)
        self.label_3 = QtWidgets.QLabel(SetupDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.privateKeyLE = QtWidgets.QLineEdit(SetupDialog)
        self.privateKeyLE.setObjectName("privateKeyLE")
        self.verticalLayout.addWidget(self.privateKeyLE)
        self.sandboxCB = QtWidgets.QCheckBox(SetupDialog)
        self.sandboxCB.setObjectName("sandboxCB")
        self.verticalLayout.addWidget(self.sandboxCB)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(SetupDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(SetupDialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(SetupDialog)
        QtCore.QMetaObject.connectSlotsByName(SetupDialog)

    def retranslateUi(self, SetupDialog):
        _translate = QtCore.QCoreApplication.translate
        SetupDialog.setWindowTitle(_translate("SetupDialog", "Setup Account"))
        self.label.setText(_translate("SetupDialog", "Account ID:"))
        self.label_2.setText(_translate("SetupDialog", "API Key:"))
        self.label_3.setText(_translate("SetupDialog", "Private Key:"))
        self.sandboxCB.setText(_translate("SetupDialog", "Sandbox Account?"))
        self.cancelButton.setText(_translate("SetupDialog", "&Cancel"))
        self.okButton.setText(_translate("SetupDialog", "&Ok"))

