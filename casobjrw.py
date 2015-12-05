import pickle

from casdata_pts import casdata

x = casdata('cax/e29OPT2-389-10g40mid-cas.cax')

fname = 'casobj.pic'
# Write object to file
print "Write data to file..."
with open(fname,'wb') as fp:
    pickle.dump(x,fp)
    
# Read object back from file
print "Read data from file..."
with open(fname,'rb') as fp:
    xx=pickle.load(fp)

