from IPython.core.debugger import Tracer

import os
#import sys


def runcas(caifile,*args):

    if not os.path.isfile(caifile):
        print "Could not open file " + caifile
        return
    
    # Remove existing files
    if os.path.isfile(os.path.splitext(caifile)[0]+'.log'):
        os.remove(os.path.splitext(caifile)[0]+'.log')
    if os.path.isfile(os.path.splitext(caifile)[0]+'.out'):
        os.remove(os.path.splitext(caifile)[0]+'.out')
    if os.path.isfile(os.path.splitext(caifile)[0]+'.cax'):
        os.remove(os.path.splitext(caifile)[0]+'.cax')
    
    os.chdir(os.path.dirname(caifile)) # change working dir

    if len(args) == 0: # Set default version
        casver = 4
    else:
        casver = args[0]


    #Tracer()()

    if casver == 4:
        cmd = 'cas4 -V 2.05.12_MROD ' + caifile + ' >/dev/null 2>&1 &'
        os.system(cmd)



#if __name__ == '__main__':
#    casdata(sys.argv[1])
