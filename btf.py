from IPython.core.debugger import Tracer

import numpy as np
import sys

import libADDC

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
    ADDC,dim = libADDC.addc(fuetype)
    addc = ADDC[:dim,:dim]

    # Define some matrices
    ndim = addc.shape[0]
    RP = np.zeros((ndim,ndim)) # Square root of power matrix
    WP = np.zeros((ndim,ndim)) # Rod weight factors

    # Calculate number of hot rods (POW[i,j] > 0)
    Ntotrods = 96 # SVEA-96
    Nhotrods = sum(sum(POW>0))

    # Determine total power for each sub bundle
    FSUB = np.zeros(4)
    FSUB[0] = sum(sum(POW[:5,:5])) # North-West quarter
    FSUB[1] = sum(sum(POW[6:,:5])) # South-West
    FSUB[2] = sum(sum(POW[:5,6:])) # North-East
    FSUB[3] = sum(sum(POW[6:,6:])) # South-East
    
    # Normalized sub bundle power distribution
    POWn = POW
    POWn[:5,:5] = POW[:5,:5]/FSUB[0] * Nhotrods/4
    POWn[6:,:5] = POW[6:,:5]/FSUB[1] * Nhotrods/4
    POWn[:5,6:] = POW[:5,6:]/FSUB[2] * Nhotrods/4
    POWn[6:,6:] = POW[6:,6:]/FSUB[3] * Nhotrods/4

    FSUBn = FSUB/FSUB.mean()

    # Calculate mismatch-factor
    MF = -0.14 + 1.5*FSUBn - 0.36*FSUBn**2




    Tracer()()
