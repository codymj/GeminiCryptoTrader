# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/AboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 280)
        AboutDialog.setMinimumSize(QtCore.QSize(400, 280))
        AboutDialog.setMaximumSize(QtCore.QSize(400, 280))
        self.gridLayout = QtWidgets.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.aboutTW = QtWidgets.QTabWidget(AboutDialog)
        self.aboutTW.setObjectName("aboutTW")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.aboutTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.aboutTab)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.aboutTW.addTab(self.aboutTab, "")
        self.authorsTab = QtWidgets.QWidget()
        self.authorsTab.setObjectName("authorsTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.authorsTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.authorsTab)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_3.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.aboutTW.addTab(self.authorsTab, "")
        self.licenseTab = QtWidgets.QWidget()
        self.licenseTab.setObjectName("licenseTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.licenseTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.licenseTab)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout_4.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)
        self.aboutTW.addTab(self.licenseTab, "")
        self.gridLayout.addWidget(self.aboutTW, 1, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.closeButton = QtWidgets.QPushButton(AboutDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 2)

        self.retranslateUi(AboutDialog)
        self.aboutTW.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About Gemini CryptoTrader"))
        self.label.setText(_translate("AboutDialog", "Gemini CryptoTrader"))
        self.plainTextEdit.setPlainText(_translate("AboutDialog", "©2018\n"
"\n"
"https://github.com/codymj/GeminiCryptoTrader"))
        self.aboutTW.setTabText(self.aboutTW.indexOf(self.aboutTab), _translate("AboutDialog", "About"))
        self.plainTextEdit_2.setPlainText(_translate("AboutDialog", "Cody Johnson <codyj@protonmail.com>"))
        self.aboutTW.setTabText(self.aboutTW.indexOf(self.authorsTab), _translate("AboutDialog", "Authors"))
        self.plainTextEdit_3.setPlainText(_translate("AboutDialog", "GNU LESSER GENERAL PUBLIC LICENSE\n"
"Version 3, 29 June 2007\n"
"\n"
"Copyright © 2007 Free Software Foundation, Inc. <https://fsf.org/>\n"
"\n"
"Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.\n"
"\n"
"This version of the GNU Lesser General Public License incorporates the terms and conditions of version 3 of the GNU General Public License, supplemented by the additional permissions listed below.\n"
"\n"
"0. Additional Definitions.\n"
"As used herein, “this License” refers to version 3 of the GNU Lesser General Public License, and the “GNU GPL” refers to version 3 of the GNU General Public License.\n"
"\n"
"“The Library” refers to a covered work governed by this License, other than an Application or a Combined Work as defined below.\n"
"\n"
"An “Application” is any work that makes use of an interface provided by the Library, but which is not otherwise based on the Library. Defining a subclass of a class defined by the Library is deemed a mode of using an interface provided by the Library.\n"
"\n"
"A “Combined Work” is a work produced by combining or linking an Application with the Library. The particular version of the Library with which the Combined Work was made is also called the “Linked Version”.\n"
"\n"
"The “Minimal Corresponding Source” for a Combined Work means the Corresponding Source for the Combined Work, excluding any source code for portions of the Combined Work that, considered in isolation, are based on the Application, and not on the Linked Version.\n"
"\n"
"The “Corresponding Application Code” for a Combined Work means the object code and/or source code for the Application, including any data and utility programs needed for reproducing the Combined Work from the Application, but excluding the System Libraries of the Combined Work.\n"
"\n"
"1. Exception to Section 3 of the GNU GPL.\n"
"You may convey a covered work under sections 3 and 4 of this License without being bound by section 3 of the GNU GPL.\n"
"\n"
"2. Conveying Modified Versions.\n"
"If you modify a copy of the Library, and, in your modifications, a facility refers to a function or data to be supplied by an Application that uses the facility (other than as an argument passed when the facility is invoked), then you may convey a copy of the modified version:\n"
"\n"
"a) under this License, provided that you make a good faith effort to ensure that, in the event an Application does not supply the function or data, the facility still operates, and performs whatever part of its purpose remains meaningful, or\n"
"b) under the GNU GPL, with none of the additional permissions of this License applicable to that copy.\n"
"3. Object Code Incorporating Material from Library Header Files.\n"
"The object code form of an Application may incorporate material from a header file that is part of the Library. You may convey such object code under terms of your choice, provided that, if the incorporated material is not limited to numerical parameters, data structure layouts and accessors, or small macros, inline functions and templates (ten or fewer lines in length), you do both of the following:\n"
"\n"
"a) Give prominent notice with each copy of the object code that the Library is used in it and that the Library and its use are covered by this License.\n"
"b) Accompany the object code with a copy of the GNU GPL and this license document.\n"
"4. Combined Works.\n"
"You may convey a Combined Work under terms of your choice that, taken together, effectively do not restrict modification of the portions of the Library contained in the Combined Work and reverse engineering for debugging such modifications, if you also do each of the following:\n"
"\n"
"a) Give prominent notice with each copy of the Combined Work that the Library is used in it and that the Library and its use are covered by this License.\n"
"b) Accompany the Combined Work with a copy of the GNU GPL and this license document.\n"
"c) For a Combined Work that displays copyright notices during execution, include the copyright notice for the Library among these notices, as well as a reference directing the user to the copies of the GNU GPL and this license document.\n"
"d) Do one of the following:\n"
"0) Convey the Minimal Corresponding Source under the terms of this License, and the Corresponding Application Code in a form suitable for, and under terms that permit, the user to recombine or relink the Application with a modified version of the Linked Version to produce a modified Combined Work, in the manner specified by section 6 of the GNU GPL for conveying Corresponding Source.\n"
"1) Use a suitable shared library mechanism for linking with the Library. A suitable mechanism is one that (a) uses at run time a copy of the Library already present on the user\'s computer system, and (b) will operate properly with a modified version of the Library that is interface-compatible with the Linked Version.\n"
"e) Provide Installation Information, but only if you would otherwise be required to provide such information under section 6 of the GNU GPL, and only to the extent that such information is necessary to install and execute a modified version of the Combined Work produced by recombining or relinking the Application with a modified version of the Linked Version. (If you use option 4d0, the Installation Information must accompany the Minimal Corresponding Source and Corresponding Application Code. If you use option 4d1, you must provide the Installation Information in the manner specified by section 6 of the GNU GPL for conveying Corresponding Source.)\n"
"5. Combined Libraries.\n"
"You may place library facilities that are a work based on the Library side by side in a single library together with other library facilities that are not Applications and are not covered by this License, and convey such a combined library under terms of your choice, if you do both of the following:\n"
"\n"
"a) Accompany the combined library with a copy of the same work based on the Library, uncombined with any other library facilities, conveyed under the terms of this License.\n"
"b) Give prominent notice with the combined library that part of it is a work based on the Library, and explaining where to find the accompanying uncombined form of the same work.\n"
"6. Revised Versions of the GNU Lesser General Public License.\n"
"The Free Software Foundation may publish revised and/or new versions of the GNU Lesser General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.\n"
"\n"
"Each version is given a distinguishing version number. If the Library as you received it specifies that a certain numbered version of the GNU Lesser General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that published version or of any later version published by the Free Software Foundation. If the Library as you received it does not specify a version number of the GNU Lesser General Public License, you may choose any version of the GNU Lesser General Public License ever published by the Free Software Foundation.\n"
"\n"
"If the Library as you received it specifies that a proxy can decide whether future versions of the GNU Lesser General Public License shall apply, that proxy\'s public statement of acceptance of any version is permanent authorization for you to choose that version for the Library."))
        self.aboutTW.setTabText(self.aboutTW.indexOf(self.licenseTab), _translate("AboutDialog", "License"))
        self.label_2.setText(_translate("AboutDialog", "v0.0.0"))
        self.closeButton.setText(_translate("AboutDialog", "&Close"))

