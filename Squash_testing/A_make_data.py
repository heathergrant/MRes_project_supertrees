#This script is designed to show how much "noise" can be generated by manipulating internal branch lengths
#For each "squash value", a hundred randomly generated trees are squashed (internal branch lengths reduced) 
#each random generated tree has an alignment simulated, which is reconstructed using iqtree

from __future__ import print_function
import glob, string, os 
var.verboseRead = 0
var.warnReadNoFile = 0 
nTax = int(var.argvAfterDoubleDash[0]) #when reading file put -- and tax no.                
taxNames= list(string.uppercase[:nTax]) #give taxa names A-Z

myP=[0.2, 0.4, 0.6, 0.8, 1.0] #my squash values 
myComp= [0.4, 0.16, 0.2] #HIV COMP FROM ANDERSON ET AL. 2001
myRVals = [1.463523, 2.50155, 0.4082, 0.60375, 3.2494124, 0.5522] #HIV R CALCULATED FROM Q FROM ANDERSON ET AL. 2001

for p in myP:
    os.system('mkdir ./results%i' %int(100*p))
    fileroot = './results%i/treereplicate' % int(100*p)
    for x in range(100):
        t=func.randomTree(taxNames=taxNames, nTax=nTax, randomBrLens=1)
        filename= fileroot +'%.2d' %x
        for n in t.iterInternalsNoRoot():
            n.br.len *= p
            t.writeNewick(filename + 'squashed')
        a=func.newEmptyAlignment(dataType='dna', taxNames=t.taxNames, length = 1000)
        t.data = Data([a]) #match tree t with data a 
        t.newComp(spec='specified', val= myComp) #specify the composition HIV 
        t.newRMatrix(spec='specified', val = myRVals) # specify R matrix 
        t.setNGammaCat(nGammaCat=4)
        t.newGdasrv(free=0, val=0.5)
        t.setPInvar(free=0, val=0.0)
        func.reseedCRandomizer(os.getpid())
        t.simulate()
        a.writePhylip(filename + '.phy')

    #make the iqtrees 
    for myfile in glob.glob('./results%i/*phy' %int(100*p)):
        os.system('iqtree-omp -s %s -nt AUTO' %myfile)
