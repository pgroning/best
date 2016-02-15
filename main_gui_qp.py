#!/usr/bin/python

from IPython.core.debugger import Tracer

import sys, os
from PyQt4 import QtGui, QtCore
import numpy as np

class MainWin(QtGui.QMainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Main Window')
        self.resize(1100,620)
        self.move(200,200)

        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()
        self.create_mainframe()


    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        quit_action = self.create_action("&Quit", slot=self.close, 
                                         shortcut="Ctrl+Q", tip="Close the application")

        self.add_actions(self.file_menu,(quit_action,None))


    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QtGui.QAction(text, self)
        if icon is not None:
            action.setIcon(QtGui.QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
        

    def create_toolbar(self):
        fileAction = QtGui.QAction(QtGui.QIcon('icons/open-file-icon_32x32.png'), 'Open file', self)
        fileAction.setStatusTip('Open file')
        #fileAction.triggered.connect(self.openFile)

        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(fileAction)

    def create_statusbar(self):
        self.status_text = QtGui.QLabel("Main window")
        self.statusBar().addWidget(self.status_text, 1)


    def create_mainframe(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWin()
    window.show()
    #app.exec_()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
