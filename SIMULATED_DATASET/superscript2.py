#!/Users/heathergrant/p4-phylogenetics/p4
#!/usr/bin/python

from subprocess import call

my_MRP_list=[]
my_Maj_R_list=[]
my_SR2008_list=[]
my_SPA_list=[]
my_QPA_list=[]
my_SPA_supp_list=[]
my_QPA_supp_list=[]

for x in range(100):
	os.chdir('/Users/heathergrant/MRes_project_supertrees/REALTHING2/replicate%i/supertrees' % (x+1))
	os.system('pwd')
	read('../results/*contree')
	inTrees = var.trees
	var.trees = []
	MRP=func.readAndPop('mrpStrictConsTree.nex')
	MajR=func.readAndPop('mrpMajRuleConsTree.nex')
	MajR.name='MajR'
	SR2008=func.readAndPop('SR2008_cons.nex')
	a=func.readAndPop('mrpStrictConsTree.nex')
	SR2008.name='SR2008'
	SR2008.taxNames=a.taxNames
	MRP.taxNames=a.taxNames
	SPA=func.readAndPop('SPA_cons.nex')
	SPA.taxNames=a.taxNames
	QPA=func.readAndPop('QPA_cons.nex')
	QPA.taxNames=a.taxNames
	SPA_support=func.readAndPop('SPA_supports_cons.nex')
	SPA_support.taxNames=a.taxNames
	QPA_support=func.readAndPop('QPA_supports_cons.nex')
	QPA_support.taxNames=a.taxNames
	trees=[MRP, MajR, SR2008, SPA, QPA, SPA_support, QPA_support]
	taxNames=list(string.uppercase[:10])
	tt=Trees(trees=trees, taxNames=taxNames)
	dd=tt.inputTreesToSuperTreeDistances(inTrees)
	my_MRP_list.append(dd[0][2])
	my_Maj_R_list.append(dd[1][2])
	my_SR2008_list.append(dd[2][2])
	my_SPA_list.append(dd[3][2])
	my_QPA_list.append(dd[4][2])
	my_SPA_supp_list.append(dd[5][2])
	my_QPA_supp_list.append(dd[6][2])
print(my_MRP_list)
print(my_Maj_R_list)
print(my_SR2008_list)
print(my_SPA_list)
print(my_QPA_list)
print(my_SPA_supp_list)
print(my_QPA_supp_list)
#for x in replicates:
#	os.system('mkdir ./replicate%i' % x)	

#for x in replicates:
#	os.chdir('/home/heather/REALTHING/replicate%i' % x)
	#os.system('cd ~/directorypractice/replicate%i' %(x+1))
#	call(["p4", "/home/heather/REALTHING/code/A_dirprac_make_data.py"])
	

#check distance between input trees and true tree
#for x in range(2):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i' % (x+1))
#	os.system('pwd')
#	call(["p4", "/Users/heathergrant/directorypractice/code/B_input_trees_distances.py"])
	

#make mr.nex for each replicate folder. 
#for x in range(2):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i' % (x+1))
#	os.system('mkdir supertrees')
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i/supertrees' % (x+1))
#	call(["p4", "/Users/heathergrant/directorypractice/code/C_sMakeMR.py"])

#make MRP for each folder 
#for x in range(2):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i/supertrees' % (x+1))
#	call(["paup", "/Users/heathergrant/directorypractice/code/paupme.nex"])

#next... make SPA for all replicates 

#for x in range (2):
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i' % (x+1))
#	os.system('mkdir ./SPA_gubbins')
#	os.chdir('/Users/heathergrant/directorypractice/replicate%i/SPA_gubbins' %(x+1))
#	call(["p4", "/Users/heathergrant/directorypractice/code/E_SPA.py"])
#	
#
		
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

