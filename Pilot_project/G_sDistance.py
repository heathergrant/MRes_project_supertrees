## This script gives the distances from each STM and the "true tree" created at the beginning 


import p4.scqdist 

#read an alignment for taxNames' sake                                                              

a=func.readAndPop('./results/gene0.phy')                                                                                                        
#match master tree and reconstructed tree for calculating their distances                                                                                                                                                                                
truetree= func.readAndPop('./results/gene.true')                                                  
truetree.taxNames = a.taxNames                                                                                                                

mrptree = func.readAndPop('mrpStrictConsTree.nex') 
mrptree.taxNames = a.taxNames                                                                                                                

sr2008 = func.readAndPop('SR2008Cons.nex')
sr2008.taxNames=a.taxNames

spa=func.readAndPop('SPA_cons.nex')
spa.taxNames=a.taxNames

qpa= func.readAndPop('QPA_cons.nex')
qpa.taxNames=a.taxNames

mrp_rf = (truetree.topologyDistance(mrptree ,metric='sd'))
mrp_wrf =(truetree.topologyDistance(mrptree, metric='wrf'))   
mrp_bld =(truetree.topologyDistance(mrptree, metric='bld'))                                      
mrp_qd = (truetree.topologyDistance(mrptree, metric='scqdist'))

print("RF distance for MRP is %i" %mrp_rf)
print("WRF distance for MRP is %i" %mrp_wrf)
print("BLD distance for MRP is %i" %mrp_bld)
print("QD distance for MRP is %i" % mrp_qd)

sr2008_rf = (truetree.topologyDistance(sr2008 ,metric='sd'))
sr2008_wrf =(truetree.topologyDistance(sr2008, metric='wrf'))   
sr2008_bld =(truetree.topologyDistance(sr2008, metric='bld'))                                      
sr2008_qd = (truetree.topologyDistance(sr2008, metric='scqdist'))

print("RF distance for SR2008 is %i" %sr2008_rf)
print("WRF distance for SR2008 is %i" %sr2008_wrf)
print("BLD distance for SR2008 is %i" %sr2008_bld)
print("QD distance for SR2008 is %i" % sr2008_qd)


spa_rf = (truetree.topologyDistance(spa ,metric='sd'))
spa_wrf =(truetree.topologyDistance(spa, metric='wrf'))   
spa_bld =(truetree.topologyDistance(spa, metric='bld'))                                      
spa_qd = (truetree.topologyDistance(spa, metric='scqdist'))

print("RF distance for SPA is %i" %spa_rf)
print("WRF distance for SPA is %i" %spa_wrf)
print("BLD distance for SPA is %i" %spa_bld)
print("QD distance for SPA is %i" % spa_qd)


qpa_rf = (truetree.topologyDistance(qpa ,metric='sd'))
qpa_wrf =(truetree.topologyDistance(qpa, metric='wrf'))   
qpa_bld =(truetree.topologyDistance(qpa, metric='bld'))                                      
qpa_qd = (truetree.topologyDistance(qpa, metric='scqdist'))

print("RF distance for QPA is %i" %qpa_rf)
print("WRF distance for QPA is %i" %qpa_wrf)
print("BLD distance for QPA is %i" %qpa_bld)
print("QD distance for QPA is %i" % qpa_qd)