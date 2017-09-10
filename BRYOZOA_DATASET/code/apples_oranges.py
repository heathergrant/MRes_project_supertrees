from p4.stmcmc import QpaML, SpaML, SR2008ML
import numpy as np 

#read in and set up 
read('../fix_input_trees/t*')
inTrees = var.trees
var.trees = []
MRP_100=func.readAndPop('correct_mrpStrictConsTree.nex')
MRP_50=func.readAndPop('correct_mrpMajRuleConsTree.nex')
SR2008=func.readAndPop('BRYO_NEW_SR2008_50cons.nex')
SR2008.name='SR2008'
SPA=func.readAndPop('BRYO_NEW_SPA_50cons.nex')
SPA.name='SPA'
MRP_100.name='MRP_100'
MRP_50.name='MRP_50'
a=func.readAndPop('BRYO_NEW_SPA_50cons.nex')
SPA.taxNames=a.taxNames
MRP_100.taxNames=a.taxNames
MRP_50.taxNames=a.taxNames
total=func.readAndPop('total_evidence_f')
total.name='total_evidence'
total.taxNames=a.taxNames

print('MRP_100 by SR model')
stml = SR2008ML(inTrees, MRP_100)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('MRP_100 by SPA model')
stml = SpaML(inTrees, MRP_100)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)


print('MRP_50 by SR model')
stml = SR2008ML(inTrees, MRP_50)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('MRP_50 by SPA model')
stml = SpaML(inTrees, MRP_50)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)


print('SPA by SR model')
stml = SR2008ML(inTrees, SPA)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('***')
print('SPA by SPA model')
stml = SpaML(inTrees, SPA)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)
 
print('**')
print('SR2008 by SR2008 model')
stml = SR2008ML(inTrees, SR2008)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)


print('SR2008 by SPA model')
stml = SpaML(inTrees, SR2008)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('total by SR2008 model')
stml = SR2008ML(inTrees, total)
ret = stml.optimizeBeta()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

print('total by SPA model')
stml = SpaML(inTrees, total)
ret = stml.optimizeQ()
ret1=stml.ch.propTree.logLike
print(ret, ret1)

