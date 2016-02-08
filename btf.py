from IPython.core.debugger import Tracer

import numpy as np
from casio import casio

class btf:
    """Calculate BTF values"""

    def __init__(self,casobj,burnup):
        if casobj.data.fuetype == 'SVEA-96':
            self.svea96(casobj,burnup)



    def pow3d(self,casobj,voi,burnup):
        """Construct a 3D pin power distribution for specific void and burnup"""
        print "Constructing 3D pin power distribution for specific void and burnup"

        #casobj = casio()
        #casobj.loadpic('caxfiles.p')
    
        #voi = 50
        #burnup = 0
    
        ncases = len(casobj.cases)
        npst = casobj.cases[0].data.npst
        P12 = np.zeros((ncases,npst,npst))
        for i in range(ncases):
            # Initiate array 2D array
            i1 = casobj.cases[i].findpoint(burnup=burnup,vhi=40,voi=40)
            i2 = casobj.cases[i].findpoint(burnup=burnup,vhi=80,voi=80)
            #print i1,i2
        
            P1 = casobj.cases[i].statepts[i1].POW
            P2 = casobj.cases[i].statepts[i2].POW
            P12[i,:,:] = casobj.interp2(P1,P2,40,80,voi)
        
        # Expand to 3D array
        self.POW3 = casobj.pow3(P12)
        #POW3 = casobj.pow3(P12[:,:,0],P12[:,:,1],P12[:,:,2])
    
        #Tracer()()
        #DOX = calc_btf('SVEA-96',POW3)
        #DOXmax = DOX.max()
        #imax = np.where(DOX == DOX.max())
        #return POW3



    def svea96(self,casobj,burnup):
        print 'Calculating SVEA-96'
        #from btf_s96 import pow3d
        from btf_s96 import calc_btf
        voi = 50
        self.pow3d(casobj,voi,burnup)
        self.DOX = calc_btf(casobj.data.fuetype,self.POW3)
        Tracer()()



if __name__ == '__main__':
    casobj = casio()
    casobj.loadpic('caxfiles.p')
    casobj.data.fuetype = 'SVEA-96'
    burnup = 0
    btf(casobj,burnup)
    #Tracer()()
