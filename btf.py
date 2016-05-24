from IPython.core.debugger import Tracer
from pyqt_trace import pyqt_trace

import numpy as np
#from casio import casio

class btf:
    """Calculate BTF values"""

    def __init__(self,casobj):
        self.casobj = casobj

        if self.casobj.data.fuetype == 'SVEA-96':
            self.svea96()
        elif self.casobj.data.fuetype == 'A10XM':
            self.a10xm()


    def export2ascii(self):
        np.savetxt('btf.txt',self.DOX,fmt='%.4f',delimiter=' ')


    def lastindex(self,case_id):
        """Iterate over burnup points"""
        statepoints = self.casobj.cases[case_id].statepts
        burnup_old = 0.0
        for idx,p in enumerate(statepoints):
            if p.burnup < burnup_old:
                break
            burnup_old = p.burnup
        return idx


    def pow3d(self,voi,burnup):
        """Construct a 3D pin power distribution for specific void and burnup"""
        #print "Constructing 3D pin power distribution for specific void and burnup"

        #casobj = casio()
        #casobj.loadpic('caxfiles.p')
    
        #voi = 50
        #burnup = 0
    
        ncases = len(self.casobj.cases)
        npst = self.casobj.cases[0].data.npst
        P12 = np.zeros((ncases,npst,npst))
        for i in range(ncases):
            # Initiate array 2D array
            i1 = self.casobj.cases[i].findpoint(burnup=burnup,vhi=40,voi=40)
            i2 = self.casobj.cases[i].findpoint(burnup=burnup,vhi=80,voi=80)
            #print i1,i2
        
            P1 = self.casobj.cases[i].statepts[i1].POW
            P2 = self.casobj.cases[i].statepts[i2].POW
            P12[i,:,:] = self.casobj.interp2(P1,P2,40,80,voi)
        
        # Expand to 3D array
        POW3 = self.casobj.pow3(P12)
        #POW3 = casobj.pow3(P12[:,:,0],P12[:,:,1],P12[:,:,2])
    
        #Tracer()()
        #DOX = calc_btf('SVEA-96',POW3)
        #DOXmax = DOX.max()
        #imax = np.where(DOX == DOX.max())
        return POW3



    def svea96(self):
        print 'Calculating BTF for SVEA96OPT2'
        from btf_s96 import calc_btf
        
        voi = 50

        # Find intersection burnup points for all cases
        idx = self.lastindex(0)
        x = [self.casobj.cases[0].statepts[i].burnup for i in range(idx)]
        ncases = len(self.casobj.cases)
        for case_id in range(1,ncases):
            idx = self.lastindex(case_id)
            x2 = [self.casobj.cases[case_id].statepts[i].burnup for i in range(idx)]
            x = [val for val in x if val in x2]
        case_id = 0
        npst = self.casobj.cases[case_id].data.npst
        self.DOX = np.zeros((len(x),npst,npst))

        for i,burnup in enumerate(x):
            #print burnup
            POW3 = self.pow3d(voi,burnup)
            self.DOX[i,:,:] = calc_btf(self.casobj.data.fuetype,POW3)

        self.burnpoints = x

    
        #POW3 = self.pow3d(voi,0)
        #self.DOX = calc_btf(self.casobj.data.fuetype,POW3)
        #self.export2ascii()


        #from btf_s96 import pow3d
        #from btf_s96 import calc_btf
        #voi = 50
        #self.pow3d(casobj,voi,burnup)
        #self.DOX = calc_btf(casobj.data.fuetype,self.POW3)
        #Tracer()()

    def a10xm(self):
        print 'Calculating BTF for A10XM'
        from btf_a10xm import calc_btf
        
        voi = 60

        # Find intersection burnup points for all cases
        idx = self.lastindex(0)
        x = [self.casobj.cases[0].statepts[i].burnup for i in range(idx)]
        ncases = len(self.casobj.cases)
        for case_id in range(1,ncases):
            idx = self.lastindex(case_id)
            x2 = [self.casobj.cases[case_id].statepts[i].burnup for i in range(idx)]
            x = [val for val in x if val in x2]

        npst = self.casobj.cases[case_id].data.npst
        self.DOX = np.zeros((len(x),npst,npst))


        POW3 = self.pow3d(voi,0)
        self.DOX[0,:,:] = calc_btf(self.casobj.data.fuetype,POW3)

        #for i,burnup in enumerate(x):
        #    #print burnup
        #    POW3 = self.pow3d(voi,burnup)
        #    self.DOX[i,:,:] = calc_btf(self.casobj.data.fuetype,POW3)

        self.burnpoints = x

        #Tracer()()


if __name__ == '__main__':
    from casio import casio
    casobj = casio()
    casobj.loadpic('caxfiles_a10xm.p')
    #fuetype = 'SVEA96OPT2'
    btf(casobj)
    #Tracer()()
