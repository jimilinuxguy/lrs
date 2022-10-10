import os
for i in range(0,255):
    os.system("python2 lrs_pager.py "+str(i))  
    os.system("/usr/local/Cellar/python@3.10/3.10.7/bin/python3.10 top_block.py "+str(i))  
