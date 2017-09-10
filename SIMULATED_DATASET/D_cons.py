tp = TreePartitions("all_QD_distances")
tp.read("all_QD_distances")
t = tp.consensus(minimumProportion=0.0)
for n in t.iterInternalsNoRoot():
    n.name = "%.0f" % (100. * n.br.support)
t.draw()
t.name = 'SIM_SUPERTREE_0min'
t.writeNexus('SIM_SUPERTREE_QD_0min.nex')

os.system('cp SIM_SUPERTREE__QD_0min ../supertrees')
