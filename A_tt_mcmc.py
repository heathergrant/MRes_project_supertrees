var.verboseRead = 0
var.warnReadNoFile = 0 #warnings off

nTax = int(var.argvAfterDoubleDash[0]) #when reading file put -- and tax no.
nTrees = int(var.argvAfterDoubleDash[1]) #second number after --is number trees
length =int(var.argvAfterDoubleDash[2]) #third number is length of alignment
                 
taxNames= list(string.uppercase[:nTax]) #give taxa names A-Z
t=func.randomTree(taxNames=taxNames, nTax=nTax, randomBrLens=1)#draw a random tree 
t.draw()
             
#create an alignment for tree t
a=func.newEmptyAlignment(dataType='dna', taxNames=t.taxNames, length =length)
t.data = Data([a]) #match tree t with data a 
t.newComp(spec='equal')#equal composition of bases?
t.newRMatrix()#create new rate matrix
t.setPInvar()#set pinv
t.setNGammaCat()
t.simulate()
#set model and simulate data

#use mcmc chain to generate related trees
m= Mcmc(t, nChains=1, runNum=0, sampleInterval=1, checkPointInterval=1, simulate=None, verbose=True)
m.run(1) #starts running, number of generations is 1
# Find the 'local' proposal; give it a name.
for p in m.proposals:
    if p.name == 'local':
        break

tList = []
for i in range(nTrees):
    m.chains[0].proposeLocal(p)
    #m.chains[0].propTree.draw()
    t = m.chains[0].propTree.dupe() #t is still our starting point
    t.model = None #might want to change this?? 
    t.data = None
    t.logLike = None
    t.recipWeight = 1
    tList.append(t)
    
tt = Trees(trees=tList)
tt.writeNexus('tt_mcmc.nex', withTranslation=1)


