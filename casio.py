from IPython.core.debugger import Tracer

try:
    import cPickle as pickle
except:
    import pickle

import sys, os.path, re
import numpy as np

from casdata_pts import casdata


class datastruct(object):
    """Dummy class used to structure data"""
    pass


class casio:
    """Read, save and load cases"""

    def __init__(self):
        self.data = datastruct()
        self.cases = []
        #self.readinpfile(inpfile)
        #self.readcas()
        #self.savecasobj()
        #self.loadcasobj(inpfile)
        

    def readinp(self,inpfile):
        if not os.path.isfile(inpfile):
            print "Could not open file " + inpfile
            return
        else:
            print "Reading file " + inpfile
        
        with open(inpfile) as f:
            flines = f.read().splitlines() #exclude \n

        # Search for caxfiles
        reCAX = re.compile('.cax\s*$')
        caxfiles = []
        for i,x in enumerate(flines):
            if reCAX.search(x):
                caxfiles.append(x)
            else:
                break
        
        nodes  = map(int,re.split('\s+',flines[i]))

        self.data.inpfile = inpfile
        self.data.caxfiles = caxfiles
        self.data.nodes = nodes


    def readcas(self):
        for i,f in enumerate(self.data.caxfiles):
            case = casdata(f)
            case.data.topnode = self.data.nodes[i]
            self.cases.append(case)


    def savecas(self):
        pfile = os.path.splitext(self.data.inpfile)[0] + '.p'
        with open(pfile,'wb') as fp:
            pickle.dump(self.data,fp,1)
            pickle.dump(self.cases,fp,1)
        print "Saved data to file " + pfile
        

    def loadpic(self,pfile):
        print "Loading data from file " + pfile
        with open(pfile,'rb') as fp:
            self.data = pickle.load(fp)
            self.cases = pickle.load(fp)
        self.data.pfile = pfile


    def pow3(self,*args):
        """Expanding a number of 2D pin power distributions into a 3D distribution.
        Syntax: pow3(POW1,POW2,POW3,...)"""
        print "Expanding a number of 2D pin power distributions into a 3D distribution"
   
        powlist = [arg for arg in args]

        xdim = powlist[0].shape[0]
        ydim = powlist[0].shape[1]
        nodes = self.data.nodes
        zdim = max(nodes)
        POW3 = np.zeros((xdim,ydim,zdim))

        z0 = 0
        for i,POW in enumerate(powlist):
            z1 = nodes[i]
            for z in range(z0,z1):
                POW3[:,:,z] = POW 
            z0 = z1

        return POW3
        

if __name__ == '__main__':
    casio(sys.argv[1])
