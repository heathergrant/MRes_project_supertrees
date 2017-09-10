from p4.mrp import mrp

read('../results/*contree')
a = mrp(var.trees)
a.writeNexus('mr.nex')
