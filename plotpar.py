
from IPython.core.debugger import Tracer

import matplotlib.pyplot as plt
import numpy as np
#import math


class plotpar:
    """Plot parameters vs burnup"""


    def __init__(self):
        print "Plotting data..."
        self.fig_init()


    def fig_init(self):
        pass
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)
        #plt.hold(False)
        #self.fig.show()


    def plt_kinf(self,color,c):
        
        x = np.arange(0,60)
        y = [xx**2+c for xx in x]
        p = self.ax.plot(x, y, color)
        self.ax.set_xlabel('Burnup (MWd/kgU)')
        self.ax.set_ylabel('K-inf')
        #self.ax.set_title('XY point plot')
        self.fig.show()



if __name__ == '__main__':
    plotpar()

