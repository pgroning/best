#!/usr/bin/env python

# For debugging. Add Tracer()() inside the code to break at that line
from IPython.core.debugger import Tracer
# Inside iptyhon shell: run -d b<L> readfile.py
# sets a break point add line L.

import numpy as np
import re

def readfile():
    fname = "cax/e29OPT2-389-10g40mid-cas.cax"
    print "Reading file " + fname
    
    with open(fname) as f:
        #flines = f.readlines() # include \n
        flines = f.read().splitlines() #exclude \n

    # Find the lines containing some key cards
    reTIT = re.compile('^TIT')
    reTTL = re.compile('^\*I TTL')
    reREA = re.compile('REA\s+')
    reGPO = re.compile('GPO\s+')
    rePOW = re.compile('POW\s+')

    #iTIT = np.array([])
    iTIT = np.arange(0,dtype='int32') # Setup empty integer array
    #iTIT = np.zeros(100000,dtype='int32')
    iTTL = np.arange(0,dtype='int32')
    iREA = np.arange(0,dtype='int32')
    iGPO = np.arange(0,dtype='int32')
    iPOW = np.arange(0,dtype='int32')

    for idx, line in enumerate(flines):
        if reTIT.match(line) is not None:
            iTIT = np.append(iTIT,idx)
        elif reTTL.match(line) is not None:
            iTTL = np.append(iTTL,idx)
        elif reREA.match(line) is not None:
            iREA = np.append(iREA,idx)
        elif reGPO.match(line) is not None:
            iGPO = np.append(iGPO,idx)
        elif rePOW.match(line) is not None:
            iPOW = np.append(iPOW,idx)

    # Calculate burnup points
    S3C = False
    if S3C:
        tmpvec = iTIT[iTIT>iTTL[1]]
        tmpvec = tmpvec[tmpvec<iTTL[2]]
        Nburnpts = tmpvec.size
        iTITs = tmpvec[0:Nburnpts]
        tmpvec = iREA[iREA>iTITs[0]]
        iREAs = tmpvec[0:Nburnpts]
        tmpvec = iPOW[iPOW>iTITs[0]]
        iPOWs = tmpvec[0:Nburnpts]
    else:
        Nburnpts = iTIT[iTIT<iTTL[1]].size
        iTITs = iTIT[0:Nburnpts]
        iREAs = iREA[0:Nburnpts]
        iPOWs = iPOW[0:Nburnpts]

    # Calculate burnup and kinf
    burnup = np.zeros(Nburnpts)
    kinf = np.zeros(Nburnpts)
    for i in range(Nburnpts):
        burnup[i] = flines[iTITs[i]+2][0:6]
        kinf[i] = flines[iREAs[i]+1][0:12]
    


    Tracer()()


if __name__ == '__main__':
    readfile()
