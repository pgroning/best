# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'birdWeight.ui'
#
# Created: Wed Sep 23 20:45:13 2015
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

class Ui_BirdWeight(object):
    def setupUi(self, BirdWeight):
        BirdWeight.setObjectName(_fromUtf8("BirdWeight"))
        BirdWeight.setEnabled(True)
        BirdWeight.resize(371, 279)
        self.gridlayout = QtGui.QGridLayout(BirdWeight)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.leftEndSlider = QtGui.QSlider(BirdWeight)
        self.leftEndSlider.setMinimumSize(QtCore.QSize(0, 160))
        self.leftEndSlider.setMaximumSize(QtCore.QSize(16777215, 160))
        self.leftEndSlider.setProperty("value", 30)
        self.leftEndSlider.setOrientation(QtCore.Qt.Vertical)
        self.leftEndSlider.setObjectName(_fromUtf8("leftEndSlider"))
        self.gridlayout.addWidget(self.leftEndSlider, 0, 0, 1, 1)
        self.rightEndSlider = QtGui.QSlider(BirdWeight)
        self.rightEndSlider.setMinimumSize(QtCore.QSize(0, 160))
        self.rightEndSlider.setMaximumSize(QtCore.QSize(16777215, 160))
        self.rightEndSlider.setProperty("value", 30)
        self.rightEndSlider.setOrientation(QtCore.Qt.Vertical)
        self.rightEndSlider.setObjectName(_fromUtf8("rightEndSlider"))
        self.gridlayout.addWidget(self.rightEndSlider, 0, 4, 1, 1)
        self.leftTopSlider = QtGui.QSlider(BirdWeight)
        self.leftTopSlider.setMinimumSize(QtCore.QSize(160, 0))
        self.leftTopSlider.setMaximumSize(QtCore.QSize(160, 16777215))
        self.leftTopSlider.setProperty("value", 50)
        self.leftTopSlider.setOrientation(QtCore.Qt.Horizontal)
        self.leftTopSlider.setObjectName(_fromUtf8("leftTopSlider"))
        self.gridlayout.addWidget(self.leftTopSlider, 1, 1, 1, 2)
        self.leftTopLabel = QtGui.QLabel(BirdWeight)
        self.leftTopLabel.setObjectName(_fromUtf8("leftTopLabel"))
        self.gridlayout.addWidget(self.leftTopLabel, 1, 3, 1, 1)
        self.rightTopLabel = QtGui.QLabel(BirdWeight)
        self.rightTopLabel.setObjectName(_fromUtf8("rightTopLabel"))
        self.gridlayout.addWidget(self.rightTopLabel, 2, 1, 1, 1)
        self.rightTopSlider = QtGui.QSlider(BirdWeight)
        self.rightTopSlider.setMinimumSize(QtCore.QSize(160, 0))
        self.rightTopSlider.setMaximumSize(QtCore.QSize(160, 16777215))
        self.rightTopSlider.setProperty("value", 50)
        self.rightTopSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rightTopSlider.setObjectName(_fromUtf8("rightTopSlider"))
        self.gridlayout.addWidget(self.rightTopSlider, 2, 2, 1, 2)
        self.defaultPushButton = QtGui.QPushButton(BirdWeight)
        self.defaultPushButton.setObjectName(_fromUtf8("defaultPushButton"))
        self.gridlayout.addWidget(self.defaultPushButton, 3, 2, 1, 1)
        self.weightPlot = WeightPlot(BirdWeight)
        self.weightPlot.setMinimumSize(QtCore.QSize(240, 160))
        self.weightPlot.setMaximumSize(QtCore.QSize(99999, 99999))
        self.weightPlot.setObjectName(_fromUtf8("weightPlot"))
        self.gridlayout.addWidget(self.weightPlot, 0, 1, 1, 3)

        self.retranslateUi(BirdWeight)
        QtCore.QMetaObject.connectSlotsByName(BirdWeight)

    def retranslateUi(self, BirdWeight):
        BirdWeight.setWindowTitle(_translate("BirdWeight", "Dialog", None))
        BirdWeight.setToolTip(_translate("BirdWeight", "T", None))
        self.leftTopLabel.setText(_translate("BirdWeight", "<- Top Left", None))
        self.rightTopLabel.setText(_translate("BirdWeight", "Top Right ->", None))
        self.defaultPushButton.setText(_translate("BirdWeight", "Set Default (f(kinf)", None))

from weightPlot import WeightPlot

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BirdWeight = QtGui.QDialog()
    ui = Ui_BirdWeight()
    ui.setupUi(BirdWeight)
    BirdWeight.show()
    sys.exit(app.exec_())

