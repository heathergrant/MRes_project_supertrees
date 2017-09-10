
tp = TreePartitions("mcmc_trees_1.nex", skip=5000000)
tp.read("mcmc_trees_1.nex", skip=5000000)
t = tp.consensus(minimumProportion=0.5)
for n in t.iterInternalsNoRoot():
    n.name = "%.0f" % (100. * n.br.support)
t.draw()
t.name = 'Mollusc_SPA1'
t.writeNexus('SPA_cons1.nex')

os.system('cp SPA_cons1.nex ../supertrees') 

