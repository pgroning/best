from IPython.core.debugger import Tracer

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ProgressBar(QWidget):
    def __init__(self, parent=None, total=20):
        super(ProgressBar, self).__init__(parent)
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(1)
        self.progressbar.setMaximum(total)
        main_layout = QGridLayout()
        main_layout.addWidget(self.progressbar, 0, 0)
        self.setLayout(main_layout)
        self.setWindowTitle('Progress')
        self.resize(200,50)
        self.move(500,500)
        #Tracer()()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bar = ProgressBar()
    bar.show()
    sys.exit(app.exec_())

