
from subprocess import call 

for x in range(100):
    os.chdir('/home/heather/REALTHING2/replicate%i/supertrees' % (x+1))
    call(["paup", "/home/heather/REALTHING2/code/paup_this_both.nex"])

