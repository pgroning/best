from IPython.core.debugger import Tracer

try:
    import cPickle as pickle
except:
    import pickle

import sys, os.path, re
import numpy as np

from casdata_pts import casdata

class casio:

    def __init__(self):
        #self.readinpfile(inpfile)
        #self.readcas()
        #self.savecasobj()
        #self.loadcasobj(inpfile)
        pass

    def readinpfile(self,inpfile):
        if not os.path.isfile(inpfile):
            print "Could not open file " + inpfile
            return
        else:
            print "Reading file " + inpfile

        
        with open(inpfile) as f:
            flines = f.read().splitlines() #exclude \n

        # Search for caxfiles
        reCAX = re.compile('.cax\s*$')
        caxfiles = [x for x in flines if reCAX.search(x)]

        seclens = np.zeros(len(caxfiles))
        seclens[:]  = re.split('\s+',flines[len(caxfiles)])
        nodes = int(flines[len(caxfiles)+1])

        self.inpfile = inpfile
        self.caxfiles = caxfiles
        self.seclens = seclens
        self.nodes = nodes


    def readcas(self):
        casobjlist = []
        for i,f in enumerate(self.caxfiles):
            casobjlist.append(casdata(f))
            casobjlist[i].nodefrac = self.seclens[i]
            casobjlist[i].nodes = self.nodes
     
        self.casobjlist = casobjlist
     

    def savecasobj(self):
        pfile = os.path.splitext(self.inpfile)[0] + '.p'
        with open(pfile,'wb') as fp:
            pickle.dump(self.casobjlist,fp,1)
        print "Saved object list to file " + pfile
        
        self.pfile = pfile

    
    def loadcasobj(self,pfile):
        print "Loading object list from file " + pfile
        with open(pfile,'rb') as fp:
            self.casobjlist = pickle.load(fp)
        print "Object list loaded from file " + pfile


'''
x = casdata('cax/e29OPT2-389-10g40mid-cas.cax')
x2 = casdata('cax/e29OPT2-389-10g40mid-cas.cax')
x3 = casdata('cax/e29OPT2-389-10g40mid-cas.cax')
xlist = []
xlist.append(x)
xlist.append(x2)
xlist.append(x3)

fname = 'casobj.p'
# Write object to file
print "Write data to file..."
with open(fname,'wb') as fp:
    pickle.dump(xlist,fp,1)

# Read object back from file
print "Read data from file..."
with open(fname,'rb') as fp:
    xx=pickle.load(fp)

'''


if __name__ == '__main__':
    casio(sys.argv[1])
