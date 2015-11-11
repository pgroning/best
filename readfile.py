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
    
    # Read fuel dimension
    reBWR = re.compile('^\s*BWR')
    for line in flines:
        if reBWR.match(line) is not None:
            fuedim = int(line[5:7])
            break

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
        iTITbp = tmpvec[0:Nburnpts]
        tmpvec = iREA[iREA>iTITs[0]]
        iREAbp = tmpvec[0:Nburnpts]
        tmpvec = iGPO[iGPO>iTITs[0]]
        iGPObp = tmpvec[0:Nburnpts]
        tmpvec = iPOW[iPOW>iTITs[0]]
        iPOWbp = tmpvec[0:Nburnpts]
    else:
        Nburnpts = iTIT[iTIT<iTTL[1]].size
        iTITbp = iTIT[0:Nburnpts]
        iREAbp = iREA[0:Nburnpts]
        iGPObp = iGPO[0:Nburnpts]
        iPOWbp = iPOW[0:Nburnpts]

    # Read burnup and kinf
    burnup = np.zeros(Nburnpts); burnup.fill(np.nan)
    kinf = np.zeros(Nburnpts); kinf.fill(np.nan)
    for i in range(Nburnpts):
        burnup[i] = flines[iTITbp[i]+2][0:6]
        kinf[i] = flines[iREAbp[i]+1][0:12]
    
    
    # Read radial power distribution map
    gamma = True # Use GPO insted of POW

    if gamma:
        idx = iGPObp
    else:
        idx = iPOWbp

    POW = np.zeros((fuedim,fuedim,Nburnpts)); POW.fill(np.nan)
    for i in range(Nburnpts):
        caxmap = flines[idx[i]+2:idx[i]+2+fuedim]
        M = map2mat(caxmap,fuedim)
        M = symtrans(M)
        POW[:,:,i] = M


    # Calculate radial burnup distribution
    EXP = np.zeros((fuedim,fuedim,Nburnpts)); EXP.fill(np.nan)
    EXP[:,:,0] = 0 # Initial burnup
    for i in range(1,Nburnpts):
        dburn = burnup[i] - burnup[i-1]
        EXP[:,:,i] = EXP[:,:,i-1] + POW[:,:,i]*dburn



    Tracer()()



def map2mat(caxmap,dim):
    M = np.zeros((dim,dim)); M.fill(np.nan)
    for i in range(dim):
        rstr = caxmap[i]
        rvec = rstr.strip().split(' ')
        M[i,0:i+1] = rvec
    return M

def symtrans(M):
    Mt = M.transpose()
    dim = M.shape[0]
    for i in range(1,dim):
        Mt[i,0:i] = M[i,0:i]
    return Mt



if __name__ == '__main__':
    readfile()
