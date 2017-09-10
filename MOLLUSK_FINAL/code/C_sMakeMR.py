from p4.mrp import mrp

read('in_molluscs')
a = mrp(var.trees)
a.writeNexus('mr.nex')
