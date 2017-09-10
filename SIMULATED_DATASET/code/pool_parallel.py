import os
import multiprocessing as mpr
from subprocess import call

import time

T0=time.time()

rootdir='/home/heather/REALTHING/'
foldroot='replicate'
Nfolder=100
Nproc=4

def runp4(foldname):
    try:
        os.chdir(foldname)
        call(["p4", "/home/heather/REALTHING/code/B_input_trees_distances.py"])
        outhere=True    
    except:
        print('Folder not found!')
        outhere=False
    return outhere

# create pool
pool=mpr.Pool(processes=Nproc)

results=[]

for ii in range(1,Nfolder+1):
    foldname=rootdir+foldroot+'%d'%ii
    results.append( pool.apply_async(runp4,args=(foldname,)) )

OutList=[p.get() for p in results]

pool.close()
pool.join()

print(OutList)

Tend=time.time()-T0
print('Done in %f sec' %Tend)
