func.splash2()
read('../inTrees_drosophila.phy')
rNum = 1
myCalc='fastReducedRF'

#os.chdir('/home/heather/BRYO/QPA_gubbins')

# Set up an STMcmc, with defaul sample interval and (by default) no checkpoints
stm = STMcmc(var.trees, stRFCalc=myCalc, modelName='QPA', nChains=4, runNum=rNum)
stm.prob.nni = 1.0
#stm.prob.spr = 1.0
#stm.prob.polytomy = 0.5
stm.prob.spaQ_uniform = 0.2
stm.tunings.chainTemp = 1.5
print(stm.tunings)

# do a pre-run, then remove the output files and reset gen num
stm.run(2000)
os.system("rm mcmc_likes_%i" % rNum)
os.system("rm mcmc_prams_%i" % rNum)
os.system("rm mcmc_trees_%i.nex" % rNum)
stm.gen = -1

stm.autoTune()

# Now the real thing
nGens = 10000000
stm.sampleInterval = nGens/1000
stm.checkPointInterval = nGens/1
stm.run(nGens)

#### make cons trees
#tp = TreePartitions("mcmc_trees_0.nex", skip=500)
#tp.read("mcmc_trees_0.nex", skip=500)
#t = tp.consensus(minimumProportion=0.5)
#for n in t.iterInternalsNoRoot():
#    n.name = "%.0f" % (100. * n.br.support)
#t.draw()
#t.name = 'stMcmc'
#t.writeNexus('QPA_cons.nex')

#os.system('cp QPA_cons.nex ../supertrees') 

