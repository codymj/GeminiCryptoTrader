# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManageDialog(object):
    def setupUi(self, ManageDialog):
        ManageDialog.setObjectName("ManageDialog")
        ManageDialog.resize(320, 320)
        ManageDialog.setMinimumSize(QtCore.QSize(320, 320))
        ManageDialog.setMaximumSize(QtCore.QSize(320, 320))
        self.gridLayout = QtWidgets.QGridLayout(ManageDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadButton = QtWidgets.QPushButton(ManageDialog)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.removeButton = QtWidgets.QPushButton(ManageDialog)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout.addWidget(self.removeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtWidgets.QPushButton(ManageDialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.accountList = QtWidgets.QListWidget(ManageDialog)
        self.accountList.setObjectName("accountList")
        self.gridLayout.addWidget(self.accountList, 0, 0, 1, 1)

        self.retranslateUi(ManageDialog)
        QtCore.QMetaObject.connectSlotsByName(ManageDialog)

    def retranslateUi(self, ManageDialog):
        _translate = QtCore.QCoreApplication.translate
        ManageDialog.setWindowTitle(_translate("ManageDialog", "Manage Accounts"))
        self.loadButton.setText(_translate("ManageDialog", "&Load"))
        self.removeButton.setText(_translate("ManageDialog", "&Remove"))
        self.okButton.setText(_translate("ManageDialog", "&Ok"))

