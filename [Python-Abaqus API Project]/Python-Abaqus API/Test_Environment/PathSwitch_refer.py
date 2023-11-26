### [Abaqus] Change/set the work dictionary and results ###
import os
import sys
from datetime import datetime

class Students():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My name is %s and come from %s "%(name,city))
    def speak(self):
        print("我在慢慢学Python")

# Acquire the time
time = datetime.now().strftime("%Y%m%d%H%M")
# Script Name
name = os.path.basename(sys.argv[0])
name = name[:-3]
# change the work to folder
folder = os.path.abspath(os.path.join(os.getcwd(), ".."))+'\\Results\\'+'Test_'+time+'_'+name
#
def makedir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        print("---  Creating new folder... ---")
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print(path)
        print("---  OK  ---")
    else:
        print("---  Already Existed!  ---")
        print(path)

makedir(folder)
# change the work to folder
os.chdir(folder)


import os
import sys
from datetime import datetime




### [Abaqus] Change/set the work dictionary and results ###
# Acquire the time
time = datetime.now().strftime("%Y%m%d%H%M")
# Script Name
name = os.path.basename(sys.argv[0])
name = name[:-3]
# change the work to folder
folder = os.path.abspath(os.path.join(os.getcwd(), ".."))+'\\Results\\'+'Test_'+time+'_'+name
# make and change the work to folder
os.makedirs(folder)
os.chdir(folder)
# --------------------------#




# The following format can not be exacute in the CAE
def makedir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        print("---  Creating new folder... ---")
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print(path)
        print("---  OK  ---")
    else:
        print("---  Already Existed!  ---")
        print(path)

# makedir(folder)


