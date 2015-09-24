# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'btfPopup.ui'
#
# Created: Wed Sep 23 20:41:05 2015
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

class Ui_BftPopup(object):
    def setupUi(self, BftPopup):
        BftPopup.setObjectName(_fromUtf8("BftPopup"))
        BftPopup.resize(621, 262)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(BftPopup)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.activeLengthLabel = QtGui.QLabel(BftPopup)
        self.activeLengthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.activeLengthLabel.setObjectName(_fromUtf8("activeLengthLabel"))
        self.horizontalLayout.addWidget(self.activeLengthLabel)
        self.activeLengthLineEdit = QtGui.QLineEdit(BftPopup)
        self.activeLengthLineEdit.setMinimumSize(QtCore.QSize(54, 0))
        self.activeLengthLineEdit.setMaximumSize(QtCore.QSize(54, 16777215))
        self.activeLengthLineEdit.setObjectName(_fromUtf8("activeLengthLineEdit"))
        self.horizontalLayout.addWidget(self.activeLengthLineEdit)
        self.fuelWeightLabel = QtGui.QLabel(BftPopup)
        self.fuelWeightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fuelWeightLabel.setObjectName(_fromUtf8("fuelWeightLabel"))
        self.horizontalLayout.addWidget(self.fuelWeightLabel)
        self.fuelWeightLineEdit = QtGui.QLineEdit(BftPopup)
        self.fuelWeightLineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.fuelWeightLineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.fuelWeightLineEdit.setObjectName(_fromUtf8("fuelWeightLineEdit"))
        self.horizontalLayout.addWidget(self.fuelWeightLineEdit)
        self.averEnrichLabel = QtGui.QLabel(BftPopup)
        self.averEnrichLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.averEnrichLabel.setObjectName(_fromUtf8("averEnrichLabel"))
        self.horizontalLayout.addWidget(self.averEnrichLabel)
        self.averEnrichLineEdit = QtGui.QLineEdit(BftPopup)
        self.averEnrichLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.averEnrichLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.averEnrichLineEdit.setObjectName(_fromUtf8("averEnrichLineEdit"))
        self.horizontalLayout.addWidget(self.averEnrichLineEdit)
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btfTabButton = QtGui.QPushButton(BftPopup)
        self.btfTabButton.setObjectName(_fromUtf8("btfTabButton"))
        self.horizontalLayout.addWidget(self.btfTabButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.filelinewidget = CaseLineWidget(BftPopup)
        self.filelinewidget.setObjectName(_fromUtf8("filelinewidget"))
        self.verticalLayout.addWidget(self.filelinewidget)
        spacerItem2 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.axialBtfCheckBox = QtGui.QCheckBox(BftPopup)
        self.axialBtfCheckBox.setObjectName(_fromUtf8("axialBtfCheckBox"))
        self.gridLayout.addWidget(self.axialBtfCheckBox, 0, 0, 1, 1)
        self.btfLibLabel = QtGui.QLabel(BftPopup)
        self.btfLibLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.btfLibLabel.setObjectName(_fromUtf8("btfLibLabel"))
        self.gridLayout.addWidget(self.btfLibLabel, 0, 2, 1, 1)
        self.btfLibComboBox = QtGui.QComboBox(BftPopup)
        self.btfLibComboBox.setObjectName(_fromUtf8("btfLibComboBox"))
        self.gridLayout.addWidget(self.btfLibComboBox, 0, 3, 1, 2)
        self.voidLabel = QtGui.QLabel(BftPopup)
        self.voidLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voidLabel.setObjectName(_fromUtf8("voidLabel"))
        self.gridLayout.addWidget(self.voidLabel, 0, 5, 1, 1)
        self.voidItem = QtGui.QComboBox(BftPopup)
        self.voidItem.setMaximumSize(QtCore.QSize(70, 16777215))
        self.voidItem.setObjectName(_fromUtf8("voidItem"))
        self.gridLayout.addWidget(self.voidItem, 0, 6, 1, 1)
        self.simplyfiedCheckBox = QtGui.QCheckBox(BftPopup)
        self.simplyfiedCheckBox.setObjectName(_fromUtf8("simplyfiedCheckBox"))
        self.gridLayout.addWidget(self.simplyfiedCheckBox, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.activeLengthLabel_3 = QtGui.QLabel(BftPopup)
        self.activeLengthLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.activeLengthLabel_3.setObjectName(_fromUtf8("activeLengthLabel_3"))
        self.gridLayout.addWidget(self.activeLengthLabel_3, 3, 2, 1, 2)
        self.comboBox_2 = QtGui.QComboBox(BftPopup)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 3, 4, 1, 1)
        self.CRTypeLabel = QtGui.QLabel(BftPopup)
        self.CRTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CRTypeLabel.setObjectName(_fromUtf8("CRTypeLabel"))
        self.gridLayout.addWidget(self.CRTypeLabel, 3, 5, 1, 1)
        self.CRtypeItem = QtGui.QComboBox(BftPopup)
        self.CRtypeItem.setMaximumSize(QtCore.QSize(70, 16777215))
        self.CRtypeItem.setObjectName(_fromUtf8("CRtypeItem"))
        self.gridLayout.addWidget(self.CRtypeItem, 3, 6, 1, 1)
        self.fillBurnupButton = QtGui.QPushButton(BftPopup)
        self.fillBurnupButton.setObjectName(_fromUtf8("fillBurnupButton"))
        self.gridLayout.addWidget(self.fillBurnupButton, 3, 7, 1, 1)
        self.sortCaseLinesButton = QtGui.QPushButton(BftPopup)
        self.sortCaseLinesButton.setObjectName(_fromUtf8("sortCaseLinesButton"))
        self.gridLayout.addWidget(self.sortCaseLinesButton, 0, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(17, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.crWidget = CRWidget(BftPopup)
        self.crWidget.setMinimumSize(QtCore.QSize(62, 230))
        self.crWidget.setObjectName(_fromUtf8("crWidget"))
        self.verticalLayout_2.addWidget(self.crWidget)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(BftPopup)
        QtCore.QMetaObject.connectSlotsByName(BftPopup)

    def retranslateUi(self, BftPopup):
        BftPopup.setWindowTitle(_translate("BftPopup", "BTF Popup", None))
        self.activeLengthLabel.setText(_translate("BftPopup", "Act. Length;", None))
        self.fuelWeightLabel.setText(_translate("BftPopup", "Weight:", None))
        self.averEnrichLabel.setText(_translate("BftPopup", "Enrich:", None))
        self.btfTabButton.setText(_translate("BftPopup", "BTF Tab...", None))
        self.axialBtfCheckBox.setText(_translate("BftPopup", "Axial BTF", None))
        self.btfLibLabel.setText(_translate("BftPopup", "BTF library:", None))
        self.voidLabel.setText(_translate("BftPopup", "Void:", None))
        self.simplyfiedCheckBox.setText(_translate("BftPopup", "Simplyfied", None))
        self.activeLengthLabel_3.setText(_translate("BftPopup", "Corner Protect.:", None))
        self.CRTypeLabel.setText(_translate("BftPopup", "Conrod:", None))
        self.fillBurnupButton.setText(_translate("BftPopup", "Bur. sync!", None))
        self.sortCaseLinesButton.setText(_translate("BftPopup", "Sort!", None))

from caseLineWidget import CaseLineWidget
from CRWidget import CRWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BftPopup = QtGui.QDialog()
    ui = Ui_BftPopup()
    ui.setupUi(BftPopup)
    BftPopup.show()
    sys.exit(app.exec_())

