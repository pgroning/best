# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created: Tue Sep 22 23:02:13 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(678, 495)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bundes/icons/bird-icon_32x32.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 381))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 27))
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
        self.menuHelp.setGeometry(QtCore.QRect(381, 195, 125, 107))
        self.menuHelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.lineEdit = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
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
        self.actionPreferencies.setObjectName(_fromUtf8("actionPreferencies"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_Best = QtGui.QAction(MainWindow)
        self.actionAbout_Best.setObjectName(_fromUtf8("actionAbout_Best"))
        self.actionFint = QtGui.QAction(MainWindow)
        self.actionFint.setObjectName(_fromUtf8("actionFint"))
        self.actionKinf = QtGui.QAction(MainWindow)
        self.actionKinf.setObjectName(_fromUtf8("actionKinf"))
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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Best", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Map 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
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

