func.splash2()
read('../in_molluscs')
rNum = 0
myCalc='fastReducedRF'

# Set up an STMcmc, with defaul sample interval and (by default) no checkpoints
stm = STMcmc(var.trees, stRFCalc=myCalc,  modelName='SPA', nChains=4, runNum=rNum)
stm.prob.nni = 1.0
#stm.prob.spr = 1.0
#stm.prob.polytomy = 0.5
stm.prob.spaQ_uniform = 0.2
stm.tunings.chainTemp = 2.5
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
stm.sampleInterval = nGens/10000
stm.checkPointInterval = nGens/4
stm.run(nGens)

#### make cons tree

#tp = TreePartitions("mcmc_trees_0.nex", skip=500)
#tp.read("mcmc_trees_0.nex", skip=500)
#t = tp.consensus(minimumProportion=0.5)
#for n in t.iterInternalsNoRoot():
#    n.name = "%.0f" % (100. * n.br.support)
#t.draw()
#t.name = 'stMcmc'
#t.writeNexus('SPA_cons.nex')

#os.system('cp SPA_cons.nex ../supertrees') 

