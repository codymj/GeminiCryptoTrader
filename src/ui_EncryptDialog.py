# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncryptDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EncryptDialog(object):
    def setupUi(self, EncryptDialog):
        EncryptDialog.setObjectName("EncryptDialog")
        EncryptDialog.resize(320, 240)
        EncryptDialog.setMinimumSize(QtCore.QSize(320, 240))
        EncryptDialog.setMaximumSize(QtCore.QSize(320, 240))
        self.gridLayout = QtWidgets.QGridLayout(EncryptDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(EncryptDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(EncryptDialog)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.noButton = QtWidgets.QPushButton(EncryptDialog)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.yesButton = QtWidgets.QPushButton(EncryptDialog)
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout.addWidget(self.yesButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(EncryptDialog)
        QtCore.QMetaObject.connectSlotsByName(EncryptDialog)

    def retranslateUi(self, EncryptDialog):
        _translate = QtCore.QCoreApplication.translate
        EncryptDialog.setWindowTitle(_translate("EncryptDialog", "Encrypt data?"))
        self.label.setText(_translate("EncryptDialog", "Would you like to set up encryption?"))
        self.plainTextEdit.setPlainText(_translate("EncryptDialog", "If you choose to do so, you will need to remember your password. Failing to remember your password will require you to re-enter all of your data as the process cannot be undone.\n"
"\n"
"You can choose to encrypt your data at a later time."))
        self.noButton.setText(_translate("EncryptDialog", "&No"))
        self.yesButton.setText(_translate("EncryptDialog", "&Yes"))

