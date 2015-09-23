# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enrPopup.ui'
#
# Created: Wed Sep 23 20:38:29 2015
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

class Ui_EnrDialog(object):
    def setupUi(self, EnrDialog):
        EnrDialog.setObjectName(_fromUtf8("EnrDialog"))
        EnrDialog.resize(316, 298)
        self.layoutWidget = QtGui.QWidget(EnrDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 302, 266))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridlayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.u235Label = QtGui.QLabel(self.layoutWidget)
        self.u235Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.u235Label.setObjectName(_fromUtf8("u235Label"))
        self.gridlayout.addWidget(self.u235Label, 1, 0, 1, 1)
        self.u235DoubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.u235DoubleSpinBox.setDecimals(3)
        self.u235DoubleSpinBox.setMinimum(0.71)
        self.u235DoubleSpinBox.setMaximum(5.0)
        self.u235DoubleSpinBox.setSingleStep(0.05)
        self.u235DoubleSpinBox.setProperty("value", 2.0)
        self.u235DoubleSpinBox.setObjectName(_fromUtf8("u235DoubleSpinBox"))
        self.gridlayout.addWidget(self.u235DoubleSpinBox, 1, 1, 1, 1)
        self.pufissLabel = QtGui.QLabel(self.layoutWidget)
        self.pufissLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pufissLabel.setObjectName(_fromUtf8("pufissLabel"))
        self.gridlayout.addWidget(self.pufissLabel, 1, 2, 1, 1)
        self.pufissDoubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.pufissDoubleSpinBox.setDecimals(3)
        self.pufissDoubleSpinBox.setMinimum(0.0)
        self.pufissDoubleSpinBox.setMaximum(9.0)
        self.pufissDoubleSpinBox.setSingleStep(0.05)
        self.pufissDoubleSpinBox.setProperty("value", 0.0)
        self.pufissDoubleSpinBox.setObjectName(_fromUtf8("pufissDoubleSpinBox"))
        self.gridlayout.addWidget(self.pufissDoubleSpinBox, 1, 3, 1, 1)
        self.gd2o3Label = QtGui.QLabel(self.layoutWidget)
        self.gd2o3Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gd2o3Label.setObjectName(_fromUtf8("gd2o3Label"))
        self.gridlayout.addWidget(self.gd2o3Label, 2, 0, 1, 1)
        self.gd2o3DoubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.gd2o3DoubleSpinBox.setDecimals(3)
        self.gd2o3DoubleSpinBox.setMaximum(9.99)
        self.gd2o3DoubleSpinBox.setSingleStep(0.05)
        self.gd2o3DoubleSpinBox.setObjectName(_fromUtf8("gd2o3DoubleSpinBox"))
        self.gridlayout.addWidget(self.gd2o3DoubleSpinBox, 2, 1, 1, 1)
        self.sortEnrButton = QtGui.QPushButton(self.layoutWidget)
        self.sortEnrButton.setObjectName(_fromUtf8("sortEnrButton"))
        self.gridlayout.addWidget(self.sortEnrButton, 2, 2, 1, 2)
        self.standardEnrLabel = QtGui.QLabel(self.layoutWidget)
        self.standardEnrLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.standardEnrLabel.setObjectName(_fromUtf8("standardEnrLabel"))
        self.gridlayout.addWidget(self.standardEnrLabel, 3, 0, 1, 3)
        self.standardEnrComboBox = QtGui.QComboBox(self.layoutWidget)
        self.standardEnrComboBox.setObjectName(_fromUtf8("standardEnrComboBox"))
        self.gridlayout.addWidget(self.standardEnrComboBox, 3, 3, 1, 1)
        self.standardGdLabel = QtGui.QLabel(self.layoutWidget)
        self.standardGdLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.standardGdLabel.setObjectName(_fromUtf8("standardGdLabel"))
        self.gridlayout.addWidget(self.standardGdLabel, 4, 0, 1, 3)
        self.standardGdComboBox = QtGui.QComboBox(self.layoutWidget)
        self.standardGdComboBox.setObjectName(_fromUtf8("standardGdComboBox"))
        self.gridlayout.addWidget(self.standardGdComboBox, 4, 3, 1, 1)
        self.companyLabel = QtGui.QLabel(self.layoutWidget)
        self.companyLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.companyLabel.setObjectName(_fromUtf8("companyLabel"))
        self.gridlayout.addWidget(self.companyLabel, 5, 0, 1, 3)
        self.companyComboBox = QtGui.QComboBox(self.layoutWidget)
        self.companyComboBox.setObjectName(_fromUtf8("companyComboBox"))
        self.companyComboBox.addItem(_fromUtf8(""))
        self.companyComboBox.addItem(_fromUtf8(""))
        self.companyComboBox.addItem(_fromUtf8(""))
        self.companyComboBox.addItem(_fromUtf8(""))
        self.gridlayout.addWidget(self.companyComboBox, 5, 3, 1, 1)
        self.addEnrButton = QtGui.QPushButton(self.layoutWidget)
        self.addEnrButton.setObjectName(_fromUtf8("addEnrButton"))
        self.gridlayout.addWidget(self.addEnrButton, 6, 0, 1, 2)
        self.deleteEnrButton = QtGui.QPushButton(self.layoutWidget)
        self.deleteEnrButton.setObjectName(_fromUtf8("deleteEnrButton"))
        self.gridlayout.addWidget(self.deleteEnrButton, 6, 2, 1, 2)
        self.enrButtonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.enrButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.enrButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.enrButtonBox.setObjectName(_fromUtf8("enrButtonBox"))
        self.gridlayout.addWidget(self.enrButtonBox, 7, 0, 1, 4)
        self.indexLabel = QtGui.QLabel(self.layoutWidget)
        self.indexLabel.setTextFormat(QtCore.Qt.RichText)
        self.indexLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.indexLabel.setIndent(1)
        self.indexLabel.setObjectName(_fromUtf8("indexLabel"))
        self.gridlayout.addWidget(self.indexLabel, 0, 1, 1, 2)
        self.indexSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.indexSpinBox.setMinimum(1)
        self.indexSpinBox.setMaximum(16)
        self.indexSpinBox.setObjectName(_fromUtf8("indexSpinBox"))
        self.gridlayout.addWidget(self.indexSpinBox, 0, 3, 1, 1)
        self.lockEnrButton = QtGui.QPushButton(self.layoutWidget)
        self.lockEnrButton.setObjectName(_fromUtf8("lockEnrButton"))
        self.gridlayout.addWidget(self.lockEnrButton, 0, 0, 1, 1)

        self.retranslateUi(EnrDialog)
        QtCore.QObject.connect(self.enrButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EnrDialog.accept)
        QtCore.QObject.connect(self.enrButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EnrDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EnrDialog)

    def retranslateUi(self, EnrDialog):
        EnrDialog.setWindowTitle(_translate("EnrDialog", "EnrichmentDialog", None))
        self.u235Label.setText(_translate("EnrDialog", "U-235:", None))
        self.pufissLabel.setText(_translate("EnrDialog", "Pu-fiss:", None))
        self.gd2o3Label.setText(_translate("EnrDialog", "Gd2O3:", None))
        self.sortEnrButton.setToolTip(_translate("EnrDialog", "Sort the enrichments in increasing values", None))
        self.sortEnrButton.setText(_translate("EnrDialog", "Sort enrichments", None))
        self.standardEnrLabel.setText(_translate("EnrDialog", "Standard enrichments:", None))
        self.standardGdLabel.setText(_translate("EnrDialog", "Standard BA contents", None))
        self.companyLabel.setText(_translate("EnrDialog", "Company:", None))
        self.companyComboBox.setToolTip(_translate("EnrDialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose a fuel vendor to use the set of standard enrichments used by that company</p></body></html>", None))
        self.companyComboBox.setItemText(0, _translate("EnrDialog", "WSE", None))
        self.companyComboBox.setItemText(1, _translate("EnrDialog", "Areva", None))
        self.companyComboBox.setItemText(2, _translate("EnrDialog", "GNF", None))
        self.companyComboBox.setItemText(3, _translate("EnrDialog", "Other", None))
        self.addEnrButton.setToolTip(_translate("EnrDialog", "Add another enrichment to the design<br>This is done for all the axial levels<br>selected in the BtfPopup", None))
        self.addEnrButton.setText(_translate("EnrDialog", "Add enrichment", None))
        self.deleteEnrButton.setToolTip(_translate("EnrDialog", "Delete the selected enrichment level<br>This is done for all the axial levels<br>selected in the BtfPopup", None))
        self.deleteEnrButton.setText(_translate("EnrDialog", "Delete enrichment", None))
        self.enrButtonBox.setToolTip(_translate("EnrDialog", "\"OK\" to change the enrichment<br>and close this popup<br>\"Apply\" to change the enricment<br>\"Cancel\" to close popup without changeing the enrichment", None))
        self.indexLabel.setText(_translate("EnrDialog", "Enrichment index:", None))
        self.lockEnrButton.setText(_translate("EnrDialog", "Lock", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EnrDialog = QtGui.QDialog()
    ui = Ui_EnrDialog()
    ui.setupUi(EnrDialog)
    EnrDialog.show()
    sys.exit(app.exec_())

