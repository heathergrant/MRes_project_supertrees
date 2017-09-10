## This script gives the distance matrix between supertree method outputs. 
import p4.scqdist 

#read an alignment for taxNames                                                              
a=func.readAndPop('./results/gene1.phy')      
                                                                                                  
#match master tree and reconstructed tree for calculating their distances                                                                                                                                                                                
truetree= func.readAndPop('./results/gene.true')                                                  
truetree.name = 'true_tree' 
mrp = func.readAndPop('./supertrees/mrpStrictConsTree.nex') 
mrp.name='mrp'

#sr2008 = func.readAndPop('./supertrees/SR2008Cons.nex')
#sr2008.name='sr2008'

spa=func.readAndPop('./supertrees/SPA_cons.nex')
spa.name='spa'

qpa= func.readAndPop('./supertrees/QPA_cons.nex')
qpa.name='qpa'

qpa_support = func.readAndPop('./supertrees/QPA_use_support_cons.nex')
qpa_support.name='qpa_support'

spa_support = func.readAndPop('./supertrees/SPA_use_support_cons.nex')

mytreelist= [truetree, mrp, spa, qpa, spa_support, qpa_support]
tt = Trees(mytreelist, taxNames=a.taxNames)

dm = tt.topologyDistanceMatrix('scqdist')
#dm.writeNexus()
dm.writeNexus(fName="qd_distancematix.nex")

#rf_dist = (truetree.topologyDistance(mrp, metric='sd'))
#print("RF distance from true tree to mrp is %i" % rf_dist)

#rf_dist_2 = (spa.topologyDistance(qpa, metric='sd'))
#print("RF distance spa to qpa is %i" %rf_dist_2)

