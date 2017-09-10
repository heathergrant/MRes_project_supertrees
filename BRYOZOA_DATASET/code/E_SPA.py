
func.splash2()
read('../fix_input_trees/t*')
rNum = 0
myCalc='fastReducedRF'

#os.chdir('/home/heather/BRYO/SPA_gubbins')
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

stm.autoTune(carryOn=True)

# Now the real thing
nGens = 10000000
stm.sampleInterval = nGens/10000
stm.checkPointInterval = nGens/4
stm.run(nGens)
