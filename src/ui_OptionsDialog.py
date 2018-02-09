# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.resize(420, 240)
        OptionsDialog.setMinimumSize(QtCore.QSize(420, 240))
        OptionsDialog.setMaximumSize(QtCore.QSize(420, 240))
        self.gridLayout = QtWidgets.QGridLayout(OptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encryptButton = QtWidgets.QPushButton(OptionsDialog)
        self.encryptButton.setObjectName("encryptButton")
        self.horizontalLayout.addWidget(self.encryptButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(OptionsDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.doneButton = QtWidgets.QPushButton(OptionsDialog)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout.addWidget(self.doneButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(OptionsDialog)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)

    def retranslateUi(self, OptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        OptionsDialog.setWindowTitle(_translate("OptionsDialog", "Options"))
        self.encryptButton.setText(_translate("OptionsDialog", "&Encrypt"))
        self.cancelButton.setText(_translate("OptionsDialog", "&Cancel"))
        self.doneButton.setText(_translate("OptionsDialog", "&Done"))

