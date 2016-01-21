"""
This demo demonstrates how to embed a matplotlib (mpl) plot 
into a PyQt4 GUI application, including:
* Using the navigation toolbar
* Adding data to the plot
* Dynamically modifying the plot's properties
* Processing mpl events
* Saving the plot to a file from a menu
The main goal is to serve as a basis for developing rich PyQt GUI
applications featuring mpl plots (using the mpl OO API).
Eli Bendersky (eliben@gmail.com)
License: this code is in the public domain
Last modified: 19.01.2009
"""

from IPython.core.debugger import Tracer

import sys, os#, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4 import QtGui, QtCore

import numpy as np

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
#from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

from casio import casio

from pyDraw import Bundle


class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Main Window')
        self.move(300,200)

        # Retrieve initial data
        self.data_init()
        self.case_id_current = 0

        self.create_menu()
        self.create_toolbar()
        self.create_main_frame()
        self.create_status_bar()

        #self.textbox.setText('1 2 3 4')
        #self.data_init()
        
        #self.case_cbox.setCurrentIndex(0) # Set default plot case
        #self.case_id_current = 0
        #self.on_plot() # Init plot
        self.on_draw()
        self.draw_fuelmap()
        #Tracer()()

    def data_init(self):
        self.cas = casio()
        self.cas.loadpic('caxfiles.p')


    def setpincoords(self):
        self.xlist = ('01','02','03','04','05','06','07','08','09','10')
        self.ylist  = ('A','B','C','D','E','F','G','H','I','J')

        for i,y in enumerate(self.ylist):
            for j,x in enumerate(self.xlist):
                pin = y + x
                row = 10*i + j
                #print row,pin
                item = QTableWidgetItem(pin)
                self.table.setItem(row,0,item)
                self.table.setItem(row,1,QTableWidgetItem(str(0)))

       #pinlist = ('A01','A02','A03','A04','A05','A06','A07','A08','A09','A10')
       # for row,pin in enumerate(pinlist):
       #     item = QTableWidgetItem(pin)
       #     self.table.setItem(row,0,item)
       #     self.table.setItem(row,1,QTableWidgetItem(str(0)))

    def plot_kinf(self,case_id):

        case = self.cas.cases[case_id]
        idx0 = self.startpoint(case_id)
        statepts = case.statepts[idx0:]

        burnup_old = 0.0
        for idx,p in enumerate(statepts):
            if p.burnup < burnup_old:
                break
            burnup_old = p.burnup
        
        x = [statepts[i].burnup for i in range(idx)]
        y = [statepts[i].kinf for i in range(idx)]

        labstr = self.cas.cases[case_id].data.caxfile
        labstr = os.path.split(labstr)[1]
        labstr = os.path.splitext(labstr)[0]

        self.axes.plot(x,y,label=labstr)
        self.axes.set_xlabel('Burnup (MWd/kgU)')
        self.axes.set_ylabel('K-inf')
        self.axes.legend(loc='best',prop={'size':8})
        self.canvas.draw()
        self.on_draw()

    def plot_fint(self,case_id):

        case = self.cas.cases[case_id]
        idx0 = self.startpoint(case_id)
        statepts = case.statepts[idx0:]

        burnup_old = 0.0
        for idx,p in enumerate(statepts):
            if p.burnup < burnup_old:
                break
            burnup_old = p.burnup

        x = [statepts[i].burnup for i in range(idx)]
        y = [statepts[i].fint for i in range(idx)]

        labstr = case.data.caxfile
        labstr = os.path.split(labstr)[1]
        labstr = os.path.splitext(labstr)[0]
        
        self.axes.plot(x,y,label=labstr)
        self.axes.set_xlabel('Burnup (MWd/kgU)')
        self.axes.set_ylabel('Fint')
        self.axes.legend(loc='best',prop={'size':8})
        self.canvas.draw()
        self.on_draw()

    def plot_btf(self,case_id):
        print "BTF"
        
        self.axes.set_xlabel('Burnup (MWd/kgU)')
        self.axes.set_ylabel('BTF')
        self.on_draw()

    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"
        
        path = unicode(QFileDialog.getSaveFileName(self, 
                        'Save file', '', 
                        file_choices))
        if path:
            self.canvas.print_figure(path, dpi=self.dpi)
            self.statusBar().showMessage('Saved to %s' % path, 2000)
    
    def on_about(self):
        msg = """ A demo of using PyQt with matplotlib:
        
         * Use the matplotlib navigation bar
         * Add values to the text box and press Enter (or click "Draw")
         * Show or hide the grid
         * Drag the slider to modify the width of the bars
         * Save the plot to a file using the File menu
         * Click on a bar to receive an informative message
        """
        QMessageBox.about(self, "About the demo", msg.strip())
    
    def on_click(self, event):
        # The event received here is of the type
        # matplotlib.backend_bases.PickEvent
        #
        # It carries lots of information, of which we're using
        # only a small amount here.
        # 
        #box_points = event.artist.get_bbox().get_points()
        #msg = "You've clicked on a bar with coords:\n %s" % box_points
        
        #QMessageBox.information(self, "Click!", "You clicked me!")
        #print event.x,event.y
        if event.button is 1:
            print event.xdata, event.ydata

    def on_draw(self):
        """ Redraws the figure
        """

        # clear the axes and redraw the plot anew
        #
        self.axes.clear()
        self.axes.axis('equal')
        #self.axes.set_xlim(0,1)
        #self.axes.set_ylim(0,1)
        #self.axes.axis('equal')
        
        #self.axes.set_position([0,0,1,1])
        self.axes.set_xlim(0,1.2)
        self.axes.set_ylim(0,1)
        self.axes.set_position([0,0,1,1])
        #self.axes.set_visible(False)
        self.axes.set_frame_on(False)
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)
       
        #self.axes.grid(self.grid_cb.isChecked())

        #xmax = self.slider.value()
        #self.axes.set_xlim(0,xmax)

        #self.axes.axis('equal')

        #Tracer()()
        
        self.canvas.draw()

    def draw_fuelmap(self):

        # Draw a rectangle
        rect = mpatches.Rectangle((0.035,0.035), 0.935, 0.935, fc=(0.8,0.898,1),ec=(0.3, 0.3, 0.3))
        self.axes.add_patch(rect)


        # a fancy box with round corners. pad=0.1
        p_fancy = mpatches.FancyBboxPatch((0.12, 0.12),
                                 0.77, 0.77,
                                 boxstyle="round,pad=0.04",
                                 fc=(0.85,1,1),
                                 ec=(0.3, 0.3, 0.3))
        p_fancy.set_linewidth(4.0)
        self.axes.add_patch(p_fancy)

        # Draw water channel
        #rect = mpatches.Rectangle((0,0), 0.2, 0.2, fc=(0.8,0.898,1),ec=(0.3, 0.3, 0.3))

        #rot45=mpatches.transforms.Affine2D().rotate_deg(-45) + self.axes.transData
        #rect.set_transform(rot45)
        #self.axes.add_patch(rect)
        
        # Draw water cross
        pp = [[0.09, 0.503], [0.15, 0.515], [0.3, 0.515], [0.36, 0.503], [0.38, 0.503],
              [0.38, 0.497], [0.36, 0.497], [0.3, 0.485], [0.15, 0.485], [0.09, 0.497]]
        poly = mpatches.Polygon(pp)
        poly.set_facecolor((0.8,0.898,1))
        poly.set_linewidth(1.5)
        poly.set_closed(False)
        self.axes.add_patch(poly)

        pp = [[0.92, 0.503], [0.86, 0.515], [0.71, 0.515], [0.65, 0.503], [0.63, 0.503],
              [0.63, 0.497], [0.65, 0.497], [0.71, 0.485], [0.86, 0.485], [0.92, 0.497]]
        poly = mpatches.Polygon(pp)
        poly.set_facecolor((0.8,0.898,1))
        poly.set_linewidth(1.5)
        poly.set_closed(False)
        self.axes.add_patch(poly)

        pp = [[0.497, 0.09], [0.485, 0.15], [0.485, 0.3], [0.497, 0.36], [0.497, 0.38],
              [0.503, 0.38], [0.503, 0.36], [0.515, 0.3], [0.515, 0.15], [0.503, 0.09]]
        poly = mpatches.Polygon(pp)
        poly.set_facecolor((0.8,0.898,1))
        poly.set_linewidth(1.5)
        poly.set_closed(False)
        self.axes.add_patch(poly)

        pp = [[0.497, 0.92], [0.485, 0.86], [0.485, 0.71], [0.497, 0.65], [0.497, 0.63],
              [0.503, 0.63], [0.503,0.65], [0.515, 0.71], [0.515, 0.86], [0.503, 0.92]]
        poly = mpatches.Polygon(pp)
        poly.set_facecolor((0.8,0.898,1))
        poly.set_linewidth(1.5)
        poly.set_closed(False)
        self.axes.add_patch(poly)

        # Draw water channel
        pp = [[0.38, 0.5], [0.5, 0.63], [0.63, 0.5], [0.5, 0.38]]
        poly = mpatches.Polygon(pp)
        poly.set_facecolor((0.8,0.898,1))
        poly.set_linewidth(1.5)
        poly.set_closed(True)
        self.axes.add_patch(poly)

        cmap = [[0,0,1], [0,1,1], [0,1,0], [0.604,0.804,0.196], [1,1,0], [0.933,0.867,0.51], [1,0.549,0], [1,0,0]]
        enr_steps = [0.71, 2.5, 3.2, 3.4, 4.0, 4.2, 4.6, 4.9, 0]
        enr_ba = [3.4, 5.0]

        pin_radius = 0.028
        pin_delta = 0.078

        # Draw enrichment level circles
        for i in range(8):
            circle = mpatches.Circle((1.06,0.9-i*pin_delta), pin_radius, fc=cmap[i], ec=(0.1, 0.1, 0.1))
            circle.set_linewidth(2.0)
            self.axes.add_patch(circle)
            self.axes.text(1.11,0.9-i*pin_delta,'0.71',fontsize=8)


        # Draw pin circles
        # Quadrant 3
        for j in range(5):
            for i in range(5):
                if i < 4 or j < 4:
                    circle = mpatches.Circle((0.13+i*pin_delta,0.13+j*pin_delta), pin_radius, fc=cmap[1], ec=(0.1, 0.1, 0.1))
                    circle.set_linewidth(2.0)
                    self.axes.add_patch(circle)
                    self.axes.text(0.13+i*pin_delta,0.13+j*pin_delta,'2',ha='center',va='center',fontsize=10)

        # Draw pin coordinates
        for i in range(5):
            self.axes.text(0.13+i*pin_delta,0.01,self.xlist[i],ha='center',va='center',fontsize=10)
        for i in range(5,10):
            self.axes.text(0.18+i*pin_delta,0.01,self.xlist[i],ha='center',va='center',fontsize=10)

        # Draw pin coordinates
        for i in range(5):
            self.axes.text(0.99,0.87-i*pin_delta,self.ylist[i],ha='center',va='center',fontsize=10)
        for i in range(5,10):
            self.axes.text(0.99,0.82-i*pin_delta,self.ylist[i],ha='center',va='center',fontsize=10)

        Tracer()()


    def startpoint(self,case_id):
        voi_val = int(self.voi_cbox.currentText())
        vhi_val = int(self.vhi_cbox.currentText())
        type_val = str(self.type_cbox.currentText())

        case = self.cas.cases[case_id]
        if type_val == 'CCl':
            idx0 = case.findpoint(tfu=293)
            voi = case.statepts[idx0].voi
            vhi = case.statepts[idx0].vhi
            voi_index = [i for i,v in enumerate(self.voilist) if int(v) == voi][0]
            vhi_index = [i for i,v in enumerate(self.vhilist) if int(v) == vhi][0]
            self.voi_cbox.setCurrentIndex(voi_index)
            self.vhi_cbox.setCurrentIndex(vhi_index)
        else:
            idx0 = case.findpoint(voi=voi_val,vhi=vhi_val)
        return idx0


    def on_plot(self):

        case_id = self.case_id_current
        case_id_max = len(self.cas.cases)
        param = self.param_cbox.currentText()
        
        self.axes.clear()
        if param == 'Kinf':
            if self.case_cb.isChecked():
                for i in range(case_id_max):
                    #idx0 = self.startpoint(i)
                    self.plot_kinf(i)
            else:
                #idx0 = self.startpoint(case_id)
                self.plot_kinf(case_id)
        
        elif param == 'Fint':
            if self.case_cb.isChecked():
                for i in range(case_id_max):
                    self.plot_fint(i)
            else:
                self.plot_fint(case_id)

        elif param == 'BTF':
            if self.case_cb.isChecked():
                for i in range(case_id_max):
                    self.plot_btf(i)
            else:
                self.plot_btf(case_id)
 

#    def on_index(self):
#        print "Find index"
#        case_id = self.case_id_current
#        case = self.cas.cases[case_id]
##        #burnup = None
#        voi_val = int(self.voi_cbox.currentText())
#        vhi_val = int(self.vhi_cbox.currentText())
#        type_val = str(self.type_cbox.currentText())
#        print type_val,voi_val,vhi_val
##        
##        #index = self.cas.findpoint(case,burnup,vhi,voi)
##        #index = self.cas.findpoint(case,vhi=vhi_val,voi=voi_val)
##        index = self.cas.findpoint(case,voi=voi_val,vhi=vhi_val)
#        #idx0 = case.findpoint(voi=voi_val,vhi=vhi_val)
#
#        if type_val == 'CCl':
#            idx0 = case.findpoint(tfu=293)
#            print idx0

    def create_main_frame(self):
        self.main_frame = QWidget()

        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((6, 5), dpi=self.dpi, facecolor=(1,1,0.8784))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.mpl_connect('button_press_event',self.on_click)
        self.canvas.setParent(self.main_frame)
        

        # Since we have only one plot, we can use add_axes 
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        #
        self.axes = self.fig.add_subplot(111)
        
        # Bind the 'pick' event for clicking on one of the bars
        #
        #self.canvas.mpl_connect('pick_event', self.on_pick)
        
        # Create the navigation toolbar, tied to the canvas
        #
        #self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        # Other GUI controls
        # 
        #self.textbox = QLineEdit()
        #self.textbox.setMinimumWidth(200)
        #self.connect(self.textbox, SIGNAL('editingFinished ()'), self.on_draw)

                
        #self.draw_button = QPushButton("Draw")
        #self.connect(self.draw_button, SIGNAL('clicked()'), self.on_plot)
        
        #self.grid_cb = QCheckBox("Show Grid")
        #self.grid_cb.setChecked(True)
        #self.connect(self.grid_cb, SIGNAL('stateChanged(int)'), self.on_draw)
        
        #slider_label = QLabel('X-max:')
        #self.slider = QSlider(Qt.Horizontal)
        #self.slider.setRange(1, 75)
        #self.slider.setValue(65)
        #self.slider.setTracking(True)
        #self.slider.setTickPosition(QSlider.TicksBothSides)
        #self.connect(self.slider, SIGNAL('valueChanged(int)'), self.on_draw)
 
        param_label = QLabel('Parameter:')
        self.param_cbox = QComboBox()
        paramlist = ['ENR','FINT','EXP','BTF','BTFP','XFL1','XFL2','ROD','LOCK']
        for i in paramlist:
            self.param_cbox.addItem(i)
        #self.connect(self.param_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)
        param_hbox = QHBoxLayout()
        param_hbox.addWidget(param_label)
        param_hbox.addWidget(self.param_cbox)

        case_label = QLabel('Case number:')
        self.case_cbox = QComboBox()
        caselist = ['1', '2', '3']
        for i in caselist:
            self.case_cbox.addItem(i)
        case_hbox = QHBoxLayout()
        case_hbox.addWidget(case_label)
        case_hbox.addWidget(self.case_cbox)

        point_label = QLabel('Point number:')
        self.point_sbox = QSpinBox()
        self.point_sbox.setMinimum(0)
        self.point_sbox.setMaximum(10000)
        point_hbox = QHBoxLayout()
        point_hbox.addWidget(point_label)
        point_hbox.addWidget(self.point_sbox)

        self.enr_plus_button = QPushButton("+ enr")
        self.enr_minus_button = QPushButton("- enr")
        enr_hbox = QHBoxLayout()
        enr_hbox.addWidget(self.enr_plus_button)
        enr_hbox.addWidget(self.enr_minus_button)



        #Tracer()()


        #case_label = QLabel('All cases:')
        #self.case_cb = QCheckBox("All Cases")
        #self.case_cb.setChecked(False)
        #self.connect(self.case_cb, SIGNAL('stateChanged(int)'), self.on_plot)
#       self.case_cbox = QComboBox()
#        caselist = ['1','2','3','All']
#        for i in caselist:
#            self.case_cbox.addItem(i)
        
        type_label = QLabel('Type:')
        self.type_cbox = QComboBox()
        typelist = ['Hot', 'HCr', 'CCl', 'CCr']
        for i in typelist:
            self.type_cbox.addItem(i)
        #self.connect(self.type_cbox, SIGNAL('currentIndexChanged(int)'), self.on_index)

        voi_label = QLabel('VOI:')
        self.voi_cbox = QComboBox()
        self.voilist = ['0', '40', '80']
        for i in self.voilist:
            self.voi_cbox.addItem(i)
        # Determine voi index
        voi = self.cas.cases[self.case_id_current].statepts[0].voi
        voi_index = [i for i,v in enumerate(self.voilist) if int(v) == voi]
        voi_index = voi_index[0]
        self.voi_cbox.setCurrentIndex(voi_index)
        #self.connect(self.voi_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)

        vhi_label = QLabel('VHI:')
        self.vhi_cbox = QComboBox()
        self.vhilist = ['0', '40', '80']
        for i in self.vhilist:
            self.vhi_cbox.addItem(i)
        # Determine vhi index
        vhi = self.cas.cases[self.case_id_current].statepts[0].vhi
        vhi_index = [i for i,v in enumerate(self.vhilist) if int(v) == vhi]
        vhi_index = vhi_index[0]
        self.vhi_cbox.setCurrentIndex(vhi_index)
        #self.connect(self.vhi_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)


        #self.case_cbox.setWhatsThis("What is this?")

        #self.connect(self.case_cbox, SIGNAL('activated(QString)'), self.on_case)
        #self.connect(self.case_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)
        #Tracer()()

        # Define table widget
        self.table = QTableWidget()
        self.table.setRowCount(100)
        self.table.setColumnCount(2)
        #self.table.verticalHeader().hide()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(('Pin','Value'))
        self.table.setSortingEnabled(True)
        #self.tableview = QTableView()

        self.setpincoords()
        #self.table.resizeColumnsToContents()
        #Tracer()()

        #
        # Layout with box sizers
        # 
        vbox = QVBoxLayout()
        vbox.addLayout(param_hbox)
        vbox.addLayout(case_hbox)
        vbox.addLayout(point_hbox)
        vbox.addLayout(enr_hbox)

        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vbox.addItem(spacerItem)


        #for w in [  self.textbox, self.draw_button, self.grid_cb,
        #            slider_label, self.slider]:
        
        #for w in [  type_label, self.type_cbox, voi_label, self.voi_cbox,
        #            vhi_label, self.vhi_cbox]:
        #
        #    vbox.addWidget(w)
        #    vbox.setAlignment(w, Qt.AlignHCenter)
        

        #self.bundle = Bundle()
        #self.bundle.setParent(self.main_frame)
        #Tracer()()

        hbox = QHBoxLayout()

        #hbox.addWidget(self.bundle)
        #vbox.addLayout(hbox)
        #vbox.addWidget(self.canvas)
        #hbox2.addWidget(self.mpl_toolbar)
        
        hbox.addLayout(vbox)
        #hbox.addWidget(self.bundle)
        hbox.addWidget(self.canvas)
        hbox.addWidget(self.table)
        #hbox.addItem(spacerItemH)

        self.main_frame.setLayout(hbox)
        self.setCentralWidget(self.main_frame)
    
    def create_status_bar(self):
        self.status_text = QLabel("Main window")
        self.statusBar().addWidget(self.status_text, 1)
        
    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        save_settings_action = self.create_action("&Save settings...",
            shortcut="Ctrl+S", slot=self.save_plot, 
            tip="Save settings")
        quit_action = self.create_action("&Quit", slot=self.close, 
            shortcut="Ctrl+Q", tip="Close the application")
        
        open_file_action = self.create_action("&Open file...", tip="Open file")

        self.add_actions(self.file_menu, 
            (open_file_action, save_settings_action, None, quit_action))


        self.edit_menu = self.menuBar().addMenu("&Edit") 
        preferences = self.create_action("Preferences...", tip="Preferences...")        
        self.add_actions(self.edit_menu, (None, preferences))

        self.tools_menu = self.menuBar().addMenu("&Tools")
        plot_action = self.create_action("Plot...", tip="Plot...")
        btf_action = self.create_action("BTF...", tip="BTF...")
        casmo_action = self.create_action("CASMO...", tip="CASMO...")
        data_action = self.create_action("Fuel data...", tip="Fuel data...")
        table_action = self.create_action("Point table...", tip="Point table...")
        optim_action = self.create_action("Optimization...", tip="BTF optimization...")
        egv_action = self.create_action("EGV...", tip="EGV...")
        self.add_actions(self.tools_menu, 
                         (plot_action, btf_action, casmo_action, data_action,
                          table_action, optim_action, egv_action))
        
        
        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", 
            shortcut='F1', slot=self.on_about, 
            tip='About the demo')
        
        self.add_actions(self.help_menu, (about_action,))

    def create_toolbar(self):
        exitAction = QAction(QIcon('icons/exit-icon_32x32.png'), 'Exit', self)
        #exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        fileAction = QAction(QIcon('icons/open-file-icon_32x32.png'), 'Open file', self)
        fileAction.setStatusTip('Open file')

        settingsAction = QAction(QIcon('icons/preferences-icon_32x32.png'), 'Settings', self)
        settingsAction.setStatusTip('Settings')

        plotAction = QAction(QIcon('icons/diagram-icon_32x32.png'), 'Plot', self)
        plotAction.setStatusTip('Open plot window')

        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(fileAction)
        toolbar.addAction(settingsAction)
        toolbar.addAction(plotAction)
        toolbar.addAction(exitAction)

        toolbar.setMovable(False)
        toolbar.setFloatable(True)
        toolbar.setAutoFillBackground(False)


    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


def main():
    app = QApplication(sys.argv)
    window = AppForm()
    window.show()
    #app.exec_()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
