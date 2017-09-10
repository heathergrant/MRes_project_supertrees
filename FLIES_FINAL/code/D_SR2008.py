func.splash2()
read('../inTrees_drosophila.phy')
rNum = 0
myCalc='fastReducedRF'

# Set up an STMcmc, with defaul sample interval and (by default) no checkpoints
stm = STMcmc(var.trees, stRFCalc=myCalc, modelName='SR2008_rf_aZ_fb', nChains=4, runNum=rNum)
stm.prob.nni = 1.0
#stm.prob.spr = 1.0
#stm.prob.polytomy = 0.5
stm.prob.spaQ_uniform = 0.2
stm.tunings.chainTemp = 1.2
#print(stm.tunings)

## do a pre-run, then remove the output files and reset gen num
stm.run(5000)
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
#stm.run(nGens)

#### make cons tree
 
