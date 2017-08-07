## This script gives the distance matrix between supertree method outputs. 
import p4.scqdist 

#read an alignment for taxNames                                                              
a=func.readAndPop('./results/gene0.phy')      
                                                                                                  
#match master tree and reconstructed tree for calculating their distances                                                                                                                                                                                
truetree= func.readAndPop('./results/gene.true')                                                  
truetree.taxNames = a.taxNames                                                                                                                

mrp = func.readAndPop('mrpStrictConsTree.nex') 
mrp.taxNames = a.taxNames                                                                                                                

sr2008 = func.readAndPop('SR2008Cons.nex')
sr2008.taxNames=a.taxNames

spa=func.readAndPop('SPA_cons.nex')
spa.taxNames=a.taxNames

qpa= func.readAndPop('QPA_cons.nex')
qpa.taxNames=a.taxNames

var.trees.append(truetree)
var.trees.append(mrp)
var.trees.append(sr2008)
var.trees.append(spa)
var.trees.append(qpa) 
mytreelist= [truetree, mrp, sr2008, spa, qpa]
tt = Trees(mytreelist)

dm = tt.topologyDistanceMatrix('sd')
dm.writeNexus()

rf_dist = (truetree.topologyDistance(mrp, metric='sd'))
print("RF distance from true tree to mrp is %i" % rf_dist)

rf_dist_2 = (spa.topologyDistance(qpa, metric='sd'))
print("RF distance spa to qpa is %i" %rf_dist_2)

#for mystm in stmlist:
#
#	rf_dist = (truetree.topologyDistance(%s, metric='sd' % mystm))
#	qd_dist = (truetree.topologyDistance(%s, metric='scqdist' % mystm))
#
#	print("RF distance for %s is %i" %(mystm, rf_dist))
#	print("QD distance for %s is %i" % (mystm, qd_dist)
