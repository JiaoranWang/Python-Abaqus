import os
import sys
from datetime import datetime
import pathlib
### Print the current dic ###

base_dir1 = os.path.dirname(__file__)
base_dir2 = os.getcwd()
print(base_dir1)
print(base_dir2)
sys.path.append('../../Exe_Scripts') #回到上层目录
# base_dir3 = pathlib.path.parent()
# print(base_dir3)
# os.path.dirname   =>   /xx/xx，os.getcwd()    =>  \xx\xx，
import os
print ('***获取当前目录文件***')
print("abs path is %s" %(os.path.abspath(sys.argv[0])))
print(os.path.basename(sys.argv[0]))  # 当前文件名名称
print(os.path.basename(__file__))  # 当前文件名名称
print ('***获取当前目录***')
# print os.getcwd()
print (os.path.abspath(os.path.dirname(__file__)))

print ('***获取上级目录***')
print (os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print (os.path.abspath(os.path.dirname(os.getcwd())))
print (os.path.abspath(os.path.join(os.getcwd(), "..")))

print ('***获取上上级目录***')
print (os.path.abspath(os.path.join(os.getcwd(), "../..")))

# C:\Users\jiaor\PycharmProjects\pythonProject_HP\[Python-Abaqus API Project]\Python-Abaqus API\Exe_Scripts\Test

# whether the path exists
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        print("---  创建新的文件夹... ")
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  OK  ---")
        print(path)
    else:
        print("---  文件夹已存在!  ---")
        print(path)
base_dir2 = base_dir2
mkdir(base_dir2)
# Obtaining the parent directory
# for the result folder name
import sys
print("abs path is %s" %(os.path.abspath(sys.argv[0])))
print(sys.argv[0])
print(sys.argv) # 输入参数列表
print(sys.argv[0])  # 第0个就是这个python文件本身的路径（全路径）

a = os.path.basename(sys.argv[0])
a = a[:-3]
print(a)

time1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time2 = datetime.now().strftime("%Y%m%d%H%M")
print(time1,time2)


folder = os.path.abspath(os.path.join(os.getcwd(), "../.."))+'\\Results\\'+'Test_'+time2+'_'+a
mkdir(folder)
print(folder)
# find the direct result directionary

### [Abaqus] Change/set the work dictionary and results ###
import os
import sys
from datetime import datetime
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


import subprocess
import sys
import time
# p = subprocess.Popen(["cmd", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE)
# p1 = p.communicate("Python --version\n")
# # p1 = subprocess.Popen(["cmd", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE)
# # p1.communicate('argument 1')
# # p1.communicate('argument 2')

p = subprocess.Popen(["test_2.py", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE)
