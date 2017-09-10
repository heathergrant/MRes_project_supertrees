from p4.mrp import mrp

read('./fix_input_trees/t*')
a = mrp(var.trees)
a.writeNexus('mr.nex')
