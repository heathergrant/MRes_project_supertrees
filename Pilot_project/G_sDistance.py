## This script gives the distance matrix between supertree method outputs. 
import p4.scqdist 

#read an alignment for taxNames                                                              
a=func.readAndPop('./results/gene0.phy')      
                                                                                                  
#match master tree and reconstructed tree for calculating their distances                                                                                                                                                                                
truetree= func.readAndPop('./results/gene.true')                                                  
truetree.name = 'true_tree' 
mrp = func.readAndPop('mrpStrictConsTree.nex') 
mrp.name='mrp'

sr2008 = func.readAndPop('SR2008Cons.nex')
sr2008.name='sr2008'

spa=func.readAndPop('SPA_cons.nex')
spa.name='spa'

qpa= func.readAndPop('QPA_cons.nex')
qpa.name='qpa'

var.trees.append(truetree)
var.trees.append(mrp)
var.trees.append(sr2008)
var.trees.append(spa)
var.trees.append(qpa) 
mytreelist= [truetree, mrp, sr2008, spa, qpa]
tt = Trees(mytreelist, taxNames=a.taxNames)


dm = tt.topologyDistanceMatrix('sd')
dm.writeNexus()
#dm.writeNexus(fName="distancematic.nex")

#rf_dist = (truetree.topologyDistance(mrp, metric='sd'))
#print("RF distance from true tree to mrp is %i" % rf_dist)

#rf_dist_2 = (spa.topologyDistance(qpa, metric='sd'))
#print("RF distance spa to qpa is %i" %rf_dist_2)

