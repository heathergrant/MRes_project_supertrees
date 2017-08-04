
myCalc='fastReducedRF'
read('./results/*treefile')



stm = STMcmc(var.trees, modelName='SPA', spaQ=0.5, beta=1.2, stRFCalc=myCalc, runNum=0, sampleInterval=20, checkPointInterval=10000)

stm.tunings.nni=1.0
stm.tunings.spr=1.0
stm.tunings.chainTemp = 2.0


stm.run(20000)
stm.run(20000)

