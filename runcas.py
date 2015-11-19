from IPython.core.debugger import Tracer

import os
import sys

class runcas:

    def __init__(self,caifile,*args):
        self.caifile = caifile
        self.runcas(caifile,*args)

    def runcas(self,caifile,*args):
        
        if not os.path.isfile(caifile):
            print "Could not find file " + caifile
            return

        # Clean up directory
        if os.path.isfile(os.path.splitext(caifile)[0]+'.log'):
            os.remove(os.path.splitext(caifile)[0]+'.log')
        if os.path.isfile(os.path.splitext(caifile)[0]+'.out'):
                os.remove(os.path.splitext(caifile)[0]+'.out')
        if os.path.isfile(os.path.splitext(caifile)[0]+'.cax'):
            os.remove(os.path.splitext(caifile)[0]+'.cax')
    
        workdir = os.path.abspath(os.path.curdir)
        os.chdir(os.path.dirname(caifile)) # change dir

        if len(args) == 0: # Set default version
            casver = '4'
        else:
            casver = args[0]

        if casver is '4':
            cmd = 'linrun cas4 -V 2.05.12_MROD '+caifile+' >/dev/null 2>&1 &'
            os.system(cmd)

        os.chdir(workdir) # change back to working dir

    def procrun(self):
        
        caifile = self.caifile
        if not os.path.isfile(caifile):
            print "Could not find file " + caifile
            return

        tmpfile = os.path.dirname(caifile)+'/tmp.'+os.path.basename(caifile)
        if os.path.isfile(tmpfile):
            # Process is running
            return True
        else:
            # Process is not running
            return False

if __name__ == '__main__':
    if len(sys.argv) < 3:
        runcas(sys.argv[1])
    else:
        runcas(sys.argv[1],sys.argv[2])
