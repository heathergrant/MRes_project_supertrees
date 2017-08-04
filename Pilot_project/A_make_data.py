#This script makes a "true" tree and several corresponding "gene" trees
# so called gene trees made by various squashing regimes and reconstruction 


from __future__ import print_function
import glob, string, os, random
var.verboseRead = 0
var.warnReadNoFile = 0 
nTax = int(var.argvAfterDoubleDash[0]) #when reading file put -- and tax no.                
taxNames= list(string.uppercase[:nTax]) #give taxa names A-Z

myP=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] #my squash values 
myComp= [0.4, 0.16, 0.2] #HIV COMP FROM ANDERSON ET AL. 2001
myRVals = [1.463523, 2.50155, 0.4082, 0.60375, 3.2494124, 0.5522] #HIV R CALCULATED FROM Q FROM ANDERSON ET AL. 2001

t=func.randomTree(taxNames=taxNames, nTax=nTax, randomBrLens=1)
os.system('mkdir ./results')
fileroot = './results/gene'
a=func.newEmptyAlignment(dataType='dna', taxNames=t.taxNames, length = 2000)
t.data = Data([a]) #match tree t with data a 
t.writeNewick(fileroot +'.true')
t.newComp(spec='specified', val= myComp) #specify the composition HIV 
t.newRMatrix(spec='specified', val = myRVals) # specify R matrix 
t.setNGammaCat(nGammaCat=4)
t.newGdasrv(free=0, val=0.5)
t.setPInvar(free=0, val=0.0)
func.reseedCRandomizer(os.getpid())

for x in range(20):
    filename= fileroot +'%i' %x
    for n in t.iterInternalsNoRoot():
        if random.random() < 0.5:
            n.br.len *= random.choice(myP)
    t.writeNewick(filename)
    t.simulate()
    a.writePhylip(filename + '.phy' )

#make the iqtrees 
for myfile in glob.glob('./results/*.phy'):
    os.system('iqtree-omp -s %s -nt AUTO' %myfile)
