#! /usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot

from mainwin import Ui_MainWindow
from pyDraw import Bundle



class Main(QtGui.QMainWindow):
    def __init__(self):
        #super(Main, self).__init__()
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Show message in statusbar
        self.statusBar().showMessage('Ready')

        # File menu exit action
        self.ui.fileMenuExit.triggered.connect(self.close)        
        #self.ui.fileMenuExit.setStatusTip('Exit application')
        #self.ui.fileMenuExit.setShortcut('Ctrl+Q')
        
        # File menu open file action
        self.ui.fileMenuOpenFile.triggered.connect(self.fileDialog)

        # Draw bundle map
        b = Bundle()
        #self.ui.tabWidget.grid.addWidget(b,1,0,1,1)
        self.ui.gridLayout.addWidget(b,0,0,1,1)
        
    def fileDialog(self):

        fileName = QtGui.QFileDialog.getOpenFileName(self, "Open Data File", "/", "Text files (*.txt)") 
        #if fileName:
            #f = open(fileName, 'r')
            #data = f.read()
            #self.textEdit.setText(data)
            
            
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
             "Are you sure to quit?", QtGui.QMessageBox.Yes | 
             QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    # Create an PyQT4 application object.
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
