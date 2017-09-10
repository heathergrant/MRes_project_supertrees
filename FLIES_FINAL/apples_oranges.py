from p4.stmcmc import QpaML, SpaML, SR2008ML
import numpy as np 

#read in and set up 
read('../inTrees_drosophila.phy')
inTrees = var.trees
var.trees = []
MRP=func.readAndPop('mrpStrictConsTree.nex')
MajR=func.readAndPop('mrpMajRuleConsTree.nex')
SR2008=func.readAndPop('SR2008_1_minprop0cons.nex')
QPA=func.readAndPop('QPA_1_minprop0cons.nex')
SPA=func.readAndPop('SPA_0_minprop0cons.nex')
QPA.name='QPA'
SPA.name='SPA'
MRP.name='MRP'
MajR.name='MajR'
a=func.readAndPop('SPA_0_minprop0cons.nex')
QPA.taxNames=a.taxNames
SPA.taxNames=a.taxNames
MRP.taxNames=a.taxNames
MajR.taxNames=a.taxNames
SR2008.name='SR2008'


#print('MRP by SR model')
#stml = SR2008ML(inTrees, MRP)
#ret = stml.optimizeBeta()
#ret1=stml.ch.propTree.logLike
#print(ret, ret1)

print('MRP by SPA model')
stml = SpaML(inTrees, MRP)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('MRP by QPA model')
stml = QpaML(inTrees, MRP)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('MajR by SPA model')
stml = SpaML(inTrees, MajR)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('MajR by QPA model')
stml = QpaML(inTrees, MajR)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('SR2008 by SR2008 model')
stml = SR2008ML(inTrees, SR2008)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('SR2008 by SPAML model')
stml = SpaML(inTrees, SR2008)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('SR2008 by QPAML model')
stml = QpaML(inTrees, SR2008)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('SPA by SR2008 model')
stml = SR2008ML(inTrees, SPA)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('SPA by SpA model')
stml = SpaML(inTrees, SPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('SPA by QPA model')
stml = QpaML(inTrees, SPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('QpA by sr2008 model')
stml = SR2008ML(inTrees, QPA)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('QpA by SpA model')
stml = SpaML(inTrees, QPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('QpA by QPA model')
stml = QpaML(inTrees, QPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

methodlist=[stmcmc.SR2008ML, stmcmc.SpaML,stmcmc.QpaML]
strees=[SR2008, QPA,SPA]

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
