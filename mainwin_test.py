# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin_test.ui'
#
# Created: Sun Sep 27 23:07:18 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pyDraw import Bundle

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(765, 542)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/bird-icon_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        # Draw bundle map
        b = Bundle()
        #self.ui.tabWidget.grid.addWidget(b,1,0,1,1)
        self.verticalLayout.addWidget(b)

        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuPlot = QtGui.QMenu(self.menuTools)
        self.menuPlot.setObjectName(_fromUtf8("menuPlot"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setGeometry(QtCore.QRect(359, 196, 125, 107))
        self.menuHelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.BottomToolBarArea|QtCore.Qt.TopToolBarArea)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileMenuOpenFile = QtGui.QAction(MainWindow)
        self.fileMenuOpenFile.setCheckable(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/open-file-icon_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileMenuOpenFile.setIcon(icon1)
        self.fileMenuOpenFile.setObjectName(_fromUtf8("fileMenuOpenFile"))
        self.fileMenuExit = QtGui.QAction(MainWindow)
        self.fileMenuExit.setCheckable(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/exit-icon_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileMenuExit.setIcon(icon2)
        self.fileMenuExit.setWhatsThis(_fromUtf8(""))
        self.fileMenuExit.setObjectName(_fromUtf8("fileMenuExit"))
        self.actionPreferencies = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/preferences-icon_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferencies.setIcon(icon3)
        self.actionPreferencies.setObjectName(_fromUtf8("actionPreferencies"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_Best = QtGui.QAction(MainWindow)
        self.actionAbout_Best.setObjectName(_fromUtf8("actionAbout_Best"))
        self.actionFint = QtGui.QAction(MainWindow)
        self.actionFint.setObjectName(_fromUtf8("actionFint"))
        self.actionKinf = QtGui.QAction(MainWindow)
        self.actionKinf.setObjectName(_fromUtf8("actionKinf"))
        self.actionPlot = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/diagram-icon_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon4)
        self.actionPlot.setObjectName(_fromUtf8("actionPlot"))
        self.menuFile.addAction(self.fileMenuOpenFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.fileMenuExit)
        self.menuEdit.addAction(self.actionPreferencies)
        self.menuPlot.addAction(self.actionFint)
        self.menuPlot.addAction(self.actionKinf)
        self.menuTools.addAction(self.menuPlot.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Best)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.fileMenuOpenFile)
        self.toolBar.addAction(self.actionPreferencies)
        self.toolBar.addAction(self.actionPlot)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.fileMenuExit)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Best", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit", None))
        self.menuTools.setTitle(_translate("MainWindow", "&Tools", None))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.fileMenuOpenFile.setText(_translate("MainWindow", "Open file...", None))
        self.fileMenuOpenFile.setToolTip(_translate("MainWindow", "Open file", None))
        self.fileMenuOpenFile.setStatusTip(_translate("MainWindow", "Open file", None))
        self.fileMenuOpenFile.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.fileMenuExit.setText(_translate("MainWindow", "Exit", None))
        self.fileMenuExit.setToolTip(_translate("MainWindow", "Exit", None))
        self.fileMenuExit.setStatusTip(_translate("MainWindow", "Exit application", None))
        self.fileMenuExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionPreferencies.setText(_translate("MainWindow", "Preferencies...", None))
        self.actionAbout.setText(_translate("MainWindow", "Best Help", None))
        self.actionAbout_Best.setText(_translate("MainWindow", "About Best", None))
        self.actionFint.setText(_translate("MainWindow", "Fint", None))
        self.actionKinf.setText(_translate("MainWindow", "Kinf", None))
        self.actionPlot.setText(_translate("MainWindow", "Plot", None))
        self.actionPlot.setShortcut(_translate("MainWindow", "Ctrl+P", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

