for x in range(100):
    os.chdir('/home/heather/REALTHING2/replicate%x/supertrees' %(x+1))
    os.system('pwd')
    os.system('ls')
    
