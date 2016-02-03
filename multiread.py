from multiprocessing import Pool
import time
from casdata_pts import casdata

files = []
files.append('filepath1')
files.append('filepath2')
files.append('filepath3')

start = time.time()
#for f in files:
#    d=casdata(f)

# Make the Pool of workers
n = len(files)
p = Pool(n)

# Start processes in their own threads
# and return the results
datalist = p.map(casdata, files)

#close the pool and wait for the work to finish 
p.close()
p.join()

print time.time()-start
