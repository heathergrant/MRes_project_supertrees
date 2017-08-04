os.system("rm -f mcmc*")

myCalc='fastReducedRF'
read('./results/*treefile')

stm = STMcmc(var.trees, modelName='QPA', spaQ=0.5, beta=1.2, stRFCalc=myCalc, runNum=0, sampleInterval=20, checkPointInterval=10000, useSplitSupport=False, verbose=True, nChains=4)
#stm.spaQ=True

stm.tunings.nni=1.0
stm.tunings.spr=1.0
stm.tunings.chainTemp = 2.0

stm.run(20000)

#options
#STMcmc(inTrees, bigT=None, modelName='SR2008_rf_aZ', beta=1.0, spaQ=0.5, stRFCalc='purePython1', nChains=1, runNum=0, sampleInterval=100, checkPointInterval=None, useSplitSupport=False, verbose=True, checkForOutputFiles=True)
