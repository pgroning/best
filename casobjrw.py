try:
    import cPickle as pickle
except:
    import pickle

from casdata_pts import casdata

x = casdata('cax/e29OPT2-389-10g40mid-cas.cax')

fname = 'casobj.p'
# Write object to file
print "Write data to file..."
with open(fname,'wb') as fp:
    pickle.dump(x,fp,1)
    
# Read object back from file
print "Read data from file..."
with open(fname,'rb') as fp:
    xx=pickle.load(fp)

