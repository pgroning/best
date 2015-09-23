# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'writeBtfTab.ui'
#
# Created: Wed Sep 23 20:41:35 2015
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

class Ui_btfTabDialog(object):
    def setupUi(self, btfTabDialog):
        btfTabDialog.setObjectName(_fromUtf8("btfTabDialog"))
        btfTabDialog.resize(556, 89)
        self.layoutWidget = QtGui.QWidget(btfTabDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 539, 65))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.defaultFilePushButton = QtGui.QPushButton(self.layoutWidget)
        self.defaultFilePushButton.setObjectName(_fromUtf8("defaultFilePushButton"))
        self.hboxlayout.addWidget(self.defaultFilePushButton)
        self.s3TabRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.s3TabRadioButton.setObjectName(_fromUtf8("s3TabRadioButton"))
        self.hboxlayout.addWidget(self.s3TabRadioButton)
        self.p4TabRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.p4TabRadioButton.setObjectName(_fromUtf8("p4TabRadioButton"))
        self.hboxlayout.addWidget(self.p4TabRadioButton)
        self.p7TabRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.p7TabRadioButton.setObjectName(_fromUtf8("p7TabRadioButton"))
        self.hboxlayout.addWidget(self.p7TabRadioButton)
        spacerItem = QtGui.QSpacerItem(41, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.conrodCheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.conrodCheckBox.setObjectName(_fromUtf8("conrodCheckBox"))
        self.hboxlayout.addWidget(self.conrodCheckBox)
        self.writePushButton = QtGui.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/stock-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.writePushButton.setIcon(icon)
        self.writePushButton.setObjectName(_fromUtf8("writePushButton"))
        self.hboxlayout.addWidget(self.writePushButton)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.tabFileLineWidget = FileLineWidget(self.layoutWidget)
        self.tabFileLineWidget.setObjectName(_fromUtf8("tabFileLineWidget"))
        self.vboxlayout.addWidget(self.tabFileLineWidget)

        self.retranslateUi(btfTabDialog)
        QtCore.QMetaObject.connectSlotsByName(btfTabDialog)

    def retranslateUi(self, btfTabDialog):
        btfTabDialog.setWindowTitle(_translate("btfTabDialog", "Write BTF Tables", None))
        self.defaultFilePushButton.setToolTip(_translate("btfTabDialog", "Sets a default filename", None))
        self.defaultFilePushButton.setText(_translate("btfTabDialog", "Default File Name", None))
        self.s3TabRadioButton.setToolTip(_translate("btfTabDialog", "Choose Simulate3 table format", None))
        self.s3TabRadioButton.setText(_translate("btfTabDialog", "s3", None))
        self.p4TabRadioButton.setToolTip(_translate("btfTabDialog", "Choose Polca4 table format", None))
        self.p4TabRadioButton.setText(_translate("btfTabDialog", "p4", None))
        self.p7TabRadioButton.setToolTip(_translate("btfTabDialog", "Choose Polca7 table format", None))
        self.p7TabRadioButton.setText(_translate("btfTabDialog", "p7", None))
        self.conrodCheckBox.setToolTip(_translate("btfTabDialog", "If this is marked:<br>The written tables will be calculated<br>as a funktion of control rod presence", None))
        self.conrodCheckBox.setText(_translate("btfTabDialog", "Conrod", None))
        self.writePushButton.setToolTip(_translate("btfTabDialog", "Write the BTF (R-fact) tables in<br>filename given below", None))
        self.writePushButton.setText(_translate("btfTabDialog", "Write BTF Table", None))

from fileLineWidget import FileLineWidget
import CuteBird_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    btfTabDialog = QtGui.QDialog()
    ui = Ui_btfTabDialog()
    ui.setupUi(btfTabDialog)
    btfTabDialog.show()
    sys.exit(app.exec_())

