# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'casmoEdit.ui'
#
# Created: Wed Sep 23 20:35:15 2015
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

class Ui_CasmoEdit(object):
    def setupUi(self, CasmoEdit):
        CasmoEdit.setObjectName(_fromUtf8("CasmoEdit"))
        CasmoEdit.resize(742, 557)
        CasmoEdit.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.verticalLayout = QtGui.QVBoxLayout(CasmoEdit)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fileTypeLabel = QtGui.QLabel(CasmoEdit)
        self.fileTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fileTypeLabel.setObjectName(_fromUtf8("fileTypeLabel"))
        self.gridLayout.addWidget(self.fileTypeLabel, 0, 0, 1, 1)
        self.fileTypeChoice = QtGui.QComboBox(CasmoEdit)
        self.fileTypeChoice.setObjectName(_fromUtf8("fileTypeChoice"))
        self.gridLayout.addWidget(self.fileTypeChoice, 0, 1, 1, 1)
        self.findButton = QtGui.QToolButton(CasmoEdit)
        self.findButton.setMinimumSize(QtCore.QSize(0, 27))
        self.findButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.gridLayout.addWidget(self.findButton, 0, 2, 1, 1)
        self.findPrevButton = QtGui.QPushButton(CasmoEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(41)
        sizePolicy.setVerticalStretch(27)
        sizePolicy.setHeightForWidth(self.findPrevButton.sizePolicy().hasHeightForWidth())
        self.findPrevButton.setSizePolicy(sizePolicy)
        self.findPrevButton.setMinimumSize(QtCore.QSize(41, 27))
        self.findPrevButton.setMaximumSize(QtCore.QSize(41, 16777215))
        self.findPrevButton.setObjectName(_fromUtf8("findPrevButton"))
        self.gridLayout.addWidget(self.findPrevButton, 0, 3, 1, 1)
        self.findLineEdit = QtGui.QLineEdit(CasmoEdit)
        self.findLineEdit.setDragEnabled(True)
        self.findLineEdit.setObjectName(_fromUtf8("findLineEdit"))
        self.gridLayout.addWidget(self.findLineEdit, 0, 4, 1, 1)
        self.findAllButton = QtGui.QPushButton(CasmoEdit)
        self.findAllButton.setMaximumSize(QtCore.QSize(64, 16777215))
        self.findAllButton.setObjectName(_fromUtf8("findAllButton"))
        self.gridLayout.addWidget(self.findAllButton, 0, 5, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(CasmoEdit)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 0, 7, 1, 1)
        self.replaceButton = QtGui.QToolButton(CasmoEdit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replaceButton.sizePolicy().hasHeightForWidth())
        self.replaceButton.setSizePolicy(sizePolicy)
        self.replaceButton.setMinimumSize(QtCore.QSize(0, 27))
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.gridLayout.addWidget(self.replaceButton, 1, 2, 1, 2)
        self.replaceLineEdit = QtGui.QLineEdit(CasmoEdit)
        self.replaceLineEdit.setObjectName(_fromUtf8("replaceLineEdit"))
        self.gridLayout.addWidget(self.replaceLineEdit, 1, 4, 1, 1)
        self.undoButton = QtGui.QToolButton(CasmoEdit)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon)
        self.undoButton.setIconSize(QtCore.QSize(22, 22))
        self.undoButton.setObjectName(_fromUtf8("undoButton"))
        self.gridLayout.addWidget(self.undoButton, 1, 5, 1, 1)
        self.redoButton = QtGui.QToolButton(CasmoEdit)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon1)
        self.redoButton.setIconSize(QtCore.QSize(22, 22))
        self.redoButton.setObjectName(_fromUtf8("redoButton"))
        self.gridLayout.addWidget(self.redoButton, 1, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.textEdit = MyTextEdit(CasmoEdit)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(CasmoEdit)
        QtCore.QMetaObject.connectSlotsByName(CasmoEdit)

    def retranslateUi(self, CasmoEdit):
        CasmoEdit.setWindowTitle(_translate("CasmoEdit", "Dialog", None))
        self.fileTypeLabel.setText(_translate("CasmoEdit", "File type:", None))
        self.findButton.setText(_translate("CasmoEdit", "Find", None))
        self.findPrevButton.setText(_translate("CasmoEdit", "Prev.", None))
        self.findAllButton.setText(_translate("CasmoEdit", "FindAll", None))
        self.replaceButton.setText(_translate("CasmoEdit", "Replace", None))
        self.undoButton.setText(_translate("CasmoEdit", "...", None))
        self.redoButton.setText(_translate("CasmoEdit", "...", None))

from myTextEdit import MyTextEdit
import CuteBird_rc
