import string
#read in and set up 
read('results/*contree')
inTrees = var.trees

var.trees = []
MRP=func.readAndPop('supertrees/mrpStrictConsTree.nex')
MajR=func.readAndPop('supertrees/mrpMajRuleConsTree.nex')
SR2008=func.readAndPop('SR2008_cons.nex')
SR2008.name='SR2008'
#SPA=func.readAndPop('SPA_f.nex')
#SPA.name='SPA'
#SPA_support=func.readAndPop('SPA_supp_f.nex')
#SPA_support.name='SPA_support'
#MRP.name='MRP'
MajR.name='MajR'
a=func.readAndPop('supertrees/mrpStrictConsTree.nex')
#SPA.taxNames=a.taxNames
MRP.taxNames=a.taxNames
#inTrees.taxNames = list(string.uppercase[:10])
#MajR.taxNames=a.taxNames


#trees=[total_evidence, MRP,MajR, SR2008,SPA, SPA_support]
trees=[MRP, MajR]
taxNames=list(string.uppercase[:10])



#tt=Trees(trees=trees, taxNames=MRP.taxNames)
tt=Trees(trees=trees, taxNames=taxNames)
tt.inputTreesToSuperTreeDistances(inTrees)

#dm = tt.topologyDistanceMatrix('scqdist')
#dm.writeNexus()
#dm.writeNexus('qd_distances.nex')
#paup execute rf_dist nj save





