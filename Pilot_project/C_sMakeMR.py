from p4.mrp import mrp
read('./results/*treefile')
a = mrp(var.trees)
a.writeNexus('mr.nex')
