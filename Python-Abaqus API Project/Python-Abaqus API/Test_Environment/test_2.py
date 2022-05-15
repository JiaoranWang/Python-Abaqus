import subprocess
import sys
import time
# p = subprocess.Popen(["cmd", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE)
# p1 = p.communicate("Python --version\n")
# # p1 = subprocess.Popen(["cmd", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE)
# # p1.communicate('argument 1')
# # p1.communicate('argument 2')

p = subprocess.Popen(["test_2.py", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE)