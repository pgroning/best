# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optPopup.ui'
#
# Created: Wed Sep 23 20:45:39 2015
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

class Ui_OptimizePopup(object):
    def setupUi(self, OptimizePopup):
        OptimizePopup.setObjectName(_fromUtf8("OptimizePopup"))
        OptimizePopup.resize(331, 292)
        self.layoutWidget = QtGui.QWidget(OptimizePopup)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 268))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridlayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.optIncrButton = QtGui.QPushButton(self.layoutWidget)
        self.optIncrButton.setObjectName(_fromUtf8("optIncrButton"))
        self.gridlayout.addWidget(self.optIncrButton, 1, 0, 1, 1)
        self.optDecrButton = QtGui.QPushButton(self.layoutWidget)
        self.optDecrButton.setObjectName(_fromUtf8("optDecrButton"))
        self.gridlayout.addWidget(self.optDecrButton, 1, 1, 1, 1)
        self.optRadialButton = QtGui.QPushButton(self.layoutWidget)
        self.optRadialButton.setObjectName(_fromUtf8("optRadialButton"))
        self.gridlayout.addWidget(self.optRadialButton, 2, 0, 1, 1)
        self.stepCountLabel = QtGui.QLabel(self.layoutWidget)
        self.stepCountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stepCountLabel.setObjectName(_fromUtf8("stepCountLabel"))
        self.gridlayout.addWidget(self.stepCountLabel, 4, 0, 1, 3)
        self.stepCountSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.stepCountSpinBox.setMaximum(8)
        self.stepCountSpinBox.setObjectName(_fromUtf8("stepCountSpinBox"))
        self.gridlayout.addWidget(self.stepCountSpinBox, 4, 3, 1, 1)
        self.showStepsCheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.showStepsCheckBox.setObjectName(_fromUtf8("showStepsCheckBox"))
        self.gridlayout.addWidget(self.showStepsCheckBox, 5, 0, 1, 2)
        self.optStopButton = QtGui.QPushButton(self.layoutWidget)
        self.optStopButton.setObjectName(_fromUtf8("optStopButton"))
        self.gridlayout.addWidget(self.optStopButton, 5, 2, 1, 2)
        self.optBArodCheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.optBArodCheckBox.setObjectName(_fromUtf8("optBArodCheckBox"))
        self.gridlayout.addWidget(self.optBArodCheckBox, 6, 0, 1, 1)
        self.targetEnrichLabel = QtGui.QLabel(self.layoutWidget)
        self.targetEnrichLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.targetEnrichLabel.setObjectName(_fromUtf8("targetEnrichLabel"))
        self.gridlayout.addWidget(self.targetEnrichLabel, 6, 1, 1, 2)
        self.targetEnrichSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.targetEnrichSpinBox.setDecimals(3)
        self.targetEnrichSpinBox.setMaximum(4.999)
        self.targetEnrichSpinBox.setSingleStep(0.05)
        self.targetEnrichSpinBox.setObjectName(_fromUtf8("targetEnrichSpinBox"))
        self.gridlayout.addWidget(self.targetEnrichSpinBox, 6, 3, 1, 1)
        self.optFintCheckBox = QtGui.QCheckBox(self.layoutWidget)
        self.optFintCheckBox.setObjectName(_fromUtf8("optFintCheckBox"))
        self.gridlayout.addWidget(self.optFintCheckBox, 7, 0, 1, 1)
        self.maxFintLabel = QtGui.QLabel(self.layoutWidget)
        self.maxFintLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxFintLabel.setObjectName(_fromUtf8("maxFintLabel"))
        self.gridlayout.addWidget(self.maxFintLabel, 7, 1, 1, 2)
        self.maxFintSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.maxFintSpinBox.setDecimals(3)
        self.maxFintSpinBox.setMinimum(0.0)
        self.maxFintSpinBox.setMaximum(1.8)
        self.maxFintSpinBox.setSingleStep(0.05)
        self.maxFintSpinBox.setProperty("value", 1.3)
        self.maxFintSpinBox.setObjectName(_fromUtf8("maxFintSpinBox"))
        self.gridlayout.addWidget(self.maxFintSpinBox, 7, 3, 1, 1)
        self.optIncrAllButton = QtGui.QPushButton(self.layoutWidget)
        self.optIncrAllButton.setObjectName(_fromUtf8("optIncrAllButton"))
        self.gridlayout.addWidget(self.optIncrAllButton, 1, 2, 1, 2)
        self.showBtfEnvelopPopup = QtGui.QPushButton(self.layoutWidget)
        self.showBtfEnvelopPopup.setObjectName(_fromUtf8("showBtfEnvelopPopup"))
        self.gridlayout.addWidget(self.showBtfEnvelopPopup, 8, 1, 1, 1)
        self.showFintEnvelopPopup = QtGui.QPushButton(self.layoutWidget)
        self.showFintEnvelopPopup.setObjectName(_fromUtf8("showFintEnvelopPopup"))
        self.gridlayout.addWidget(self.showFintEnvelopPopup, 8, 2, 1, 2)
        self.optBothButton = QtGui.QPushButton(self.layoutWidget)
        self.optBothButton.setObjectName(_fromUtf8("optBothButton"))
        self.gridlayout.addWidget(self.optBothButton, 3, 1, 1, 1)
        self.optEnrichAllButton = QtGui.QPushButton(self.layoutWidget)
        self.optEnrichAllButton.setObjectName(_fromUtf8("optEnrichAllButton"))
        self.gridlayout.addWidget(self.optEnrichAllButton, 2, 2, 1, 2)
        self.optEnrichButton = QtGui.QPushButton(self.layoutWidget)
        self.optEnrichButton.setObjectName(_fromUtf8("optEnrichButton"))
        self.gridlayout.addWidget(self.optEnrichButton, 2, 1, 1, 1)

        self.retranslateUi(OptimizePopup)
        QtCore.QMetaObject.connectSlotsByName(OptimizePopup)

    def retranslateUi(self, OptimizePopup):
        OptimizePopup.setWindowTitle(_translate("OptimizePopup", "Optimization Popup", None))
        self.optIncrButton.setToolTip(_translate("OptimizePopup", "Increase enrichment in best rod", None))
        self.optIncrButton.setText(_translate("OptimizePopup", "Opt. Increase", None))
        self.optDecrButton.setToolTip(_translate("OptimizePopup", "Decrease enrichment in worst rod", None))
        self.optDecrButton.setText(_translate("OptimizePopup", "Opt. Decrease", None))
        self.optRadialButton.setToolTip(_translate("OptimizePopup", "Optimize the radial distribution of enrichments", None))
        self.optRadialButton.setText(_translate("OptimizePopup", "Opt. Radial", None))
        self.stepCountLabel.setText(_translate("OptimizePopup", "Number of Optimizing Steps:", None))
        self.showStepsCheckBox.setText(_translate("OptimizePopup", "Show Opt. Steps", None))
        self.optStopButton.setText(_translate("OptimizePopup", "STOP", None))
        self.optBArodCheckBox.setText(_translate("OptimizePopup", "Opt. BA rod", None))
        self.targetEnrichLabel.setText(_translate("OptimizePopup", "Target enrichment:", None))
        self.optFintCheckBox.setText(_translate("OptimizePopup", "Opt. Fint", None))
        self.maxFintLabel.setText(_translate("OptimizePopup", "Maximum Fint:", None))
        self.optIncrAllButton.setToolTip(_translate("OptimizePopup", "Increase enrichment in all rods", None))
        self.optIncrAllButton.setText(_translate("OptimizePopup", "All Increase", None))
        self.showBtfEnvelopPopup.setText(_translate("OptimizePopup", "BTF Envelop...", None))
        self.showFintEnvelopPopup.setText(_translate("OptimizePopup", "Fint Envelop...", None))
        self.optBothButton.setText(_translate("OptimizePopup", "Opt. Both", None))
        self.optEnrichAllButton.setText(_translate("OptimizePopup", "Opt. Enr. All", None))
        self.optEnrichButton.setText(_translate("OptimizePopup", "Opt. Enrich.", None))

