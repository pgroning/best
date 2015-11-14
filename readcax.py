#!/usr/bin/env python

# > from readcax import readcax
# > data = readcax('fname')


# For debugging. Add Tracer()() inside the code to break at that line
#from IPython.core.debugger import Tracer
# Inside iptyhon shell: run -d b<L> readfile.py
# sets a break point add line L.

import numpy as np
import re
import linecache
import os.path

class readcax:

    def __init__(self,fname):
        self.readcax(fname)
        

    def readcax(self,fname):
        #fname = "cax/e29OPT2-389-10g40mid-cas.cax"
        #fname = "cax/e34OPT3-367-10g50mid-cas.cax"
        #print "Reading file " + fname
        
        # Read input file up to maxlen using random access
        if not os.path.isfile(fname):
            print "Could not open file " + fname
            return
        else:
            print "Reading file " + fname

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
        reFUE = re.compile('^\s*FUE\s+')
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
        reS3C = re.compile('(^| )S3C')
        reTIT = re.compile('^TIT')
        reTTL = re.compile('^\*I TTL')
        reREA = re.compile('REA\s+')
        reGPO = re.compile('GPO\s+')
        rePOW = re.compile('POW\s+')
        
        # Setup empty integer arrays
        iEND = np.arange(0,dtype='int32')
        iBWR = np.arange(0,dtype='int32')
        iLFU = np.arange(0,dtype='int32')
        iLPI = np.arange(0,dtype='int32')
        iFUE = np.arange(0,dtype='int32')
        iPIN = np.arange(0,dtype='int32')
        iTIT = np.arange(0,dtype='int32')
        iTTL = np.arange(0,dtype='int32')
        iREA = np.arange(0,dtype='int32')
        iGPO = np.arange(0,dtype='int32')
        iPOW = np.arange(0,dtype='int32')
        
        # Search for regexp matches
        for i, line in enumerate(flines):
            if reEND.match(line) is not None:
                iEND = np.append(iEND,i)
            elif reBWR.match(line) is not None:
                iBWR = np.append(iBWR,i)
            elif reLFU.match(line) is not None:
                iLFU = np.append(iLFU,i)
            elif reLPI.match(line) is not None:
                iLPI = np.append(iLPI,i)
            elif reFUE.match(line) is not None:
                iFUE = np.append(iFUE,i)
            elif rePIN.match(line) is not None:
                iPIN = np.append(iPIN,i)
            elif reTIT.match(line) is not None:
                iTIT = np.append(iTIT,i)
            elif reTTL.match(line) is not None:
                iTTL = np.append(iTTL,i)
            elif reREA.match(line) is not None:
                iREA = np.append(iREA,i)
            elif reGPO.match(line) is not None:
                iGPO = np.append(iGPO,i)
            elif rePOW.match(line) is not None:
                iPOW = np.append(iPOW,i)

        # Read fuel dimension
        npst = int(flines[iBWR[0]][5:7])
        
        # Read LFU map
        caxmap = flines[iLFU[0]+1:iLFU[0]+1+npst]
        LFU = self.__symtrans(self.__map2mat(caxmap,npst)).astype(int)
        
        # Determine fuel type
        
        
        # Read LPI map
        caxmap = flines[iLPI[0]+1:iLPI[0]+1+npst]
        LPI = self.__symtrans(self.__map2mat(caxmap,npst)).astype(int)
            
        # Read FUE
        iFUE = iFUE[iFUE<iEND[0]]
        Nfue = iFUE.size
        FUE = np.zeros((Nfue,5)); FUE.fill(np.nan)
        for i,idx in enumerate(iFUE):
            rvec = re.split('\*',flines[idx].strip())
            rstr = rvec[0]
            rvec = re.split('\s+',rstr.strip())
            FUE[i,0] = rvec[1]
            FUE[i,1:3] = re.split('/',rvec[2])
            if np.size(rvec) > 3:
                FUE[i,3:5] = re.split('=',rvec[3])
                
        # Determine number of BA rods types
        Nba = 0
        for content in FUE[:,4]:
            if np.isnan(content) == False:
                Nba += 1
                
        # Read PIN
        Npin = iPIN.size
        
        # Read SLA
            
        
        # Calculate burnup points
        
        # Check if S3C card exists
        S3C = False
        for i,line in enumerate(flines):
            if reS3C.match(line) is not None:
                iS3C = i
                S3C = True
                break
                
        if iGPO.size >= iREA.size: # Use gamma smearing power
            iPOW = iGPO
            
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
        Kinf = np.zeros(Nburnpts); Kinf.fill(np.nan)
        for i in range(Nburnpts):
            burnup[i] = flines[iTITbp[i]+2][0:6]
            Kinf[i] = flines[iREAbp[i]+1][0:12]

        
        # Read radial power distribution map
        
        POW = np.zeros((npst,npst,Nburnpts)); POW.fill(np.nan)
        for i in range(Nburnpts):
            caxmap = flines[iPOW[i]+2:iPOW[i]+2+npst]
            M = self.__symtrans(self.__map2mat(caxmap,npst))
            POW[:,:,i] = M
            
        # Calculate Fint
        Fint = np.zeros(Nburnpts); Fint.fill(np.nan)
        for i in range(Nburnpts):
            Fint[i] = POW[:,:,i].max()

        # Calculate radial burnup distribution
        EXP = np.zeros((npst,npst,Nburnpts)); EXP.fill(np.nan)
        EXP[:,:,0] = 0 # Initial burnup
        for i in range(1,Nburnpts):
            dburn = burnup[i] - burnup[i-1]
            EXP[:,:,i] = EXP[:,:,i-1] + POW[:,:,i]*dburn
            
        self.fname = fname
        self.burnup = burnup
        self.Kinf = Kinf
        self.Fint = Fint
        self.EXP = EXP


    def __map2mat(self,caxmap,dim):
        M = np.zeros((dim,dim)); M.fill(np.nan)
        for i in range(dim):
            rstr = caxmap[i]
            rvec = re.split('\s+',rstr.strip())
            M[i,0:i+1] = rvec
        return M

    def __symtrans(self,M):
        Mt = M.transpose()
        dim = M.shape[0]
        for i in range(1,dim):
            Mt[i,0:i] = M[i,0:i]
        return Mt
        

if __name__ == '__main__':
    readcax()
