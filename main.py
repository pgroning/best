#! /usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot

from mainwin import Ui_MainWindow



class Main(QtGui.QMainWindow):
    def __init__(self):
        #super(Main, self).__init__()
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    # Create an PyQT4 application object.
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
