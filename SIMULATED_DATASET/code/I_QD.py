## This script gives the distance matrix between supertree method outputs. 
import p4.scqdist 

#read an alignment for taxNames                                                              
a=func.readAndPop('../results/gene1.phy')      
                                                                                                  
#match master tree and reconstructed tree for calculating their distances                                                                                                                                                                                
TRUE_tree= func.readAndPop('../results/gene.true')                                                  
TRUE_tree.name = 'True_tree' 

MRP = func.readAndPop('mrpStrictConsTree.nex')
MRP.name='MRP'

MajR = func.readAndPop('mrpMajRuleConsTree.nex')
MajR.name='MajR'

SR2008 = func.readAndPop('SR2008_cons.nex')
SR2008.name='SR2008'

SPA=func.readAndPop('SPA_cons.nex')
SPA.name='SPA'

QPA= func.readAndPop('QPA_cons.nex')
QPA.name='QPA'

QPA_split_support = func.readAndPop('QPA_supports_cons.nex')
QPA_split_support.name='QPA_supports'

SPA_split_support = func.readAndPop('SPA_supports_cons.nex')
SPA_split_support.name='SPA_supports'

mytreelist= [TRUE_tree, MRP, MajR, SR2008, SPA, QPA, SPA_split_support, QPA_split_support]
tt = Trees(mytreelist, taxNames=a.taxNames)

dm = tt.topologyDistanceMatrix('scqdist')
#dm.writeNexus()
dm.writeNexus(fName="distancematix.nex")

#rf_dist = (truetree.topologyDistance(mrp, metric='sd'))
#print("RF distance from true tree to mrp is %i" % rf_dist)

#rf_dist_2 = (spa.topologyDistance(qpa, metric='sd'))
#print("RF distance spa to qpa is %i" %rf_dist_2)

