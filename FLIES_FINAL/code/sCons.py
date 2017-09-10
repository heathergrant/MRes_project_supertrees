
tp = TreePartitions("mcmc_trees_0.nex", skip=50)
tp.read("mcmc_trees_0.nex", skip=50)
t = tp.consensus(minimumProportion=0.0)
for n in t.iterInternalsNoRoot():
    n.name = "%.0f" % (100. * n.br.support)
t.draw()
t.name = 'SPA'
t.writeNexus('SPA_0_minprop0cons.nex')

os.system('cp SPA_0_minprop0cons.nex ../supertrees') 

