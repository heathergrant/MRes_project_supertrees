#!/Users/heathergrant/p4-phylogenetics/p4
#!/usr/bin/python

import os
import multiprocessing as mpr
from subprocess import call
import time
T0=time.time()

rootdir='/home/heather/REALTHING2/'
foldroot='replicate'
Nfolder=100
Nproc=10


#for ii in range(1,Nfolder+1):
#    os.system('mkdir replicate%i/QPA_gubbins' %ii)

def runp4(foldname):
    try:
        os.chdir(foldname)
        call(["p4", "/home/heather/REALTHING2/code/F_QPA.py"])
        outhere=True    
    except:
        print('Folder not found!')
        outhere=False
    return outhere


# create pool
pool=mpr.Pool(processes=Nproc)

results=[]

for ii in range(1,Nfolder+1):
    foldname='/home/heather/REALTHING2/replicate%i/QPA_gubbins' %ii
    results.append( pool.apply_async(runp4,args=(foldname,)) )

OutList=[p.get() for p in results]

pool.close()
pool.join()

print(OutList)

Tend=time.time()-T0
print('Done in %f sec' %Tend)
