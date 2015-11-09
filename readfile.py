#!/usr/bin/env python

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
    iTTL = np.arange(0,dtype='int32')
    iREA = np.arange(0,dtype='int32')
    iGPO = np.arange(0,dtype='int32')
    iPOW = np.arange(0,dtype='int32')

    for idx, line in enumerate(flines):
        if reTIT.match(line) is not None:
            iTIT = np.append(iTIT,idx)
            #print m.group()
        elif reTTL.match(line) is not None:
            iTTL = np.append(iTTL,idx)
        elif reREA.match(line) is not None:
            iREA = np.append(iREA,idx)
        elif reGPO.match(line) is not None:
            iGPO = np.append(iGPO,idx)
        elif rePOW.match(line) is not None:
            iPOW = np.append(iPOW,idx)
            

    print iGPO[0]
    print flines[iGPO[0]]
    print iGPO.size





if __name__ == '__main__':
    readfile()
