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
SR2008.taxNames=a.taxNames
trees=[MRP,MajR, SR2008, QPA,SPA]


tt=Trees(trees=trees, taxNames=a.taxNames)
tt.inputTreesToSuperTreeDistances(inTrees)

dm = tt.topologyDistanceMatrix('scqdist')
dm.writeNexus()
dm.writeNexus('qd_distances.nex')
#paup execute rf_dist nj save


from p4.supertreesupport import SuperTreeSupport
print("%20s  %6s  %6s  %6s  %6s  %6s" % (' ', 'S', 'P', 'Q', 'R', 'V'))
for st in trees:
    
    sts = SuperTreeSupport(st, inTrees)
    
    sts.doSaveDecoratedTree = False
    sts.decoratedFilename='mytree.nex'
    sts.doSaveIndexTree=False
    sts.indexFilename='mytreeIndex.nex'
    sts.csvFilename='mytreeIndex.csv'
    sts.doDrawTree=False
    sts.verbose=0
    
    sts.superTreeSupport()
    print("%20s  %6.2f  %6.2f  %6.2f  %6.2f  %6.2f" % (st.name, sts.S, sts.P, sts.Q, sts.R, sts.V))
    






