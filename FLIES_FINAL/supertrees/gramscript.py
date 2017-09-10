from gram import TreeGram
from gram import TreeGramRadial


read('qd_distance_stm_tree')
t=var.trees[0]
#t.reRoot(t.node('out'))
tg=TreeGramRadial(t, equalDaylight=False)

tg.font='palatino'
tg.setScaleBar(xOffset=2, yOffset=-1)
tg.baseName = 'flies_tree_of_supertree_qd'

tg.pdf()

'''
read('mrpMajRuleConsTree.nex')
t=var.trees[0]
t.reRoot(t.node('out'))
tg=TreeGram(t)
#tg = TreeGramRadial(t, equalDaylight=False)
tg.font='palatino'
#tg = TreeGramRadial(t, equalDaylight=False)
#tg.setScaleBar()
tg.baseName = 'flies_majR'

tg.pdf()

read('SR2008_1_minprop50cons.nex')
t=var.trees[0]
t.reRoot(t.node('out'))
tg=TreeGram(t)
#tg = TreeGramRadial(t, equalDaylight=False)
tg.font='palatino'
#tg = TreeGramRadial(t, equalDaylight=False)
#tg.setScaleBar()
tg.baseName = 'flies_SR2008'

tg.pdf()
'''
