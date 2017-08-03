#A distribution of RF, WRF, QD distances from the master tree and reconstructed tree are printed for each squash value.                                                             
import p4.scqdist 
myP=[0.2, 0.4, 0.6, 0.8, 1.0] #my squash values


for p in myP:
    #read an alignment for taxNames' sake                                                                                                       
    a=func.readAndPop('./results%i/treereplicate00.phy' %int(100*p))                                                                            
    my_rf_list=[]
    my_wrf_list=[]
    my_bld_list=[]
    my_qd_list =[]
                                                                                                                                                
    #match master tree and reconstructed tree for calculating their distances                                                                   
    for rnum in range(100):                                                                                                                     
        fname1='./results%i/treereplicate%ssquashed' % (int(100*p), string.zfill(rnum,2))                                                       
        t1=func.readAndPop(fname1)                                                                                                           
        fname2= './results%i/treereplicate%s.phy.treefile'% (int(100*p),  string.zfill(rnum,2))                                                 
        t2=func.readAndPop(fname2)                                                                                                            
        t1.taxNames = a.taxNames                                                                                                                
        t2.taxNames = a.taxNames                                                                                                                
        my_rf_list.append(t1.topologyDistance(t2,metric='sd'))                                                                                  
        my_wrf_list.append(t1.topologyDistance(t2, metric='wrf'))                                                                               
        my_bld_list.append(t1.topologyDistance(t2, metric='bld'))                                                                                    
        my_qd_list.append(t1.topologyDistance(t2, metric='scqdist'))
                                                             
    n=Numbers(my_rf_list)
    n.binSize=1.0                                    
    print("The RF distribution for squash category %i" % int(100*p))
    n.histo()
    #m=Numbers(my_qd_list)
    #m.binSize=1.0
    #print("The QD distribution for squash category %i" % int(100*p))
    #m.histo()

