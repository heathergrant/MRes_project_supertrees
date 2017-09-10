#!/Users/heathergrant/p4-phylogenetics/p4
#!/usr/bin/python

from subprocess import call

#alias parent= '/Users/heathergrant/directorypractice'
#parent=os.getcwd()


#make 100 sets of 100 input trees 
#for x in range(100):
#	os.system('mkdir ./replicate%i' %(x+ 1))	

for x in range(100):	
	os.chdir('/Users/heathergrant/MRes_project_supertrees/REALTHING2/replicate%i/supertrees' % (x+1))
#	os.system('cd ~/directorypractice/replicate%i' %(x+1))
	call(["paup", "/Users/heathergrant/MRes_project_supertrees/REALTHING2/code/paup_nj_trees.nex"])
	#call(["p4", "/Users/heathergrant/MRes_project_supertrees/REALTHING2/code/I_QD.py"])
        #os.system('pwd')
        #os.system('ls')

#check distance between input trees and true tree
#for x in range(100):
#	os.chdir('/home/heather/REALTHING2/replicate%i/QPA_gubbins' % (x+1))
#	os.system('pwd')
#	call(["p4", "/home/heather/sReadSTMcmcCheckPoints.py"])
	

#make mr.nex for each replicate folder. 
#for x in range(100):
#	os.chdir('/home/heather/REALTHING/replicate%i' % (x+1))
#	os.system('mkdir supertrees')
#	os.chdir('/home/heather/REALTHING/replicate%i/supertrees' % (x+1))
#	call(["p4", "/home/heather/REALTHING/code/C_sMakeMR.py"])

#make MRP for each folder 
#for x in range(100):
#	os.chdir('/home/heather/REALTHING/replicate%i/supertrees' % (x+1))
#	call(["paup", "/home/heather/REALTHING/code/paupme.nex"])

#next... make SPA for all replicates 

#for x in range (100):
#	os.chdir('/home/heather/REALTHING/replicate%i' % (x+1))
#	os.chdir('/home/heather/REALTHING/replicate%i/SPA_gubbins' %(x+1))
#	os.system('rm mcmc*')
#	call(["p4", "/home/heather/REALTHING/code/E_SPA.py"])
#	
#	
#for x in range (100):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i' % (x+1))
#	os.system('mkdir ./QPA_gubbins')
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i/QPA_gubbins' %(x+1))
#	call(["p4", "/Users/heathergrant/directorypractice/code/F_QPA.py"])
	
#sr2008 autotune doesn't work 
##Think about it  

#for x in range (2):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i' % (x+1))
#	os.system('mkdir ./SPA_use_support_gubbins')
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i/SPA_use_support_gubbins' %(x+1))
#	call(["p4", "/Users/heathergrant/directorypractice/code/G_SPA_with_support.py"])
	

#for x in range (2):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i' % (x+1))
#	os.system('mkdir ./QPA_use_support_gubbins')
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i/QPA_use_support_gubbins' %(x+1))
#	call(["p4", "/Users/heathergrant/directorypractice/code/H_QPA_with_support.py"])

#so let's do the distance matrix 

#os.system('mkdir distance_matricies')

#for x in range (2):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i' % (x+1))
#	call(["p4", "/Users/heathergrant/directorypractice/code/I_Distance_matrix.py"])
#	os.system('cp distancematrix.nex /Users/heathergrant/directorypractice/distance_matricies')

