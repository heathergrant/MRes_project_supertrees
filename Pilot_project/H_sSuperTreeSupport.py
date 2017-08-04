#this script does supertree support between each STM and the input trees 


from p4.supertreesupport import SuperTreeSupport

#mrptree = func.readAndPop('mrpStrictConsTree.nex') 
#sr2008 = func.readAndPop('SR2008Cons.nex')
#spa=func.readAndPop('SPA_cons.nex')
#qpa=func.readAndPop('QPA_cons.nex')

sts = SuperTreeSupport('mrpStrictConsTree.nex', './results/*treefile')
#sts.doSaveDecoratedTree = False
#sts.decoratedFilename='mytree.nex'
sts.verbose=3
sts.doDrawTree=True
print("MRP SUPPORT")
sts.superTreeSupport()

sts_spa = SuperTreeSupport('SPA_cons.nex', './results/*treefile')
sts_spa.verbose=3
sts_spa.doDrawTree=True
print("SPA SUPPORT")
sts_spa.superTreeSupport()

sts_qpa = SuperTreeSupport('QPA_cons.nex', './results/*treefile')
sts_qpa.verbose=3
sts_qpa.doDrawTree=True
print("QPA SUPPORT")
sts_qpa.superTreeSupport()

sts_sr2008 = SuperTreeSupport('SR2008Cons.nex', './results/*treefile')
print("SR2008 SUPPORT")
sts.verbose=3
sts_sr2008.doDrawTree=True
sts_sr2008.superTreeSupport()


