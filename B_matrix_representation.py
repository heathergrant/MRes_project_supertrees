#create matrix representation of input trees and output mr.nex
from p4.mrp import mrp
read('tt_mcmc.nex')
a = mrp(var.trees)
a.writeNexus('mr.nex')
#in order to convert the splits a BACK into a set of trees
#from p4.mrp import reverseMrp
#a = func.readAndPop('mr.nex')
#a.setNexusSets()
#tt = reverseMrp(a)
#for t in tt:
  #  t.write()

