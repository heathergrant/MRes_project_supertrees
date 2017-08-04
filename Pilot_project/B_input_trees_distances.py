##Question: How much variation is there in the input trees? 

import p4.scqdist 

#read an alignment for taxNames' sake                                                                                                       
a=func.readAndPop('./results/gene0.phy')                                                                            

rf_list=[]
wrf_list=[]
bld_list=[]
qd_list =[]
        
truetree = func.readAndPop('./results/gene.true')
truetree.taxNames= a.taxNames                                                                                                                                        

#match true tree with each replicate in turn to find various distances                                                                    
for myfile in glob.glob('./results/*treefile'):                                                                                                                                                                            
        t1=func.readAndPop(myfile)                                                                                                                                                                                                  
        t1.taxNames = a.taxNames                                                                                                                
        rf_list.append(t1.topologyDistance(truetree,metric='sd'))                                                                                  
        wrf_list.append(t1.topologyDistance(truetree, metric='wrf'))                                                                               
        bld_list.append(t1.topologyDistance(truetree, metric='bld'))                                                                                    
        qd_list.append(t1.topologyDistance(truetree, metric='scqdist'))
                                                             
n=Numbers(rf_list)
n.binSize=2.0                                    
print("The RF distribution for in my input trees")
n.histo()
qd=Numbers(qd_list)
print("The QD distribution for my input trees")
qd.histo()

    #m=Numbers(my_qd_list)
    #m.binSize=1.0
    #print("The QD distribution for squash category %i" % int(100*p))
    #m.histo()

