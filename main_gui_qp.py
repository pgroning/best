#!/usr/bin/python

from IPython.core.debugger import Tracer

import sys, os
from PyQt4 import QtGui, QtCore
import numpy as np

from pyDraw import Bundle

class MainWin(QtGui.QMainWindow):

    def __init__(self):
        super(MainWin, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Main Window')
        self.resize(1100,620)
        self.move(200,200)

        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()
        self.create_mainframe()

        self.resizeEvent = self.on_resize

    def on_resize(self,event):        
        self.bundle.setGeometry(0,0,self.width()*0.55,self.height()*0.8)


    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        quit_action = self.create_action("&Quit", slot=self.close, 
                                         shortcut="Ctrl+Q", tip="Close the application")

        self.add_actions(self.file_menu,(quit_action,None))


    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QtGui.QAction(text, self)
        if icon is not None:
            action.setIcon(QtGui.QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, QtCore.SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
        

    def create_toolbar(self):
        fileAction = QtGui.QAction(QtGui.QIcon('icons/open-file-icon_32x32.png'), 'Open file', self)
        fileAction.setStatusTip('Open file')
        #fileAction.triggered.connect(self.openFile)

        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(fileAction)

    def create_statusbar(self):
        self.status_text = QtGui.QLabel("Main window")
        self.statusBar().addWidget(self.status_text, 1)


    def create_mainframe(self):
        self.main_frame = QtGui.QWidget()

        # Define Bundle fuel map
        self.bundle_widget = QtGui.QWidget()
        self.bundle_widget.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        #self.bundle_widget.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.MinimumExpanding)
        self.bundle = Bundle(self.bundle_widget)
        
        bundle_box = QtGui.QVBoxLayout()
        bundle_box.addWidget(self.bundle_widget)
        
        bundle_gbox = QtGui.QGroupBox()
        bundle_gbox.setStyleSheet("QGroupBox { background-color: rgb(200, 200,\
        200); border:1px solid gray; border-radius:5px;}")
        bundle_gbox.setLayout(bundle_box)

        # -- Define table widget --
        self.table = QtGui.QTableWidget()
        self.table.setRowCount(100)
        self.table.setColumnCount(4)
        #self.table.verticalHeader().hide()
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #self.table.setMinimumWidth(180)
        self.table.setSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        self.table.setHorizontalHeaderLabels(('Coord','EXP','FINT','BTF'))
        self.table.setSortingEnabled(True)
        self.table.setColumnHidden(0,True)

        tvbox = QtGui.QVBoxLayout()
        tvbox.addWidget(self.table)
        tableGbox = QtGui.QGroupBox()
        tableGbox.setStyleSheet("QGroupBox { background-color: rgb(200, 200,\
        200); border:1px solid gray; border-radius:5px;}")
        tableGbox.setLayout(tvbox)

        # --------------------------------------

        param_label = QtGui.QLabel('Parameter:')
        self.param_cbox = QtGui.QComboBox()
        paramlist = ['ENR','FINT','EXP','BTF','BTFP','XFL1','XFL2','ROD','LOCK']
        for i in paramlist:
            self.param_cbox.addItem(i)
        #self.connect(self.param_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)
        param_hbox = QtGui.QHBoxLayout()
        param_hbox.addWidget(param_label)
        param_hbox.addWidget(self.param_cbox)
        #self.connect(self.param_cbox, QtCore.SIGNAL('currentIndexChanged(int)'), self.set_pinvalues)

        case_label = QtGui.QLabel('Case number:')
        self.case_cbox = QtGui.QComboBox()
        caselist = ['1', '2', '3']
        for i in caselist:
            self.case_cbox.addItem(i)
        case_hbox = QtGui.QHBoxLayout()
        case_hbox.addWidget(case_label)
        case_hbox.addWidget(self.case_cbox)
        #self.connect(self.case_cbox, SIGNAL('currentIndexChanged(int)'), self.set_pinvalues)
        #self.connect(self.case_cbox, QtCore.SIGNAL('currentIndexChanged(int)'), self.fig_update)

        point_label = QtGui.QLabel('Point number:')
        self.point_sbox = QtGui.QSpinBox()
        self.point_sbox.setMinimum(0)
        self.point_sbox.setMaximum(10000)
        point_hbox = QtGui.QHBoxLayout()
        point_hbox.addWidget(point_label)
        point_hbox.addWidget(self.point_sbox)
        #self.connect(self.point_sbox, SIGNAL('valueChanged(int)'), self.set_pinvalues)

        self.enr_plus_button = QtGui.QPushButton("+ enr")
        self.enr_minus_button = QtGui.QPushButton("- enr")
        enr_hbox = QtGui.QHBoxLayout()
        enr_hbox.addWidget(self.enr_minus_button)
        enr_hbox.addWidget(self.enr_plus_button)
        #self.connect(self.enr_plus_button, SIGNAL('clicked()'), self.draw_fuelmap)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(param_hbox)
        vbox.addLayout(case_hbox)
        vbox.addLayout(point_hbox)
        vbox.addLayout(enr_hbox)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        vbox.addItem(spacerItem)

        Tracer()()
        groupbox = QtGui.QGroupBox()
        groupbox.setStyleSheet("QGroupBox { background-color: rgb(200, 200,\
        200); border:1px solid gray; border-radius:5px;}")
        groupbox.setLayout(vbox)
        groupbox.setSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)

        # --------------------------------------------

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(groupbox)
        hbox.addWidget(bundle_gbox)
        hbox.addWidget(tableGbox)

        self.main_frame.setLayout(hbox)
        self.setCentralWidget(self.main_frame)

        



def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWin()
    window.show()
    #app.exec_()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
