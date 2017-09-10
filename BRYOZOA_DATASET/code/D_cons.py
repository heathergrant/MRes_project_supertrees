tp = TreePartitions("mcmc_trees_1.nex", skip=5000)
tp.read("mcmc_trees_1.nex", skip=5000)
t = tp.consensus(minimumProportion=0.5)
for n in t.iterInternalsNoRoot():
    n.name = "%.0f" % (100. * n.br.support)
t.draw()
t.name = 'SR2008_NEW_BRYO'
t.writeNexus('BRYO_NEW_SR2008_50cons.nex')

os.system('cp BRYO_NEW_SR2008_50cons.nex ../supertrees') 

