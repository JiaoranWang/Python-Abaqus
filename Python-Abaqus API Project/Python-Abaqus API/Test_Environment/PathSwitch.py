'''@ [Abaqus] Change/set the work dictionary and results

This part is to change the abaqus working directory to our desire folder
Folder name format: /Test_MMDDHHMM_XXXXXXX (.py scriptname)
example :Results/Test_202205142316_ABQcaeK

'''

import os
import sys
from datetime import datetime
# Acquire the time
time = datetime.now().strftime("%Y%m%d%H%M")
# Acquire Script Name
name = os.path.basename(sys.argv[0])
name = name[:-3]
# change the work to parent folder
folder = os.path.abspath(os.path.join(os.getcwd(), ".."))+'\\Results\\'+'Test_'+time+'_'+name
# change the work to grandparent folder
folder = os.path.abspath(os.path.join(os.getcwd(), "../.."))+'\\Results\\'+'Test_'+time+'_'+name
# make and change the work to folder
os.makedirs(folder)
os.chdir(folder)
# --------------------------#



