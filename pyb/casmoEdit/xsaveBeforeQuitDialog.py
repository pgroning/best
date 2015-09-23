# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveBeforeQuitDialog.ui'
#
# Created: Wed Sep 23 20:35:42 2015
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

class Ui_SaveBeforeQuitDialog(object):
    def setupUi(self, SaveBeforeQuitDialog):
        SaveBeforeQuitDialog.setObjectName(_fromUtf8("SaveBeforeQuitDialog"))
        SaveBeforeQuitDialog.resize(266, 145)
        self.layoutWidget = QtGui.QWidget(SaveBeforeQuitDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 130))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.vboxlayout.setSpacing(4)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.warningLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.warningLabel.setFont(font)
        self.warningLabel.setTextFormat(QtCore.Qt.PlainText)
        self.warningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warningLabel.setObjectName(_fromUtf8("warningLabel"))
        self.vboxlayout.addWidget(self.warningLabel)
        self.modifiedLabel = QtGui.QLabel(self.layoutWidget)
        self.modifiedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.modifiedLabel.setObjectName(_fromUtf8("modifiedLabel"))
        self.vboxlayout.addWidget(self.modifiedLabel)
        self.file_nameLabel = QtGui.QLabel(self.layoutWidget)
        self.file_nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.file_nameLabel.setObjectName(_fromUtf8("file_nameLabel"))
        self.vboxlayout.addWidget(self.file_nameLabel)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout.addWidget(self.label)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(41, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.hboxlayout.addWidget(self.buttonBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(SaveBeforeQuitDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SaveBeforeQuitDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SaveBeforeQuitDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveBeforeQuitDialog)

    def retranslateUi(self, SaveBeforeQuitDialog):
        SaveBeforeQuitDialog.setWindowTitle(_translate("SaveBeforeQuitDialog", "Dialog", None))
        self.warningLabel.setText(_translate("SaveBeforeQuitDialog", "Warning!", None))
        self.modifiedLabel.setText(_translate("SaveBeforeQuitDialog", "The file has been modified!", None))
        self.file_nameLabel.setText(_translate("SaveBeforeQuitDialog", "filename", None))
        self.label.setText(_translate("SaveBeforeQuitDialog", "Do you want to save the file before quit?", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SaveBeforeQuitDialog = QtGui.QDialog()
    ui = Ui_SaveBeforeQuitDialog()
    ui.setupUi(SaveBeforeQuitDialog)
    SaveBeforeQuitDialog.show()
    sys.exit(app.exec_())

