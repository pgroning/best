from IPython.core.debugger import Tracer

import numpy as np
import sys

#sys.path.append('/btf')
#from libADDC import addc
#import libADDC
# source /opt/intel/bin/compilervars.sh intel64
import libADDC

class btfcalc:

    def __init__(self,POW):
        fuetype = "SVEA-96"
        self.addc(fuetype)
        self.btf(POW)

    def addc(self,fuetype):  # Import addc from shared lib
        print fuetype
        ADDC,dim = libADDC.addc(fuetype)
        self.addc = ADDC[:dim,:dim]

    def btf(self,POW):
        print "Calculating btf..."
        # Calculation of R-factors for SVEA-96 Optima 2 D4.1.5
        
        ndim = self.addc.shape[0]
        RP = np.zeros((ndim,ndim)); #RP.fill(np.nan)
        WP = np.zeros((ndim,ndim));
        

        


        Tracer()()

if __name__ == '__main__':
        btfcalc(sys.argv[1])
