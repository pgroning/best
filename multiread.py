from multiprocessing import Pool
import time
from casdata_pts import casdata

files = []
files.append('cax/10g40bot/e29OPT2-382-10g40bot-cas.cax')
files.append('cax/10g40mid/e29OPT2-389-10g40mid-cas.cax')
files.append('cax/10g40top/e29OPT2-384-10g40top-cas.cax')

start = time.time()
#for f in files:
#    d=casdata(f)

# Make the Pool of workers
n = len(files)
#n=1
p = Pool(n)

# Start processes in their own threads
# and return the results
datalist = p.map(casdata, files)

#close the pool and wait for the work to finish 
p.close()
p.join()

print time.time()-start
