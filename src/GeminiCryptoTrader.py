################################################################################
#
#  GeminiCryptoTrader.py
#  Author: Cody Johnson <codyj@protonmail.com>
#
################################################################################

from MainWindow import MainWindow
from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
