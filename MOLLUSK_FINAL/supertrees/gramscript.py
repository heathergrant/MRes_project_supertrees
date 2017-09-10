from gram import TreeGram
from gram import TreeGramRadial

#read('mrpMajRuleConsTree.nex')
#read('QPA_1_minprop50cons.nex')
read('qd_molls_st')
t=var.trees[0]
#t.reRoot(t.node('out'))
tg = TreeGramRadial(t, equalDaylight=False)
tg.font='palatino'
#tg = TreeGramRadial(t, equalDaylight=False)
tg.setScaleBar(yOffset=-3)
tg.baseName = 'molls_st_tree_qd'

tg.pdf()
