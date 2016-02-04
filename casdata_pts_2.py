#!/usr/bin/env python

# Run from ipython:
# > from casdata import casdata
# > case = casdata('caxfile')
#
# or:
# run casdata "caxfile"
#

# For debugging. Add Tracer()() inside the code to break at that line
from IPython.core.debugger import Tracer
# Inside iptyhon shell: run -d b<L> readfile.py
# sets a break point add line L.

import numpy as np
import re
import linecache
import os.path
import sys
#import time
#from multiprocessing import Pool
#from btf import btf

class datastruct:
    """Dummy class used to structure data"""
    pass


class casdata:

    def __init__(self,caxfile):
        self.data = datastruct()
        self.statepts = []
        self.readcax(caxfile)
        self.__ave_enr()
        #self.writecai()
        #self.btfcalc()


    # -------Read cax file---------
    def __matchcontent(self,flines,regexp,opt='all'):
        rec = re.compile(regexp)
        if opt == 'all':
            out = [i for i,x in enumerate(flines) if rec.match(x)]
        elif opt == 'next':
            out = next(i for i,x in enumerate(flines) if rec.match(x))
        elif opt == 'object':
            out = (i for i,x in enumerate(flines) if rec.match(x))
        return out

    def readcax(self,caxfile):
        
        if not os.path.isfile(caxfile):
            print "Could not open file " + caxfile
            return
        else:
            print "Reading file " + caxfile
                
        # Read input file up to maxlen using random access
        #maxlen = 100000
        #flines = []
        #for i in range(maxlen):
        #    flines.append(linecache.getline(caxfile,i+1).rstrip())

        # Read the whole file
        with open(caxfile) as f:
           #flines = f.readlines() # include \n
            flines = f.read().splitlines() #exclude \n
        
        # Define regexps
        #reS3C = re.compile('(^| )S3C')
        #reITTL = re.compile('^\*I TTL')
        #reREA = re.compile('REA\s+')
        #reGPO = re.compile('GPO\s+')

        # Search for regexp matches
        print "Scanning file content..."
        
        # Loop through the whole file content
        #reglist = ['^TIT','^\s*FUE\s+']
        #self.__flines = flines
        #n = 2
        #p = Pool(n)
        #ilist = p.map(self.matchcontent, reglist)
        #p.close()
        #p.join()
        iTIT = self.__matchcontent(flines,'^TIT')
        iFUE = self.__matchcontent(flines,'^\s*FUE\s+')
        iPOW = self.__matchcontent(flines,'POW\s+')
        iSIM = self.__matchcontent(flines,'^\s*SIM')
        iSPA = self.__matchcontent(flines,'^\s*SPA')
        iGAM = self.__matchcontent(flines,'^\s*GAM')
        iCRD = self.__matchcontent(flines,'^\s*CRD')
        iPOL = self.__matchcontent(flines,'^POL')
        iXFL = self.__matchcontent(flines,'^XFL')
        iPIN = self.__matchcontent(flines,'^\s*PIN')
        iTTL = self.__matchcontent(flines,'^\s*TTL')
        iVOI = self.__matchcontent(flines,'^\s*VOI')
        iDEP = self.__matchcontent(flines,'^\s*DEP')
        
        # Stop looping at first finding
        iEND = self.__matchcontent(flines,'^\s*END','next')
        iBWR = self.__matchcontent(flines,'^\s*BWR','next')
        iLFU = self.__matchcontent(flines,'^\s*LFU','next')
        iLPI = self.__matchcontent(flines,'^\s*LPI','next')
        iTFU = self.__matchcontent(flines,'^\s*TFU','next')
        iTMO = self.__matchcontent(flines,'^\s*TMO','next')
        iPDE = self.__matchcontent(flines,'^\s*PDE','next')
        iSLA = self.__matchcontent(flines,'^\s*SLA','next')
        iWRI = self.__matchcontent(flines,'^\s*WRI','next')
        iSTA = self.__matchcontent(flines,'^\s*STA','next')
        print "Done."
        #Tracer()()
        # Read title
        #self.title = flines[iTTL[0]]
        self.data.title = flines[iTTL[0]]
        # SIM
        #self.sim = flines[iSIM[0]]
        self.data.sim = flines[iSIM[0]]
        # TFU
        #self.tfu = flines[iTFU]
        self.data.tfu = flines[iTFU]
        # TMO
        #self.tmo = flines[iTMO]
        self.data.tmo = flines[iTMO]
        # VOI
        #self.voi = flines[iVOI[0]]
        self.data.voi = flines[iVOI[0]]
        # PDE
        #self.pde = flines[iPDE]
        self.data.pde = flines[iPDE]
        # BWR
        #self.bwr = flines[iBWR]
        self.data.bwr = flines[iBWR]
        # SPA
        #self.spa = flines[iSPA[0]]
        self.data.spa = flines[iSPA[0]]
        # DEP
        #self.dep = flines[iDEP[0]]
        self.data.dep = flines[iDEP[0]]
        # GAM
        #self.gam = flines[iGAM[0]]
        self.data.gam = flines[iGAM[0]]
        # WRI
        #self.wri = flines[iWRI]
        self.data.wri = flines[iWRI]
        # STA
        #self.sta = flines[iSTA]
        self.data.sta = flines[iSTA]
        # CRD
        #self.crd = flines[iCRD[0]]
        self.data.crd = flines[iCRD[0]]

        # Read fuel dimension
        npst = int(flines[iBWR][5:7])
        
        # Read LFU map
        caxmap = flines[iLFU+1:iLFU+1+npst]
        LFU = self.__symtrans(self.__map2mat(caxmap,npst)).astype(int)

        # Read LPI map
        caxmap = flines[iLPI+1:iLPI+1+npst]
        LPI = self.__symtrans(self.__map2mat(caxmap,npst)).astype(int)
        
        # Read FUE
        #iFUE = iFUE[iFUE<iEND[0]]
        iFUE = [i for i in iFUE if i<iEND]
        #iFUE = filter(lambda x,y=iEND:x<y,iFUE)
        #Nfue = iFUE.size
        Nfue = len(iFUE)
        FUE = np.zeros((Nfue,5)); FUE.fill(np.nan)
        for i,idx in enumerate(iFUE):
            rvec = re.split('\*',flines[idx].strip())
            rstr = rvec[0]
            rvec = re.split('\s+',rstr.strip())
            FUE[i,0] = rvec[1]
            FUE[i,1:3] = re.split('/',rvec[2])
            if np.size(rvec) > 3:
                FUE[i,3:5] = re.split('=',rvec[3])
        
        # Translate LFU map to ENR map
        ENR = np.zeros((npst,npst)); #ENR.fill(np.nan)
        for i in range(Nfue):
            ifu = int(FUE[i,0])
            ENR[LFU==ifu] = FUE[i,2]

        # Translate LFU map to BA map
        BA = np.zeros((npst,npst)); #BA.fill(np.nan)
        for i in range(Nfue):
            ifu = int(FUE[i,0])
            if np.isnan(FUE[i,3]):
                BA[LFU==ifu] = 0.0
            else:
                BA[LFU==ifu] = FUE[i,4]
        
        # Determine number of BA rods types
        Nba = 0
        for content in FUE[:,4]:
            if np.isnan(content) == False:
                Nba += 1
                
        # Read PIN (pin radius)
        #Npin = iPIN.size
        Npin = len(iPIN)
        ncol = 4
        PIN = np.zeros((Npin,ncol)); PIN.fill(np.nan)
        for i,idx in enumerate(iPIN):
            rvec = re.split(',|/',flines[idx].strip())
            rstr = rvec[0]
            rvec = re.split('\s+',rstr.strip())
            rlen = np.size(rvec)
            PIN[i,:rlen-1] = rvec[1:ncol+1]

        #self.pinlines = flines[iPIN[0]:iPIN[0]+Npin]
        self.data.pinlines = flines[iPIN[0]:iPIN[0]+Npin]

        # Read SLA
        #Nsla = iSLA.size
        #self.slalines = flines[iSLA[0]:iSLA[0]+Nsla]
        #self.slalines = flines[iSLA]
        self.data.slalines = flines[iSLA]

        # ------Step through the state points----------
        print "Stepping through state points..."

        #Tracer()()
        #Nburnpts = iTIT.size
        Nburnpts = len(iTIT)
        #titcrd = []
        burnup = np.zeros(Nburnpts); burnup.fill(np.nan)
        voi = np.zeros(Nburnpts); voi.fill(np.nan)
        vhi = np.zeros(Nburnpts); vhi.fill(np.nan)
        tfu = np.zeros(Nburnpts); tfu.fill(np.nan)
        tmo = np.zeros(Nburnpts); tmo.fill(np.nan)
        kinf = np.zeros(Nburnpts); kinf.fill(np.nan)
        POW = np.zeros((npst,npst,Nburnpts)); POW.fill(np.nan)
        XFL1 = np.zeros((npst,npst,Nburnpts)); XFL1.fill(np.nan)
        XFL2 = np.zeros((npst,npst,Nburnpts)); XFL2.fill(np.nan)

        # Read title cards
        titcrd = [flines[i] for i in iTIT]
        
        # Row vector containing burnup, voi, vhi, tfu and tmo
        rvec = [re.split('/',flines[i+2].strip()) for i in iTIT]

        # Row containing Kinf
        kinfstr = [flines[i+5] for i in iPOL]
 
        # Rows containing radial power distribution map
        powmap = [flines[i+2:i+2+npst] for i in iPOW]

        # Rows containing XFL maps
        xfl1map = [flines[i+2:i+2+npst] for i in iXFL]
        xfl2map = [flines[i+3+npst:i+3+2*npst] for i in iXFL]

        #Tracer()()
        for i in range(Nburnpts):
            # Read burnup, voids, tfu and tmo
            burnup[i],voi[i] = re.split('\s+',rvec[i][0].strip())
            vhi[i],tfu[i] = re.split('\s+',rvec[i][1].strip())
            tmo[i] = re.split('\s+',rvec[i][2].strip())[1]
            # Read kinf
            kinf[i] = re.split('\s+',kinfstr[i].strip())[0]
            # Read radial power distribution map
            POW[:,:,i] = self.__symtrans(self.__map2mat(powmap[i],npst))
            # Read XFL maps
            XFL1[:,:,i] = self.__symtrans(self.__map2mat(xfl1map[i],npst))
            XFL2[:,:,i] = self.__symtrans(self.__map2mat(xfl2map[i],npst))
        print "Done."
        #Tracer()()
        # -----------------------------------------------------------------------

        # Calculate radial burnup distributions
        EXP = np.zeros((npst,npst,Nburnpts)); EXP.fill(np.nan)
        for i in range(Nburnpts):
            if burnup[i] == 0:
                EXP[:,:,i] = 0
            else:
                dburn = burnup[i] - burnup[i-1]
                EXP[:,:,i] = EXP[:,:,i-1] + POW[:,:,i]*dburn


        # Calculate Fint:
        fint = np.zeros(Nburnpts); fint.fill(np.nan)
        for i in range(Nburnpts):
            fint[i] = POW[:,:,i].max()

        # Append state instancies
        for i in range(Nburnpts):
            self.statepts.append(datastruct()) # append new instance to list
            #state = data()
            self.statepts[i].titcrd = titcrd[i]
            self.statepts[i].burnup = burnup[i]
            #state.burnup = burnup[i]
            self.statepts[i].voi = voi[i]
            #state.voi = voi[i]
            self.statepts[i].vhi = vhi[i]
            #state.vhi = vhi[i]
            self.statepts[i].tfu = tfu[i]
            #state.tfu = tfu[i]
            self.statepts[i].tmo = tmo[i]
            #state.tmo = tmo[i]
            self.statepts[i].kinf = kinf[i]
            #state.kinf = kinf[i]
            self.statepts[i].fint = fint[i]
            #state.fint = fint[i]
            self.statepts[i].EXP = EXP[:,:,i]
            #state.EXP = EXP[:,:,i]
            self.statepts[i].XFL1 = XFL1[:,:,i]
            #state.XFL1 = XFL1[:,:,i]
            self.statepts[i].XFL2 = XFL2[:,:,i]
            #state.XFL2 = XFL2[:,:,i]
            self.statepts[i].POW = POW[:,:,i]
            #state.POW = POW[:,:,i]
            #self.data["statepts"].append(state)
        
        #Tracer()()
        # Saving geninfo
        #self.geninfo = data()
        self.data.caxfile = caxfile
        #info.caxfile = caxfile
        self.data.ENR = ENR
        #info.ENR = ENR
        self.data.BA = BA
        #info.BA = BA
        self.data.PIN = PIN
        #info.PIN = PIN
        self.data.LPI = LPI
        #info.LPI = LPI
        self.data.FUE = FUE
        #info.FUE = FUE
        self.data.LFU = LFU
        #info.LFU = LFU
        self.data.npst = npst
        #info.npst = npst
        #self.data['geninfo'] = info

        #self.caxfile = caxfile
        #self.burnvec = burnup
        #self.voivec = voi
        #self.vhivec = vhi
        #self.tfuvec = tfu
        #self.tmovec = tmo
        #self.kinf = kinf
        #self.fint = fint
        #self.EXP = EXP
        #self.ENR = ENR
        #self.BA = BA
        #self.PIN = PIN
        #self.LPI = LPI
        #self.FUE = FUE
        #self.LFU = LFU
        #self.npst = npst
        #self.POW = POW
        #self.XFL1 = XFL1
        #self.XFL2 = XFL2

#    def btfcalc(self):
#        btf('SVEA-96','')
        
        
        

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


#    #---------Calculate Fint-------------
#    def fint(self):
#        Nburnpts = self.POW.shape[2]
#        fint = np.zeros(Nburnpts); fint.fill(np.nan)
#        for i in range(Nburnpts):
#            fint[i] = self.POW[:,:,i].max()
#        self.fint = fint

    # --------Calculate average enrichment----------
    def __ave_enr(self):
        
        # Translate LFU map to density map
        DENS = np.zeros((self.data.npst,self.data.npst));
        Nfue = self.data.FUE[:,0].size
        for i in range(Nfue):
            ifu = int(self.data.FUE[i,0])
            DENS[self.data.LFU==ifu] = self.data.FUE[i,1]
        
        # Translate LPI map to pin radius map
        RADI = np.zeros((self.data.npst,self.data.npst));
        Npin = self.data.PIN[:,0].size
        for i in range(Npin):
            ipi = int(self.data.PIN[i,0])
            RADI[self.data.LPI==ipi] = self.data.PIN[i,1]
        
        # Calculate mass
        VOLU = np.pi*RADI**2
        MASS = DENS*VOLU
        mass = np.sum(MASS)
        MASS_U235 = MASS*self.data.ENR
        mass_u235 = np.sum(MASS_U235)
        self.data.ave_enr = mass_u235/mass


    # -------Write cai file------------
    def writecai(self,caifile):
        print "Writing to file " + caifile
        
        #caifile = "cas.inp"

        f = open(caifile,'w')
        f.write(self.title + '\n')
        f.write(self.sim + '\n')
        f.write(self.tfu + '\n')
        f.write(self.tmo + '\n')
        f.write(self.voi + '\n')

        Nfue = self.FUE.shape[0]
        for i in range(Nfue):
            f.write(' FUE  %d ' % (self.FUE[i,0]))
            f.write('%5.3f/%5.3f' % (self.FUE[i,1],self.FUE[i,2]))
            if ~np.isnan(self.FUE[i,3]):
                f.write(' %d=%4.2f' % (self.FUE[i,3],self.FUE[i,4]))
            f.write('\n')

        f.write(' LFU\n')
        for i in range(self.npst):
            for j in range(i+1):
                f.write(' %d' % self.LFU[i,j])
                #if j < i: f.write(' ')
            f.write('\n')

        f.write(self.pde + '\n')

        f.write(self.bwr + '\n')

        Npin = np.size(self.pinlines)
        for i in range(Npin):
            f.write(self.pinlines[i] + '\n')
        
        Nsla = np.size(self.slalines)
        for i in range(Nsla):
            f.write(self.slalines[i] + '\n')

        f.write(' LPI\n')
        for i in range(self.npst):
            for j in range(i+1):
                f.write(' %d' % self.LPI[i,j])
                #if j < i: f.write(' ')
            f.write('\n')

        f.write(self.spa + '\n')
        f.write(self.dep + '\n')
        f.write(self.gam + '\n')
        f.write(self.wri + '\n')
        f.write(self.sta + '\n')

        f.write(' TTL\n')

        depstr = re.split('DEP',self.dep)[1].replace(',','').strip()
        f.write(' RES,,%s\n' % (depstr))

        #f.write(' RES,,0 0.5 1.5 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0 25 30 40 50 60 70\n')
        f.write(self.crd + '\n')
        f.write(' NLI\n')
        f.write(' STA\n')
        f.write(' END\n')

        f.close()

        #Tracer()()

    def findpoint(self,burnup=None,vhi=None,voi=None,tfu=None):
        """Return statepoint index that correspond to specific burnup, void and void history
        Syntax: pt = findpoint(burnup=burnup_val,vhi=vhi_val,voi=voi_val,tfu=tfu_val)"""

        if tfu is not None:
            pindex = next(i for i,p in enumerate(self.statepts) if p.tfu==tfu)
        elif burnup is not None:
            pindex = next(i for i,p in enumerate(self.statepts)
                          if p.burnup==burnup and p.vhi==vhi and p.voi==voi)
        else:
            pindex = next(i for i,p in enumerate(self.statepts)
                          if p.vhi==vhi and p.voi==voi)    
        return pindex
        

if __name__ == '__main__':
    casdata(sys.argv[1])