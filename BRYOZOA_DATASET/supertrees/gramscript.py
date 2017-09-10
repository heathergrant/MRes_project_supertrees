from gram import TreeGram
from gram import TreeGramRadial

#read('mrpMajRuleConsTree.nex')
#read('QPA_1_minprop50cons.nex')
read('Bryo_tree_tree')
t=var.trees[0]
#t.reRoot(t.node('Pectinatella_magnifica', 'Fredericella_sultana'))
#t.reRoot(62)
tg = TreeGram(t)
tg.font='palatino'
#tg = TreeGramRadial(t, equalDaylight=False)
tg.setScaleBar(xOffset=3)
tg.baseName = 'Bryo_tree_tree'

tg.pdf()
