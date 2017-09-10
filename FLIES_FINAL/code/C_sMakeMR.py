from p4.mrp import mrp

read('inTrees_drosophila.phy')
a = mrp(var.trees)
a.writeNexus('mr.nex')
