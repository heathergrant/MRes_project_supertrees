
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
a=func.readAndPop('BRYO_NEW_SR2008_50cons.nex')
SPA.taxNames=a.taxNames
MRP_100.taxNames=a.taxNames
MRP_50.taxNames=a.taxNames
total_evidence=func.readAndPop('total_evidence_f')
total_evidence.name='total_evidence'
#total_evidence.taxNames=a.taxNames

trees=[total_evidence, MRP_100, MRP_50, SR2008,SPA]

tt=Trees(trees=trees, taxNames=a.taxNames)
tt.inputTreesToSuperTreeDistances(inTrees)

dm = tt.topologyDistanceMatrix('scqdist')
dm.writeNexus()
dm.writeNexus('qd_distances.nex')
#paup execute rf_dist nj save
dm2=tt.topologyDistanceMatrix('sd')
dm2.writeNexus()
dm2.writeNexus('rf_distances.nex')

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
    






