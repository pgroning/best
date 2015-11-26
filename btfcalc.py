from IPython.core.debugger import Tracer

import sys

#sys.path.append('/btf')
#from libADDC import addc
import libADDC

class btfcalc:

    def __init__(self,fuetype):
        self.addc(fuetype)

    def addc(self,fuetype):  # Import addc from shared lib
        print fuetype
        ADDC,dim = libADDC.addc(fuetype)
        self.addc = ADDC[:dim,:dim]

    def btf(self):
        print "Calculating btf"
        
        

        #Tracer()()

if __name__ == '__main__':
        btfcalc(sys.argv[1])
