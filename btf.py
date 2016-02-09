from IPython.core.debugger import Tracer

import numpy as np
from casio import casio

class btf:
    """Calculate BTF values"""

    def __init__(self,casobj,fuetype):
        self.casobj = casobj

        if fuetype == 'SVEA-96':
            self.svea96(fuetype)


    def export2ascii(self):
        np.savetxt('btf.txt',self.DOX,fmt='%.4f',delimiter=' ')



    def lastindex(self,case_id):
        """Iterate over burnup points"""
        print "Calculating BTF vs burnup"
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



    def svea96(self,fuetype):
        print 'Calculating SVEA-96'
        from btf_s96 import calc_btf
        
        voi = 50

        case_id = 1
        idx = self.lastindex(case_id)
        x = [self.casobj.cases[case_id].statepts[i].burnup for i in range(idx)]
        #Tracer()()
        npst = self.casobj.cases[case_id].data.npst
        self.DOX = np.zeros((len(x),npst,npst))

        for i,burnup in enumerate(x):
            #print burnup
            POW3 = self.pow3d(voi,burnup)
            self.DOX[i,:,:] = calc_btf(fuetype,POW3)

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



if __name__ == '__main__':
    casobj = casio()
    casobj.loadpic('caxfiles.p')
    fuetype = 'SVEA-96'
    btf(casobj,fuetype)
    #Tracer()()
