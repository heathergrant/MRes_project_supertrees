tp = TreePartitions("mcmc_trees_0.nex", skip=5000)
tp.read("mcmc_trees_0.nex", skip=5000)
t = tp.consensus(minimumProportion=0.5)
for n in t.iterInternalsNoRoot():
    n.name = "%.0f" % (100. * n.br.support)
t.draw()
t.name = 'QPA0'
t.writeNexus('QPA_cons0.nex')

os.system('cp QPA_cons0.nex ../supertrees') 

