from IPython.core.debugger import Tracer

import numpy as np
import sys

sys.path.append('/home/prog/dvlp/PERG/python/LIBADDC/lib/')
#import libADDC
from addc import addc

def acc_weifun(x):
    if x <= 0.06:
        f = 0.0
    elif x <= 0.279:
        f = -0.201924 + 3.40947*x - 12.3305*x**3 + 24.486*x**5
    elif x <= 0.96:
        f = 0.332027 + 0.684359*x
    else:
        f = 1.0
    return f

def node_weight(z,naxial_nodes):
    x1 = 1-(z-1)/float(naxial_nodes)
    x2 = 1-z/float(naxial_nodes)
    f1 = acc_weifun(x1)
    f2 = acc_weifun(x2)
    wz = f1-f2
    return wz

def rfact_axial(fuetype,POW):
    # Calculating axial R-factor
    
    # Import addc from shared lib
    #print fuetype
    acObj = addc(fuetype)
    AC = acObj.addc
    #AC,dim = libADDC.addc(fuetype)
    #AC = AC[:dim,:dim]

    # Define some matrices
    nside = AC.shape[0] # Number of side pins of the assembly
    dim = nside + 2 # Pin map storage dimension

    # Calculate number of hot rods (POW[i,j] > 0)
    Ntotrods = 96 # Total number of rods for SVEA-96
    Nhotrods = sum(sum(POW>0)) # Number of hot rods

    # Determine total power for each sub bundle
    FSUB = np.zeros(4)
    FSUB[0] = sum(sum(POW[:5,:5])) # North-West quarter
    FSUB[1] = sum(sum(POW[6:,:5])) # South-West
    FSUB[2] = sum(sum(POW[:5,6:])) # North-East
    FSUB[3] = sum(sum(POW[6:,6:])) # South-East
    
    # Normalized sub bundle power distribution
    POW[:5,:5] = POW[:5,:5]/FSUB[0] * Nhotrods/4
    POW[6:,:5] = POW[6:,:5]/FSUB[1] * Nhotrods/4
    POW[:5,6:] = POW[:5,6:]/FSUB[2] * Nhotrods/4
    POW[6:,6:] = POW[6:,6:]/FSUB[3] * Nhotrods/4

    #FSUB = FSUB/FSUB.mean()

    # Calculate mismatch-factor
    #MF = -0.14 + 1.5*FSUB - 0.36*FSUB**2

    # Calculate square root of power
    RP = np.zeros((dim,dim))
    RP[1:nside+1,1:nside+1] = np.sqrt(POW)
    
    # Define Rod Weight factors
    WP = np.zeros((dim,dim))
    WP[1:nside+1,1:nside+1] = np.ones((nside,nside))
    
    # PLR (modeled as cold rods)
    # For cold rods the weighting factor is 0.25 of the value of heated rod in that position
    # PLR (1/3)
    if POW[0,0]   < 0.0001: WP[1,1]   = 0.25
    if POW[0,10]  < 0.0001: WP[1,11]  = 0.25
    if POW[10,0]  < 0.0001: WP[11,1]  = 0.25
    if POW[10,10] < 0.0001: WP[11,11] = 0.25
    # PLR (2/3)
    if POW[3,4]   < 0.0001: WP[4,5]   = 0.25
    if POW[4,3]   < 0.0001: WP[5,4]   = 0.25
    if POW[3,6]   < 0.0001: WP[4,7]   = 0.25
    if POW[4,7]   < 0.0001: WP[5,8]   = 0.25   
    if POW[6,3]   < 0.0001: WP[7,4]   = 0.25
    if POW[7,4]   < 0.0001: WP[8,5]   = 0.25
    if POW[6,7]   < 0.0001: WP[7,8]   = 0.25
    if POW[7,6]   < 0.0001: WP[8,7]   = 0.25

    # Calculate pinwise R-factors for fuel-rods where POW > 0
    DOW = np.zeros((nside,nside))
    # Side rods
    WJ = 0.25  # Weighting factor for side neighboring rods
    WK = 0.125 # Weighting factor for diagonal neighboring rods
    for i in range(1,nside+1):
        for j in range(1,nside+1):
            if RP[i,j] > 0:
                # Side rods
                SJ1 = (RP[i-1,j]*WP[i-1,j] + RP[i+1,j]*WP[i+1,j] + 
                RP[i,j-1]*WP[i,j-1] + RP[i,j+1]*WP[i,j+1])*WJ

                SJ2 = (WP[i-1,j] + WP[i+1,j] +
                WP[i,j-1] + WP[i,j+1])*WJ*RP[i,j]

                SJ = min([SJ1,SJ2])
                # Diagonal rods
                SK1 = (RP[i-1,j-1]*WP[i-1,j-1] + RP[i+1,j-1]*WP[i+1,j-1] +
                RP[i-1,j+1]*WP[i-1,j+1] + RP[i+1,j+1]*WP[i+1,j+1])*WK

                SK2 = (WP[i-1,j-1] + WP[i+1,j-1] +
                WP[i-1,j+1] + WP[i+1,j+1])*WK*RP[i,j]

                SK = min([SK1,SK2])

                # Sum weighting factors
                SWJ = (WP[i-1,j] + WP[i+1,j] + WP[i,j-1] + WP[i,j+1])*WJ # Side rods
                SWK = (WP[i-1,j-1] + WP[i+1,j-1] + WP[i-1,j+1] + WP[i+1,j+1])*WK # Diagonal rods

                DOW[i-1,j-1] = (RP[i,j] + SJ + SK)/(1.0 + SWJ + SWK)*np.sqrt(Ntotrods/Nhotrods) + AC[i-1,j-1]
                

    # Apply corner rod protection.
    # The R-factor should be increased about half of the desired CPR correction
    #crpfact = 0.02
    #DOW[0,0] = DOW[0,0]                         * (1.0 + crpfact*0.5)
    #DOW[0,nside-1] = DOW[0,nside-1]             * (1.0 + crpfact*0.5)
    #DOW[nside-1,0] = DOW[nside-1,0]             * (1.0 + crpfact*0.5)
    #DOW[nside-1,nside-1] = DOW[nside-1,nside-1] * (1.0 + crpfact*0.5)

    # Calculate the max R-factor for the assembly
    Rfact = DOW.max()
    
    return DOW


def calc_btf(fuetype):

    naxial_nodes = 25

    # Setup part length rod maps
    Mplr1 = np.zeros((11,11)) # PLR (1/3) map
    Mplr1[0,0]=Mplr1[0,10]=Mplr1[10,0]=Mplr1[10,10]=1

    Mplr2 = np.zeros((11,11)) # PLR (2/3) map
    Mplr2[3,4]=Mplr2[4,3]=Mplr2[3,6]=Mplr2[6,3]=1
    Mplr2[4,7]=Mplr2[7,4]=Mplr2[6,7]=Mplr2[7,6]=1

    Mflr = 1-Mplr1-Mplr2

    # read power dist
    POW = np.loadtxt('./powdist.txt')
    MF = np.zeros((naxial_nodes,4))
    DOW = np.zeros((naxial_nodes,POW[0].size,POW[1].size))
    WZ = np.zeros(naxial_nodes)
    Raxw = np.zeros(POW.shape)
    MFpl = np.zeros(4)

    for z in range(naxial_nodes):
        
        # Calculate number of hot rods (POW[i,j] > 0)
        Ntotrods = 96 # Total number of rods for SVEA-96
        Nhotrods = sum(sum(POW>0)) # Number of hot rods
        

        # *****Mismatch factor calculation*****
        
        # Determine total power for each sub bundle
        FSUB = np.zeros(4)
        FSUB[0] = sum(sum(POW[:5,:5])) # North-West quarter
        FSUB[1] = sum(sum(POW[6:,:5])) # South-West
        FSUB[2] = sum(sum(POW[:5,6:])) # North-East
        FSUB[3] = sum(sum(POW[6:,6:])) # South-East
        # Normalize sub-bundle power
        FSUB = FSUB/FSUB.mean()

        # Calculate mismatch-factor for each sub-bundle
        MF[z,:] = -0.14 + 1.5*FSUB - 0.36*FSUB**2
        
        # Part length rods (PLR) (Sum over nodes)
        #MFpl += MF

        DOW[z,:,:] = rfact_axial(fuetype,POW)
        WZ[z] = node_weight(z+1,naxial_nodes)
        
        
    # Apply mismatch-factor to FLRs only (PLRs are taken care of separately)
    for z in range(naxial_nodes):
        for i in range(DOW[0][0].size):
            for j in range(DOW[0][1].size):
                if Mflr[i,j]:
                    if i<5 and j<5:
                        DOW[z,i,j] = DOW[z,i,j] * MF[z,0]
                    elif i<11 and j<5:
                        DOW[z,i,j] = DOW[z,i,j] * MF[z,1]
                    elif i<5 and j<11:
                        DOW[z,i,j] = DOW[z,i,j] * MF[z,2]
                    elif i<11 and j<11:
                        DOW[z,i,j] = DOW[z,i,j] * MF[z,3]
    

        # Apply axial weight function
        #WZ[z-1] = node_weight(z,naxial_nodes)
        #Raxw += DOW*WZ

                
    # Apply average mismatch-factor (along z-direction) for PLRs
    MFpl = MF.mean(0)
    Mplr = Mplr1 + Mplr2
    
    for z in range(naxial_nodes):
        for i in range(DOW[0][0].size):
            for j in range(DOW[0][1].size):
                if Mplr[i,j]:
                    if i<5 and j<5:
                        DOW[z,i,j] = DOW[z,i,j] * MFpl[0]
                    elif i<11 and j<5:
                        DOW[z,i,j] = DOW[z,i,j] * MFpl[1]
                    elif i<5 and j<11:
                        DOW[z,i,j] = DOW[z,i,j] * MFpl[2]
                    elif i<11 and j<11:
                        DOW[z,i,j] = DOW[z,i,j] * MFpl[3]

    # Integrate along z-direction and apply axial weight function
    

    Tracer()()




if __name__ == '__main__':
    calc_btf(sys.argv[1])
