# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'birdPlot.ui'
#
# Created: Wed Sep 23 20:39:24 2015
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

class Ui_BirdPlot(object):
    def setupUi(self, BirdPlot):
        BirdPlot.setObjectName(_fromUtf8("BirdPlot"))
        BirdPlot.resize(668, 440)
        self.horizontalLayout = QtGui.QHBoxLayout(BirdPlot)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.closeButton = QtGui.QPushButton(BirdPlot)
        self.closeButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/stock-stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.vboxlayout.addWidget(self.closeButton)
        self.printButton = QtGui.QPushButton(BirdPlot)
        self.printButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/stock-print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printButton.setIcon(icon1)
        self.printButton.setObjectName(_fromUtf8("printButton"))
        self.vboxlayout.addWidget(self.printButton)
        self.openTabButton = QtGui.QPushButton(BirdPlot)
        self.openTabButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/stock-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openTabButton.setIcon(icon2)
        self.openTabButton.setObjectName(_fromUtf8("openTabButton"))
        self.vboxlayout.addWidget(self.openTabButton)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.voidLabel = QtGui.QLabel(BirdPlot)
        self.voidLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.voidLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voidLabel.setObjectName(_fromUtf8("voidLabel"))
        self.hboxlayout.addWidget(self.voidLabel)
        self.voidItem = QtGui.QComboBox(BirdPlot)
        self.voidItem.setMaximumSize(QtCore.QSize(60, 16777215))
        self.voidItem.setObjectName(_fromUtf8("voidItem"))
        self.hboxlayout.addWidget(self.voidItem)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.plotAllCaseItem = QtGui.QCheckBox(BirdPlot)
        self.plotAllCaseItem.setObjectName(_fromUtf8("plotAllCaseItem"))
        self.vboxlayout.addWidget(self.plotAllCaseItem)
        self.plotVoidItem = QtGui.QCheckBox(BirdPlot)
        self.plotVoidItem.setObjectName(_fromUtf8("plotVoidItem"))
        self.vboxlayout.addWidget(self.plotVoidItem)
        self.plotMarkedRod = QtGui.QCheckBox(BirdPlot)
        self.plotMarkedRod.setObjectName(_fromUtf8("plotMarkedRod"))
        self.vboxlayout.addWidget(self.plotMarkedRod)
        self.plotBAFintRules = QtGui.QCheckBox(BirdPlot)
        self.plotBAFintRules.setObjectName(_fromUtf8("plotBAFintRules"))
        self.vboxlayout.addWidget(self.plotBAFintRules)
        self.plotXSItem = QtGui.QComboBox(BirdPlot)
        self.plotXSItem.setMaximumSize(QtCore.QSize(100, 16777215))
        self.plotXSItem.setObjectName(_fromUtf8("plotXSItem"))
        self.vboxlayout.addWidget(self.plotXSItem)
        self.plotTypeItem = QtGui.QComboBox(BirdPlot)
        self.plotTypeItem.setMaximumSize(QtCore.QSize(100, 16777215))
        self.plotTypeItem.setObjectName(_fromUtf8("plotTypeItem"))
        self.vboxlayout.addWidget(self.plotTypeItem)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.vboxlayout)
        self.plotFrame = QtGui.QFrame(BirdPlot)
        self.plotFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.plotFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.plotFrame.setLineWidth(2)
        self.plotFrame.setMidLineWidth(2)
        self.plotFrame.setObjectName(_fromUtf8("plotFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.plotFrame)
        self.verticalLayout.setSpacing(-1)
        self.verticalLayout.setMargin(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plotter = Plotter(self.plotFrame)
        self.plotter.setMinimumSize(QtCore.QSize(520, 400))
        self.plotter.setObjectName(_fromUtf8("plotter"))
        self.verticalLayout.addWidget(self.plotter)
        self.horizontalLayout.addWidget(self.plotFrame)

        self.retranslateUi(BirdPlot)
        QtCore.QMetaObject.connectSlotsByName(BirdPlot)

    def retranslateUi(self, BirdPlot):
        BirdPlot.setWindowTitle(_translate("BirdPlot", "Plot Window", None))
        self.closeButton.setText(_translate("BirdPlot", "Close", None))
        self.printButton.setText(_translate("BirdPlot", "Print", None))
        self.openTabButton.setText(_translate("BirdPlot", "Table", None))
        self.voidLabel.setText(_translate("BirdPlot", "Void:", None))
        self.plotAllCaseItem.setText(_translate("BirdPlot", "All cases", None))
        self.plotVoidItem.setText(_translate("BirdPlot", "Plot void", None))
        self.plotMarkedRod.setText(_translate("BirdPlot", "Plot rod", None))
        self.plotBAFintRules.setText(_translate("BirdPlot", "BA Fint\n"
"reduction", None))

from casPlotter import Plotter
import CuteBird_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BirdPlot = QtGui.QDialog()
    ui = Ui_BirdPlot()
    ui.setupUi(BirdPlot)
    BirdPlot.show()
    sys.exit(app.exec_())

