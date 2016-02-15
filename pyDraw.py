#!/usr/bin/python

import sys, random
from PyQt4 import QtGui, QtCore

class Bundle(QtGui.QWidget):
       
    def __init__(self,parent=None):
        super(Bundle, self).__init__(parent)
        
        self.initUI()

        # Declare attributes
        self.pinSelect = None
        self.click_x = 0
        self.click_y = 0
        self.dim = 0

        """
    def enterEvent(self, event):
        print "Mouse Entered"
        return super(Bundle, self).enterEvent(event)

    def leaveEvent(self, event):
        print "Mouse Left"
        return super(Bundle, self).enterEvent(event)
        """

        
    def initUI(self):
        self.setGeometry(0, 0, 580, 500)
        #self.setGeometry(0, 0, 800, 600)
        #self.setWindowTitle('Bundle')
        self.show()

        # Default values for mouse click
        #self.click_x = -100
        #self.click_y = -100
    
    def mousePressEvent(self, mouse_evt):
        
        super(Bundle, self).mousePressEvent(mouse_evt)

        button = mouse_evt.button()
        #item = self.itemAt(event.x(), event.y())

        if button == 1:
            #print 'SIMPLE LEFT CLICK!'
            #print mouse_evt.x(), mouse_evt.y()
            
            self.click_x = mouse_evt.pos().x()
            self.click_y = mouse_evt.pos().y()
            #print self.click_x, self.click_y

            #self.clickEvent(mouse_evt.x())

            #self.clickHilight(mouse_evt.x(),mouse_evt.y())
        #if button == 2:
        #    print 'SIMPLE RIGHT CLICK!'
            #print mouse_evt.x(), mouse_evt.y()
   
        self.update()


    #def mouseClick(self, qp, x, y):
    #    print x,y


#    def clickEvent(self, x):
#        return x

    """
    def clickHilight(self,x,y,qp):
        print x,y
        
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        
        r = s*0.06
        
        qp.drawEllipse(x,y,r,r)
    """
    

    def paintEvent(self, event):

        #self.dim = min(self.size().height(),self.size().width()/1.5)
        self.dim = self.size().height()
        s = self.dim
        #s = min(self.size().height(),self.size().width())  
        
        qp = QtGui.QPainter()

        qp.begin(self)
        self.setBackground(qp)
        self.drawFrame(qp)
        self.drawCoords(qp)
        self.drawCRD(qp)
        self.drawBox(qp)
        self.drawSymline(qp)
        qp.end()

        qp.begin(self)
        self.drawChannels(qp)
        qp.end()

        qp.begin(self)
        self.drawDiamond(qp)
        qp.end()

        qp.begin(self)
        self.paintCorners(qp)
        qp.end()

        qp.begin(self)
        self.drawCircles(qp)
        self.drawPinGroups(qp)
        self.drawZpin(qp)
        qp.end()

        qp.begin(self)
        self.clickMark(qp)
        qp.end()

    def pinPos(self, i, j):
        s = self.dim
        
        r = s*0.028
        b = s*0.075

        c = s*0.07
        a = s*0.1
        #b = s*0.070


        x = a+i*b+r
        y = a+j*b+r
        if i >= 5:
            x = x+c
        if j >= 5:
            y = y+c
        
        if i < 0:
            x = -100
        if j < 0:
            y = -100

        return x,y,r

    def clickMark(self, qp):
        s = self.dim
        #color = QtGui.QColor(0, 0, 0)
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        #pen = QtGui.QPen(color, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        dia = s*0.055

        xc = self.click_x
        yc = self.click_y

        #self.pinSelect = (-1,-1) 
        for i in range(10):
            for j in range(10):
                x,y,r = self.pinPos(i,j)
                r2 = (x-xc)**2 + (y-yc)**2
                if r2 < dia**2/4: # Click is within pin radius
                    self.pinSelect = (i,j)

        #print self.pinSelect

        d = s*0.06*1.2
        brush = QtGui.QBrush(QtCore.Qt.Dense7Pattern)
        qp.setBrush(brush)

        if self.pinSelect >= (0,0):
            if (self.pinSelect != (4,4) and self.pinSelect != (5,4) and
                self.pinSelect != (4,5) and self.pinSelect != (5,5)):
                (x,y,r) = self.pinPos(self.pinSelect[0],self.pinSelect[1])
                qp.drawRect(x-d/2, y-d/2, d, d)


    def setBackground(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#FFFFE5') # light yellow
        qp.setBrush(color)
        #qp.setBrush(QtCore.Qt.white)
        #x1 = s*0.999

        x1 = self.size().width()*0.999
        x2 = self.size().height()*0.999
        qp.drawRect(0,0,x1,x2)
        #qp.drawRect(0,0,600,600)

    def drawFrame(self, qp):
        s = self.dim
        qp.drawRect(0,0,s,s)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue
        qp.setBrush(color)
        x1 = s*0.04
        x2 = s*0.92
        qp.drawRect(x1,x1,x2,x2)
        

    def drawCoords(self, qp):
        s = self.dim
        
        qfont = QtGui.QFont('Decorative', 10)
        qfont.setStyle(QtGui.QFont.StyleNormal)
        qfont.setWeight(QtGui.QFont.Normal)
        qp.setFont(qfont)

        ycoords = ['A','B','C','D','E','F','G','H','I','J']
        xcoords = [1,2,3,4,5,6,7,8,9,10]
        for i,val in list(enumerate(ycoords)):
            #x,y,r = self.pinPos(9,9-i)
            x,y,r = self.pinPos(9,i)
            qp.drawText(x+0.1*s,y+0.01*s,val)

        for i,val in list(enumerate(xcoords)):
            #x,y,r = self.pinPos(9-i,9)
            x,y,r = self.pinPos(i,9)
            qp.drawText(x-0.01*s,y+0.115*s,str(val))


    def drawCRD(self, qp):
        s = self.dim
        # Paint crd
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        x1 = s*0.025
        x2 = s*0.92

        #s = self.size()
        #x1 = s.height()*0.025
        #x2 = s.height()*0.92
        #qp.drawLine(x1, x1, x2, x1)
        #qp.drawLine(x1, x1, x1, x2)
        gradient = QtGui.QLinearGradient(0, 0, 1, 0)
        
        brush = QtGui.QBrush(QtCore.Qt.transparent)
        qp.setBrush(brush)

        x1 = s*0.018
        y1 = s*0.1
        x2 = s*0.044
        y2 = s*0.77

        qp.drawRect(x1,y1,x2,y2)
        qp.drawLine(x1, y1*1.3, x1+x2, y1*1.3)
        qp.drawLine(x1, y2+y1*0.7, x1+x2, y2+y1*0.7)

        qp.drawRect(y1,x1,y2,x2)
        qp.drawLine(y1*1.3,x1, y1*1.3 ,x1+x2)
        qp.drawLine(y2+y1*0.7, x1, y2+y1*0.7, x1+x2)
        
        #qp.drawLine(20, 20, 555, 20)
        #qp.drawLine(20, 20, 20, 555) 

    def drawBox(self, qp):
        s = self.dim
        pen = QtGui.QPen(QtCore.Qt.black, 5, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        #x1 = s*0.05
        #x2 = s*0.92
        
        x1 = s*0.08
        x2 = s*0.84

        #s = self.size()
        #x1 = s.height()*0.05
        #x2 = s.height()*0.92
        
        #qp.drawRect(x1, x1, x2, x2)

        color = QtGui.QColor(0, 200, 255)
        color.setNamedColor('#D1EEEE') #
        qp.setBrush(color)

        qp.drawRoundedRect(x1, x1, x2, x2, 0.03*s, 0.03*s)
        

    def drawSymline(self, qp):
        s = self.dim
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        #pen.setStyle(QtCore.Qt.CustomDashLine)
        #pen.setDashPattern([2, 5, 2, 5])
        qp.setPen(pen)
        x1 = s*0.04
        x2 = s*0.96
        qp.drawLine(x1, x1, x2, x2)

    def drawQuad(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#B0E2FF')

        pen = QtGui.QPen(color, 40, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        chanLength = 140
        chanWidth = 40

        qp.drawLine(60, 310, 560, 310)
        qp.drawLine(310, 60, 310, 560)

        pen = QtGui.QPen(color, 140, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(310,310,312,312)

    def drawDiamond(self, qp):
        s = self.dim
        pen = QtGui.QPen(QtCore.Qt.black, 4, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue
        qp.setBrush(color)

        d = s*0.21 # Box size
        x1 = s*0.5
        x2 = s*0.35

        #s = self.size()
        #d = s.height()*0.21 # Box size
        
        #x1 = s.height()*0.5
        #x2 = s.height()*0.35
        qp.translate(x1, x2)
        qp.rotate(45)
        qp.drawRect(0,0,d,d)

    def paintCorners(self, qp):
        s = self.dim
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue

        x1 = s*0.4997
        d = s*0.044
        x2 = s*0.36
        x3 = s*0.64

        #s = self.size()
        #x1 = s.height()*0.4997
        #d = s.height()*0.044
        #c = 310
        #d = 28
        pen = QtGui.QPen(color, d, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        #x2 = s.height()*0.36
        #x3 = s.height()*0.64
        qp.drawPoint(x2,x1)
        qp.drawPoint(x3,x1)
        qp.drawPoint(x1,x2)
        qp.drawPoint(x1,x3)


    def drawChannels(self, qp):
        s = self.dim
        pen = QtGui.QPen(QtCore.Qt.black, 4, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue
        qp.setBrush(color)

        #d = 30
        #c = 310
        
        c = s*0.5
        d = s*0.05

        x1 = s*0.08
        x2 = s*0.84

        #s = self.size()

        #c = s.height()*0.5
        #d = s.height()*0.05

        #x1 = s.height()*0.05
        #x2 = s.height()*0.92
        qp.drawRect(x1,c-d/2,x2,d)
        qp.drawRect(c-d/2,x1,d,x2)

        #qp.drawRect(40,c-d/2,540,d)
        #qp.drawRect(c-d/2,40,d,540)

    def drawCircles(self, qp):
        s = self.dim
        pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        
        r = s*0.055
        d = s*0.070
        #x0 = s*0.07
        #x1 = s*0.08

        x0 = s*0.1
        x1 = s*0.075

        #s = self.size()

        #r = s.height()*0.06

        #color = QtGui.QColor(0, 0, 0)
        
        #x0 = s.height()*0.07
        #x1 = s.height()*0.08
        # Quad 1
        for i in range(0,5):
            for j in range(0,5):
                if (i,j) == (4,4):
                    continue
                else:
                    self.setColor(qp)
                    x,y,r = self.pinPos(i,j)
                    qp.drawEllipse(x-r,y-r,2*r,2*r)
                    #qp.drawEllipse(x0+i*x1,x0+j*x1,r,r)
                    

        #d = self.height()*0.082
        # Quad 2
        for i in range(5,10):
            for j in range(0,5):
                if (i,j) == (5,4):
                    continue
                else:
                    self.setColor(qp)
                    x,y,r = self.pinPos(i,j)
                    qp.drawEllipse(x-r,y-r,2*r,2*r)
                    #qp.drawEllipse(d+x0+i*x1,x0+j*x1,r,r)
        
        # Quad 3
        for i in range(0,5):
            for j in range(5,10):
                if (i,j) == (4,5):
                    continue
                else:
                    self.setColor(qp)
                    x,y,r = self.pinPos(i,j)
                    qp.drawEllipse(x-r,y-r,2*r,2*r)
                    #qp.drawEllipse(x0+i*x1,d+x0+j*x1,r,r)
        
        # Quad 4
        for i in range(5,10):
            for j in range(5,10):
                if (i,j) == (5,5):
                    continue
                else:
                    self.setColor(qp)
                    x,y,r = self.pinPos(i,j)
                    qp.drawEllipse(x-r,y-r,2*r,2*r)
                    #qp.drawEllipse(d+x0+i*x1,d+x0+j*x1,r,r)
        
    def drawPinGroups(self, qp):
        s = self.dim
        dx = s*0.2
        x,y0,r = self.pinPos(9,0)
        x,y1,r = self.pinPos(9,1)
        dy = y1-y0
        for i in range(0,9):
            self.setColor(qp)
            x,y,r = self.pinPos(9,i)
            qp.drawEllipse(x-r+dx,y0+i*dy-r,2*r,2*r)

    def drawZpin(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#F08080') # light coral
        qp.setBrush(color)
        brush = QtGui.QBrush(QtCore.Qt.Dense7Pattern)
        #qp.setBrush(brush)
        qp.setBrush(color)

        s = self.dim
        x1 = self.width()-s*0.04
        y1 = 0
        x2 = self.width()
        y2 = self.height()
        qp.drawRect(x1,y1,x2,y2)


    def setColor(self, qp):
        color = QtGui.QColor(0, 0, 0)
        r = random.random()
        if r < 0.1:
            color = QtGui.QColor(255, 0, 255) # purple
            qp.setBrush(color)
        elif r < 0.2:
            color = QtGui.QColor(200, 0, 255) # violet
                        #color.setNamedColor('#A020F0') # violet
            qp.setBrush(color)
                        #qp.setBrush(QtCore.Qt.blue)
        elif r < 0.3:
            color = QtGui.QColor(0, 0, 255) # blue
            qp.setBrush(color)
                        #qp.setBrush(QtCore.Qt.blue)
        elif r < 0.4:
            color = QtGui.QColor(0, 200, 255) # light blue
                        #color.setNamedColor('#63D1F4') # light blue
            qp.setBrush(color)
        elif r < 0.5:
            color = QtGui.QColor(0, 255, 0) # green
                        #qp.setBrush(QtCore.Qt.green) # green
            qp.setBrush(color)
        elif r < 0.6:
            qp.setBrush(QtCore.Qt.yellow) # yellow
        elif r < 0.7:
            color.setNamedColor('#E9C2A6') # orange
            qp.setBrush(color)
        elif r < 0.9:
            color.setNamedColor('#FF5333') # light red
            qp.setBrush(color)
        else:
            qp.setBrush(QtCore.Qt.red)



def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Bundle()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
