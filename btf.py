from IPython.core.debugger import Tracer

import numpy as np
import sys

sys.path.append('/home/prog/dvlp/PERG/python/LIBADDC/lib/')
import libADDC
#from addc import addc

def btf(fuetype,POW):
    print "Calculating btf... 447"
    
    # temp power dist
    POW = np.array([[ 0.   ,  1.15 ,  1.155,  1.183,  1.019,  0.   ,  0.991,  1.094,
         1.159,  1.154,  0.   ],
       [ 1.15 ,  1.103,  1.164,  0.371,  1.14 ,  0.   ,  1.115,  0.361,
         0.964,  0.379,  1.126],
       [ 1.155,  1.164,  1.089,  0.992,  1.066,  0.   ,  1.044,  0.949,
         0.919,  0.999,  1.1  ],
       [ 1.183,  0.371,  0.992,  0.981,  1.183,  0.   ,  1.092,  0.943,
         0.943,  0.355,  1.15 ],
       [ 1.019,  1.14 ,  1.066,  1.183,  0.   ,  0.   ,  0.   ,  1.086,
         1.02 ,  1.092,  1.059],
       [ 0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.   ,  0.   ,
         0.   ,  0.   ,  0.   ],
       [ 0.991,  1.115,  1.044,  1.092,  0.   ,  0.   ,  0.   ,  1.164,
         1.03 ,  1.097,  1.076],
       [ 1.094,  0.361,  0.949,  0.943,  1.086,  0.   ,  1.164,  0.954,
         0.978,  0.364,  1.212],
       [ 1.159,  0.964,  0.919,  0.943,  1.02 ,  0.   ,  1.03 ,  0.978,
         1.015,  1.223,  1.218],
       [ 1.154,  0.379,  0.999,  0.355,  1.092,  0.   ,  1.097,  0.364,
         1.223,  1.011,  1.048],
       [ 0.   ,  1.126,  1.1  ,  1.15 ,  1.059,  0.   ,  1.076,  1.212,
         1.218,  1.048,  0.   ]])


    # Import addc from shared lib
    print fuetype
    #acObj = addc(fuetype)
    #ac = acObj.addc
    AC,dim = libADDC.addc(fuetype)
    AC = AC[:dim,:dim]

    # Define some matrices
    nside = AC.shape[0] # Number of side pins of the assembly
    dim = nside + 2 # Pin map storage dimension
    #RP = np.zeros((dim,dim)) # Square root of power matrix
    #WP = np.zeros((dim,dim)) # Rod weight factors

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
    #POWn = POW
    POW[:5,:5] = POW[:5,:5]/FSUB[0] * Nhotrods/4
    POW[6:,:5] = POW[6:,:5]/FSUB[1] * Nhotrods/4
    POW[:5,6:] = POW[:5,6:]/FSUB[2] * Nhotrods/4
    POW[6:,6:] = POW[6:,6:]/FSUB[3] * Nhotrods/4

    FSUB = FSUB/FSUB.mean()

    # Calculate mismatch-factor
    MF = -0.14 + 1.5*FSUB - 0.36*FSUB**2

    # Calculate square root of power
    RP = np.zeros((dim,dim))
    RP[1:nside+1,1:nside+1] = np.sqrt(POW)
    
    # Define Rod Weight factors
    WP = np.zeros((dim,dim))
    WP[1:nside+1,1:nside+1] = np.ones((nside,nside))
    
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
                

    # Apply mismatch-factor to sub bundles
    DOW[:5,:5] = DOW[:5,:5] * MF[0]
    DOW[6:,:5] = DOW[6:,:5] * MF[1]
    DOW[:5,6:] = DOW[:5,6:] * MF[2]
    DOW[6:,6:] = DOW[6:,6:] * MF[3]

    # Apply corner rod protection.
    # The R-factor should be increased about half of the desired CPR correction
    crpfact = 0.02
    DOW[0,0] = DOW[0,0]                         * (1.0 + crpfact*0.5)
    DOW[0,nside-1] = DOW[0,nside-1]             * (1.0 + crpfact*0.5)
    DOW[nside-1,0] = DOW[nside-1,0]             * (1.0 + crpfact*0.5)
    DOW[nside-1,nside-1] = DOW[nside-1,nside-1] * (1.0 + crpfact*0.5)

    # Calculate the max R-factor for the assembly
    Rfact = DOW.max()


    Tracer()()

if __name__ == '__main__':
    btf(sys.argv[1],sys.argv[2])
