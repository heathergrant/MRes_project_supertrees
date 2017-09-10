from p4.stmcmc import QpaML, SpaML, SR2008ML
import numpy as np 

#read in and set up 
read('in_molluscs')
inTrees = var.trees
MRP=func.readAndPop('mrpStrictConsTree.nex')
MajR=func.readAndPop('mrpMajRuleConsTree.nex')
#SR2008=func.readAndPop('SR2008_0_minprop0cons.nex')
QPA=func.readAndPop('QPA_1_minprop50cons.nex')
SPA=func.readAndPop('SPA_1_minprop50cons.nex')
QPA.name='QPA'
SPA.name='SPA'
MRP.name='MRP'
MajR.name='MajR'
a=func.readAndPop('SPA_1_minprop50cons.nex')
QPA.taxNames=a.taxNames
SPA.taxNames=a.taxNames
MRP.taxNames=a.taxNames
MajR.taxNames=a.taxNames
#SR2008.name='SR2008'

strees=[QPA,SPA]


stml = SpaML(inTrees, SPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

stml = SpaML(inTrees, QPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

stml = QpaML(inTrees, SPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

stml = QpaML(inTrees, QPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

'''
#print(stml.ch.propTree.beta) ## BETA
#print(stml.ch.propTree.logLike) ### ML VALUE 
##up to here workee yes. 
'''
print('SPA')
stml = SpaML(inTrees, SPA)
print(stml.ch.propTree.logLike) ### ML VALUE 
print(stml.ch.propTree.optimizeQ)
print('QPA')
stml1=QpaML(inTrees, QPA)
print(stml1.ch.propTree.logLike)
#print(stml1.ch.propTree.optimizeQ)
'''
methodlist=[stmcmc.SpaML,stmcmc.QpaML]
strees=[SPA,QPA]

Ntrees=len(strees)
Nmethods=len(methodlist)

Pmatrix=np.zeros((Ntrees,Nmethods))
for ii in range(Ntrees):
    for jj in range(Nmethods):
        bigT=strees[ii]
        bigT.taxNames=a.taxNames
        stml=methodlist[jj](inTrees,bigT)
        ret=stml.ch.propTree.logLike
        Pmatrix[ii,jj]=ret
print(Pmatrix)

