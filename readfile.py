#!/usr/bin/env python

# For debugging. Add Tracer()() inside the code to break at that line
from IPython.core.debugger import Tracer
# Inside iptyhon shell: run -d b<L> readfile.py
# sets a break point add line L.

import numpy as np
import re
import linecache

def readfile():
    fname = "cax/e29OPT2-389-10g40mid-cas.cax"
    #fname = "cax/e34OPT3-367-10g50mid-cas.cax"
    print "Reading file " + fname
    
    # Read input file up to maxlen using random access
    maxlen = 50000
    flines = []
    for i in range(maxlen):
        flines.append(linecache.getline(fname,i+1).rstrip())
       
    # Read the whole file
    #with open(fname) as f:
    #   #flines = f.readlines() # include \n
    #    flines = f.read().splitlines() #exclude \n

    # Search for cards
    reBWR = re.compile('^\s*BWR')
    reLFU = re.compile('^\s*LFU')
    reLPI = re.compile('^\s*LPI')
    reFUE = re.compile('^\s*FUE')
    reTTL = re.compile('^\s*TTL')
    reSIM = re.compile('^\s*SIM')
    rePDE = re.compile('^\s*PDE')
    rePIN = re.compile('^\s*PIN')
    reSLA = re.compile('^\s*SLA')
    reSPA = re.compile('^\s*SPA')
    reCRD = re.compile('^\s*CRD')
    reGAM = re.compile('^\s*GAM')
    reWRI = re.compile('^\s*WRI')
    reSTA = re.compile('^\s*STA')
    reEND = re.compile('^\s*END')
    reTMO = re.compile('^\s*TMO')
    reTFU = re.compile('^\s*TFU')
    reVOI = re.compile('^\s*VOI')
    
    # Setup empty integer array
    iBWR = np.arange(0,dtype='int32')
    iLFU = np.arange(0,dtype='int32')
    iLPI = np.arange(0,dtype='int32')
    iFUE = np.arange(0,dtype='int32')

    for i, line in enumerate(flines):
        if reBWR.match(line) is not None:
            iBWR = np.append(iBWR,i)
        elif reLFU.match(line) is not None:
            iLFU = np.append(iLFU,i)
        elif reLPI.match(line) is not None:
            iLPI = np.append(iLPI,i)
        elif reFUE.match(line) is not None:
            iFUE = np.append(iFUE,i)

    # Read fuel dimension
    npst = int(flines[iBWR[0]][5:7])
    
    # Read LFU map
    caxmap = flines[iLFU[0]+1:iLFU[0]+1+npst]
    LFU = symtrans(map2mat(caxmap,npst)).astype(int)

    # Read LPI map
    caxmap = flines[iLPI[0]+1:iLPI[0]+1+npst]
    LPI = symtrans(map2mat(caxmap,npst)).astype(int)

    # Read FUE
    



#    reBWR = re.compile('^\s*BWR')
#    for line in flines:
#        if reBWR.match(line) is not None:
#            fuedim = int(line[5:7])
#            break


    Tracer()()

    # Check if S3C card exists
    S3C = False
    reS3C = re.compile('(^| )S3C')
    for i,line in enumerate(flines):
        if reS3C.match(line) is not None:
            iS3C = i
            S3C = True
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
        #if idx == 50000: # Max number of rows to scan
        #    break

    if iGPO.size >= iREA.size:
        iPOW = iGPO

    # Calculate burnup points
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

    POW = np.zeros((fuedim,fuedim,Nburnpts)); POW.fill(np.nan)
    for i in range(Nburnpts):
        caxmap = flines[iPOW[i]+2:iPOW[i]+2+fuedim]
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
        #rvec = rstr.strip().split(' ')
        rvec = re.split('\s+',rstr.strip())
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
