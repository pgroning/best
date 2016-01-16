from IPython.core.debugger import Tracer

import sys
from PyQt4.QtGui import *

lista = ['aa', 'ab', 'ac']
listb = ['ba', 'bb', 'bc']
listc = ['ca', 'cb', 'cc']
mystruct = {'A':lista, 'B':listb, 'C':listc}

class MyTable(QTableWidget):
    def __init__(self, thestruct, *args):
        QTableWidget.__init__(self, *args)
        QTableWidget.setHorizontalHeaderLabels(self,('','Fint','BTF','Burnup'))
        QTableWidget.verticalHeader(self).hide()
        QTableView.setSortingEnabled(self, True)
        QTableWidget.setEditTriggers(self,QAbstractItemView.NoEditTriggers)
        self.xylist = ('j7','j6','j5')
        self.setxy()
        self.data = thestruct
        self.setmydata()
        
    def setxy(self):
        for r,xy in enumerate(self.xylist):
            item = QTableWidgetItem(xy)
            self.setItem(r,0,item)

    def setmydata(self):
        n = 1
        for key in self.data:
            m = 0
            for item in self.data[key]:
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
                m += 1
            n += 1

def main(args):
    app = QApplication(args)
    table = MyTable(mystruct, 5, 4)
    table.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main(sys.argv)
