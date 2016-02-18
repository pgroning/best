"""
This is the main window of the program.
This window embeds a matplotlib (mpl) plot into a PyQt4 GUI application
"""

from IPython.core.debugger import Tracer
from pyqt_trace import pyqt_trace

import sys, os#, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4 import QtGui, QtCore

import numpy as np

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
#from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches
import time

from casio import casio
from btf import btf

#from pyDraw import Bundle
from plot_gui import PlotWin

class Circle(object):
    def __init__(self,axes,x,y,c=(1,1,1),text='',r=0.028):
        #radius = 0.028
        self.circle = mpatches.Circle((x,y), r, fc=c, ec=(0.1, 0.1, 0.1))
        self.circle.set_linewidth(2.0)
        self.x = x
        self.y = y
        self.axes = axes
        self.text = self.axes.text(x,y,text,ha='center',va='center',fontsize=8)
        self.axes.add_patch(self.circle)
        
        
    def set_text(self,text):
        self.text.remove()
        self.text = self.axes.text(self.x,self.y,text,ha='center',va='center',fontsize=8)


    def is_clicked(self,xc,yc):
        r2 = (xc-self.x)**2 + (yc-self.y)**2
        if r2 < self.circle.get_radius()**2: #Mouse click is within pin radius
            return True
        else:
            return False

#def on_resize(event):
#    Tracer()()

class MainWin(QMainWindow):
#class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Main Window')
        self.resize(1100,620)
        self.move(200,200)

        #screenShape = QDesktopWidget().screenGeometry()
        #self.resize( screenShape.width()*0.8,screenShape.width()*0.445 )
        #self.setMinimumWidth(1100)
        #self.setMinimumHeight(610)
        #Tracer()()

        self.resizeEvent = self.on_resize

        # Retrieve initial data
        #self.data_init()
        #self.case_id_current = 0

        self.create_menu()
        self.create_toolbar()
        self.create_main_frame()
        self.create_status_bar()

        self.on_draw() # Init plot
        #self.draw_fuelmap()

        #self.textbox.setText('1 2 3 4')
        #self.data_init()
        
        #self.case_cbox.setCurrentIndex(0) # Set default plot case
        #self.case_id_current = 0
        #self.on_plot() # Init plot
        #self.on_draw()
        #self.draw_fuelmap()
        #Tracer()()

    def on_resize(self,event):
        self.axes.set_xlim(0,1.2)
        self.axes.set_ylim(0,1)

    def openFile(self):
        #file_choices = "inp (*.inp);;pickle (*.p)"
        file_choices = "Data files (*.inp *.p)"
        filename = unicode(QFileDialog.getOpenFileName(self, 'Open file', '', file_choices))
        if filename:
            filext = os.path.splitext(filename)[1]
            if filext == ".p":
                self.load_pickle(filename)
            elif filext == ".inp":
                self.read_cax(filename)

    def load_pickle(self,filename):
        self.statusBar().showMessage('Importing data from %s' % filename, 2000)
        self.dataobj = casio()
        self.dataobj.loadpic(filename)
 
        #fuetype = 'SVEA-96'
        #self.dataobj.btf = btf(self.dataobj,fuetype)

        #self.setpincoords()
        self.draw_fuelmap()
        self.set_pinvalues()


    def read_cax(self,filename):
        msg = """ Click Yes to start importing data from cax files.
         
         This may take a while. Continue?
        """
        msgBox = QMessageBox()
        ret = msgBox.information(self,"Importing data",msg.strip(),QMessageBox.Yes|QMessageBox.Cancel)
        #ret = msgBox.question(self,"Importing data",msg.strip(),QMessageBox.Yes|QMessageBox.Cancel)
        self.statusBar().showMessage('Importing data from %s' % filename, 2000)
        if ret == QMessageBox.Yes:
            self.dataobj = casio()
            self.dataobj.readinp(filename)
            self.dataobj.readcax()

            self.dataobj.calcbtf()
            #fuetype = 'SVEA-96'
            #self.dataobj.btf = btf(self.dataobj,fuetype)

            #self.setpincoords()
            self.draw_fuelmap()
            self.set_pinvalues()
            #self.dataobj.savecas()
        else:
            return

    def saveData(self):
        file_choices = "Data files (*.p)"
        filename = unicode(QFileDialog.getSaveFileName(self, 'Open file', '', file_choices))
        self.dataobj.savepic(filename)

    def plotWin(self):
        #print "Open plot window"
        if hasattr(self,'dataobj'):
            plotwin = PlotWin(self)
            plotwin.show()
        else:
            msg = "There is no data to plot."
            msgBox = QMessageBox()
            msgBox.information(self,"No data",msg.strip(),QMessageBox.Close)

    def set_pinvalues(self):
        #print "Set values"
        param_str = str(self.param_cbox.currentText())
        case_num = int(self.case_cbox.currentIndex())
        point_num = int(self.point_sbox.value())
        #print param_str,case_num,point_num

        #self.table.setHorizontalHeaderItem(1,QTableWidgetItem(param_str))
        #if param_str == 'FINT': param_str = 'POW'

        #if hasattr(self,'dataobj'): # data is loaded
        #    if param_str == 'ENR':
        #        pinvalues = getattr(self.dataobj.cases[case_num].data,param_str)
        #    else:
        #        pinvalues = getattr(self.dataobj.cases[case_num].statepts[point_num],param_str)
        #    #print pinvalues

        ENR = getattr(self.dataobj.cases[case_num].data,'ENR')
        EXP = getattr(self.dataobj.cases[case_num].statepts[point_num],'EXP')
        FINT = getattr(self.dataobj.cases[case_num].statepts[point_num],'POW')
        #BTF = self.dataobj.btf.DOX[point_num,:,:]

        burnup = self.dataobj.cases[case_num].statepts[point_num].burnup
        try:
            btf_num = next(i for i,x in enumerate(self.dataobj.btf.burnpoints) if x == burnup)
            BTF = self.dataobj.btf.DOX[btf_num,:,:]
        except:
            BTF = np.zeros(np.shape(self.dataobj.btf.DOX)[1:])
            BTF.fill(np.nan)

        npst = self.dataobj.cases[case_num].data.npst
        LFU = self.dataobj.cases[case_num].data.LFU
        BA = self.dataobj.cases[case_num].data.BA

        self.table.sortItems(0,Qt.AscendingOrder) # Sorting column 0 in ascending order
        self.setpincoords()
        
        #row = 0
        k = 0
        for i in range(npst):
            for j in range(npst):
                if LFU[i,j] > 0:
                #if j != 5 and i !=5:
                #    if not ((i==4 and j==4) or (i==4 and j==6) or (i==6 and j==4) or (i==6 and j==6)):
                        #print i,j
                        #print self.circlelist[k].text.get_text()
                    self.circlelist[k].ENR = ENR[i,j]
                    self.circlelist[k].EXP = EXP[i,j]
                    self.circlelist[k].FINT = FINT[i,j]
                    self.circlelist[k].BA = BA[i,j]
                    self.circlelist[k].BTF = BTF[i,j]
                    #k += 1
                    #expval = QTableWidgetItem().setData(Qt.DisplayRole,EXP[i,j])
                    #self.table.setItem(row,1,expval)
                    expItem = QTableWidgetItem()
                    expItem.setData(Qt.EditRole, QVariant(float(np.round(EXP[i,j],3))))
                    fintItem = QTableWidgetItem()
                    fintItem.setData(Qt.EditRole, QVariant(float(np.round(FINT[i,j],3))))
                    btfItem = QTableWidgetItem()
                    btfItem.setData(Qt.EditRole, QVariant(float(np.round(BTF[i,j],3))))    

                    self.table.setItem(k,1,expItem)
                    self.table.setItem(k,2,fintItem)
                    self.table.setItem(k,3,btfItem)
                    k += 1
                    
                    #self.table.setItem(row,1,expItem)
                    #self.table.setItem(row,2,fintItem)
                    #self.table.setItem(row,3,btfItem)

                        #item.setData(Qt.EditRole, QVariant(float(FINT[i,j])))
                        #self.table.setItem(row,2,item)
                        #self.table.setItem(row,1,QTableWidgetItem(str(EXP[i,j])))
                        #self.table.setItem(row,2,QTableWidgetItem(str(FINT[i,j])))
                    #self.table.setItem(row,3,QTableWidgetItem(str(0)))
                #if j != 5 and i !=5: # Ignore water cross
                #if not (np.all(LFU[i,:]==0) or np.all(LFU[:,j]==0)): # Ignore water cross
                #    row += 1
        
        burnup = self.dataobj.cases[case_num].statepts[point_num].burnup
        voi = self.dataobj.cases[case_num].statepts[point_num].voi
        vhi = self.dataobj.cases[case_num].statepts[point_num].vhi
        kinf = self.dataobj.cases[case_num].statepts[point_num].kinf
        fint = self.dataobj.cases[case_num].statepts[point_num].fint
        btf = BTF.max()
        tfu = self.dataobj.cases[case_num].statepts[point_num].tfu
        tmo = self.dataobj.cases[case_num].statepts[point_num].tmo

        self.statusBar().showMessage("Burnup=%.3f : VOI=%.0f : VHI=%.0f : Kinf=%.5f : Fint=%.3f : BTF=%.4f : TFU=%.0f : TMO=%.0f" 
                                     % (burnup,voi,vhi,kinf,fint,btf,tfu,tmo))

        #if param_str == 'ENR':
            # Print pin ENR
        npins = len(self.circlelist)
        
        for i in range(npins):
            
        #print self.circlelist[i].text.get_text()
            if param_str == 'ENR' or param_str == 'BTF':
                if self.circlelist[i].BA == 0:
                    j = next(j for j,cobj in enumerate(self.enrpinlist) if cobj.ENR == self.circlelist[i].ENR)
                else:
                    j = next(j for j,cobj in enumerate(self.enrpinlist)
                             if cobj.BA == self.circlelist[i].BA and cobj.ENR == self.circlelist[i].ENR)
                
                fc = self.enrpinlist[j].circle.get_facecolor()
                text = self.enrpinlist[j].text.get_text()
                self.circlelist[i].set_text(text)
                self.circlelist[i].circle.set_facecolor(fc)
            
            elif param_str == 'EXP':
                if self.circlelist[i].EXP < 10:
                    text =  ('%.1f' % (self.circlelist[i].EXP))
                else:
                    text =  ('%.0f' % (self.circlelist[i].EXP))
                self.circlelist[i].set_text(text)

            elif param_str == 'FINT':
                if self.circlelist[i].FINT < 10:
                    text =  ('%.1f' % (self.circlelist[i].FINT))
                else:
                    text =  ('%.0f' % (self.circlelist[i].FINT))
                self.circlelist[i].set_text(text)


        self.canvas.draw()


        #self.circlelist[0].set_text(pinvalues[0,0])


    def setpincoords(self):
        self.table.clearContents()
        #self.xlist = ('01','02','03','04','05','06','07','08','09','10')
        #self.ylist  = ('A','B','C','D','E','F','G','H','I','J')
        npin = len(self.circlelist)
        self.table.setRowCount(npin)
        
        for i,pinobj in enumerate(self.circlelist):
            coord_item = QTableWidgetItem(pinobj.coord)
            self.table.setVerticalHeaderItem(i,coord_item)
            i_item = QTableWidgetItem()
            i_item.setData(Qt.EditRole, QVariant(int(i)))
            self.table.setItem(i,0,i_item)


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

    def tableHeaderSort(self):
        #print "Sort header"
        for i,pinobj in enumerate(self.circlelist):
            #item = QTableWidgetItem(str(self.table.item(i,0).text()))
            index = int(self.table.item(i,0).text())
            item = QTableWidgetItem(str(self.circlelist[index].coord))
            self.table.setVerticalHeaderItem(i,item)


    def tableSelectRow(self,i):
        index = next(j for j in range(self.table.rowCount()) 
                     if int(self.table.item(j,0).text()) == i)
        self.table.selectRow(index)


    def pinSelect(self,i):
        index = int(self.table.item(i,0).text())
        self.mark_pin(index)


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
        #if qApp.keyboardModifiers() & Qt.ControlModifier: # ctrl+click
        #    remove = False
        #else:
        #    remove = True

        if event.button is 1:
            #print event.xdata, event.ydata
            i = np.nan
            try: # check if any circle is selected and return the index
                i = next(i for i,cobj in enumerate(self.circlelist) 
                         if cobj.is_clicked(event.xdata,event.ydata))
            except:
                pass
            if i >= 0: # A Circle is selected
                #print self.circlelist[i].coord
                self.tableSelectRow(i)
                #self.table.selectRow(i)
                #print i,self.circlelist[i].x,self.circlelist[i].y
                self.mark_pin(i)
    
    def mark_pin(self,i):
        d = self.circlelist[i].circle.get_radius()*2*1.25
        x = self.circlelist[i].x-d/2
        y = self.circlelist[i].y-d/2
        if hasattr(self,'clickrect'): # Remove any previously selected circles
            try:
                self.clickrect.remove()
            except:
                pass
        #self.clickrect = mpatches.Rectangle((x,y), d, d,hatch='.',
        #                                    fc=(1,1,1),alpha=1.0,ec=(1, 0, 0))
        self.clickrect = mpatches.Rectangle((x,y), d, d,
                                            fc=(1,1,1),Fill=False,ec=(0, 0, 0))
        #r = self.circlelist[i].circle.get_radius()*1.3
        #x = self.circlelist[i].x
        #y = self.circlelist[i].y
        #self.clickrect = mpatches.Circle((x,y), r, fc=(1,1,1), alpha=1.0, ec=(1, 0, 0))

        self.clickrect.set_fill(False)
        self.clickrect.set_linewidth(2.0)
        self.axes.add_patch(self.clickrect)
        self.canvas.draw()


    def fig_update(self):
        """ Redraw figure and update values
        """
        self.on_draw()
        self.draw_fuelmap()
        self.set_pinvalues()

    def on_draw(self):
        """ Setup the figure axis
        """

        # clear the axes and redraw the plot anew
        #
        #self.fig.clf()
        self.axes.clear()
        self.axes.axis('equal')
        #self.axes.set_xlim(0,1)
        #self.axes.set_ylim(0,1)
        #self.axes.axis('equal')
        
        #self.axes.set_position([0,0,1,1])
        #self.axes.set_xlim(0,1.2)
        #self.axes.set_ylim(0,1)
        self.axes.set_position([0,0,1,1])
        #self.axes.set_visible(False)
        self.axes.set_frame_on(False)
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)
        #Tracer()()
        #self.axes.grid(self.grid_cb.isChecked())

        #xmax = self.slider.value()
        #self.axes.set_xlim(0,xmax)

        #self.axes.axis('equal')

        #Tracer()()
        
        #self.canvas.draw()

    def draw_fuelmap(self):
        """ Draw fuel map
        """
        from map_s96o2 import s96o2

        #print "draw fuel map"
        self.fig.set_facecolor((1,1,0.8784))
        # Draw outer rectangle
        rect = mpatches.Rectangle((0.035,0.035), 0.935, 0.935, fc=(0.8,0.898,1),ec=(0.3, 0.3, 0.3))
        self.axes.add_patch(rect)
        
        # Draw control rods
        rodrect_v = mpatches.Rectangle((0.011,0.13), 0.045, 0.77, ec=(0.3, 0.3, 0.3))
        rodrect_v.set_fill(False)
        self.axes.add_patch(rodrect_v)
        #self.axes.hlines(0.17,0.011,0.056)
        pp = [[0.011, 0.17], [0.056, 0.17]]
        poly = mpatches.Polygon(pp)
        poly.set_closed(False)
        self.axes.add_patch(poly)
        pp = [[0.011, 0.86], [0.056, 0.86]]
        poly = mpatches.Polygon(pp)
        poly.set_closed(False)
        self.axes.add_patch(poly)

        rodrect_h = mpatches.Rectangle((0.1,0.95), 0.77, 0.045, ec=(0.3, 0.3, 0.3))
        rodrect_h.set_fill(False)
        self.axes.add_patch(rodrect_h)
        pp = [[0.14, 0.95], [0.14, 0.995]]
        poly = mpatches.Polygon(pp)
        poly.set_closed(False)
        self.axes.add_patch(poly)
        pp = [[0.83, 0.95], [0.83, 0.995]]
        poly = mpatches.Polygon(pp)
        poly.set_closed(False)
        self.axes.add_patch(poly)


        # a fancy box with round corners (pad).
        p_fancy = mpatches.FancyBboxPatch((0.12, 0.12),
                                          0.77, 0.77,
                                          boxstyle="round,pad=0.04",
                                          fc=(0.85,1,1),
                                          ec=(0.3, 0.3, 0.3))
        p_fancy.set_linewidth(4.0)
        self.axes.add_patch(p_fancy)
        
        s96o2(self)
 

        
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



    def create_main_frame(self):
        self.main_frame = QWidget()

        # Create the mpl Figure and FigCanvas objects. 
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((6, 5), dpi=self.dpi, facecolor=None)
        #self.fig = Figure((6, 5), dpi=self.dpi, facecolor=(1,1,1))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.mpl_connect('button_press_event',self.on_click)
        self.canvas.setParent(self.main_frame)
        self.canvas.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.canvas.setMinimumWidth(500)
        self.canvas.setMinimumHeight(416)
        
        cvbox = QVBoxLayout()
        cvbox.addWidget(self.canvas)
        canvasGbox = QGroupBox()
        canvasGbox.setStyleSheet("QGroupBox { background-color: rgb(200, 200,\
        200); border:1px solid gray; border-radius:5px;}")
        canvasGbox.setLayout(cvbox)

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
        self.connect(self.param_cbox, SIGNAL('currentIndexChanged(int)'), self.set_pinvalues)

        case_label = QLabel('Case number:')
        self.case_cbox = QComboBox()
        caselist = ['1', '2', '3']
        for i in caselist:
            self.case_cbox.addItem(i)
        case_hbox = QHBoxLayout()
        case_hbox.addWidget(case_label)
        case_hbox.addWidget(self.case_cbox)
        #self.connect(self.case_cbox, SIGNAL('currentIndexChanged(int)'), self.set_pinvalues)
        self.connect(self.case_cbox, SIGNAL('currentIndexChanged(int)'), self.fig_update)

        point_label = QLabel('Point number:')
        self.point_sbox = QSpinBox()
        self.point_sbox.setMinimum(0)
        self.point_sbox.setMaximum(10000)
        point_hbox = QHBoxLayout()
        point_hbox.addWidget(point_label)
        point_hbox.addWidget(self.point_sbox)
        self.connect(self.point_sbox, SIGNAL('valueChanged(int)'), self.set_pinvalues)

        self.enr_plus_button = QPushButton("+ enr")
        self.enr_minus_button = QPushButton("- enr")
        enr_hbox = QHBoxLayout()
        enr_hbox.addWidget(self.enr_minus_button)
        enr_hbox.addWidget(self.enr_plus_button)
        #self.connect(self.enr_plus_button, SIGNAL('clicked()'), self.draw_fuelmap)

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
        #voi = self.cas.cases[self.case_id_current].statepts[0].voi
        #voi_index = [i for i,v in enumerate(self.voilist) if int(v) == voi]
        #voi_index = voi_index[0]
        #self.voi_cbox.setCurrentIndex(voi_index)
        #self.connect(self.voi_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)

        vhi_label = QLabel('VHI:')
        self.vhi_cbox = QComboBox()
        self.vhilist = ['0', '40', '80']
        for i in self.vhilist:
            self.vhi_cbox.addItem(i)
        # Determine vhi index
        #vhi = self.cas.cases[self.case_id_current].statepts[0].vhi
        #vhi_index = [i for i,v in enumerate(self.vhilist) if int(v) == vhi]
        #vhi_index = vhi_index[0]
        #self.vhi_cbox.setCurrentIndex(vhi_index)
        #self.connect(self.vhi_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)


        #self.case_cbox.setWhatsThis("What is this?")

        #self.connect(self.case_cbox, SIGNAL('activated(QString)'), self.on_case)
        #self.connect(self.case_cbox, SIGNAL('currentIndexChanged(int)'), self.on_plot)
        #Tracer()()

        # Define table widget
        self.table = QTableWidget()
        self.table.setRowCount(100)
        self.table.setColumnCount(4)
        #self.table.verticalHeader().hide()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.table.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
        self.table.setMinimumWidth(180)
        self.table.setHorizontalHeaderLabels(('Index','EXP','FINT','BTF'))
        self.table.setSortingEnabled(True)
        self.table.setColumnHidden(0,True)
        
        #self.connect(self.table.horizontalHeader(),SIGNAL('QHeaderView.sortIndicatorChanged(int)'),self.openFile)
        self.connect(self.table.horizontalHeader(),SIGNAL('sectionClicked(int)'),self.tableHeaderSort)
        self.connect(self.table.verticalHeader(),SIGNAL('sectionClicked(int)'),self.pinSelect)
        #self.connect(self.table,SIGNAL('cellClicked(int,int)'),self.pinSelect)
        #self.connect(self.table,SIGNAL('currentChanged(int)'),self.pinSelect)
        #Tracer()()
        self.table.cellActivated.connect(self.pinSelect)
        self.table.cellClicked.connect(self.pinSelect)
        #self.table.selectionModel().selectionChanged.connect(self.pinSelect)

        tvbox = QVBoxLayout()
        tvbox.addWidget(self.table)
        tableGbox = QGroupBox()
        tableGbox.setStyleSheet("QGroupBox { background-color: rgb(200, 200,\
        200); border:1px solid gray; border-radius:5px;}")
        tableGbox.setLayout(tvbox)
        
        #self.hview = QHeaderView

       #self.tableview = QTableView()
        #self.connect(self.table.horizontalHeader().sectionClicked(), SIGNAL('logicalIndex(int)'),self.openFile)
        #self.connect(QHeaderView.sortIndicatorChanged(), SIGNAL('logicalIndex(int)'),self.openFile)
        

        #self.setpincoords()
        self.table.resizeColumnsToContents()
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

        groupbox = QGroupBox()
        groupbox.setStyleSheet("QGroupBox { background-color: rgb(200, 200,\
        200); border:1px solid gray; border-radius:5px;}")
        groupbox.setLayout(vbox)

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
        
        spacerItemH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #hbox.addLayout(vbox)
        hbox.addWidget(groupbox)
        #hbox.addItem(spacerItemH)
        #hbox.addWidget(self.canvas)
        hbox.addWidget(canvasGbox)
        #hbox.addItem(spacerItemH)
        hbox.addWidget(tableGbox)
        #hbox.addWidget(self.table)
        #hbox.addItem(spacerItemH)

        self.main_frame.setLayout(hbox)
        self.setCentralWidget(self.main_frame)
        #Tracer()()
    
    def create_status_bar(self):
        self.status_text = QLabel("Main window")
        self.statusBar().addWidget(self.status_text, 1)
        
    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        save_settings_action = self.create_action("&Save settings...",
            shortcut="Ctrl+E", slot=self.save_plot, 
            tip="Save settings")
        quit_action = self.create_action("&Quit", slot=self.close, 
                                         shortcut="Ctrl+Q", tip="Close the application")
        
        open_file_action = self.create_action("&Open file...", slot=self.openFile,
                                              shortcut="Ctrl+L", tip="Open file")

        save_data_action = self.create_action("&Save data...", slot=self.saveData,
                                              shortcut="Ctrl+S", tip="Save data to file")

        self.add_actions(self.file_menu, 
            (open_file_action, save_data_action, save_settings_action, None, quit_action))


        self.edit_menu = self.menuBar().addMenu("&Edit") 
        preferences = self.create_action("Preferences...", tip="Preferences...")        
        self.add_actions(self.edit_menu, (None, preferences))

        self.tools_menu = self.menuBar().addMenu("&Tools")
        plot_action = self.create_action("Plot...", tip="Plot...", slot=self.plotWin)
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
        fileAction.triggered.connect(self.openFile)

        settingsAction = QAction(QIcon('icons/preferences-icon_32x32.png'), 'Settings', self)
        settingsAction.setStatusTip('Settings')

        plotAction = QAction(QIcon('icons/diagram-icon_32x32.png'), 'Plot', self)
        plotAction.setStatusTip('Open plot window')
        plotAction.triggered.connect(self.plotWin)

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
    window = MainWin()
    #window = AppForm()
    window.show()
    #app.exec_()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
