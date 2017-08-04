
myCalc='fastReducedRF'
read('./results/*treefile')

stm = STMcmc(var.trees, modelName='SR2008_rf_aZ', beta=1.2, stRFCalc=myCalc, runNum=0, sampleInterval=20, checkPointInterval=10000, nChains=4)
stm.run(20000)
stm = STMcmc(var.trees, modelName='SR2008_rf_aZ', beta=1.2, stRFCalc=myCalc, runNum=1, sampleInterval=20, checkPointInterval=10000, nChain=4)
stm.run(20000)

