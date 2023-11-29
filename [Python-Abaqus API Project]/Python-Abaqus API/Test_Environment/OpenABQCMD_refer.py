
''' --- ---'''

#Open CMD and direct to the Abaqus Command.Ink directory

# p = subprocess.Popen(["start", "cmd", "/k", "cd C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dassault Systemes SIMULIA Established Products 2021\Abaqus Command.Ink"], shell = True, stdout=subprocess.PIPE)
# p = subprocess.Popen(["start", "cmd", "/k", "cd C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dassault Systemes SIMULIA Established Products 2021"], shell = True, stdout=subprocess.PIPE)

# write the command into .bat for execute
## 去掉内部的 start 就可以只开一个窗口了
import subprocess
import sys
import time


get_input = input("Please input: Start the CAE with scripts? Y/N")

if get_input.strip().upper() == "Y":

    p = subprocess.Popen(["Abaqus_Command.lnk","start runcae.bat"], shell = True, stdout=subprocess.PIPE) # do not need to be trouble go directly to run.bat
    print('--- CMD->.bat opened! sleep 10 second... ---')
    # p.wait() # wait for the process to finish
    # p.communicate("cd C:\sa") # input
    time.sleep(10) # wait for 10 seconds
    print('--- CMD process END ---')
    sys.exit(0) # exit

else:
    p = subprocess.Popen(["cmd", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE) # do not need to be trouble go directly to run.bat


from subprocess import Popen, check_output, check_call, PIPE, call
# https://stackoverflow.com/questions/47179167/open-an-exe-file-and-give-it-input-parameters-in-python

get_input = input("What Should I do?")

if get_input.strip().lower() == "run":

    your_exe_file_address = r'"C:\Users\jiaor\PycharmProjects\pythonProject_HP\Python-Abaqus API Project\Python-Abaqus API\Test_Environment\Abaqus_Command.lnk"' # example
    # your_module_address = r'"C:\Users\you\Desktop\test.m"' # example
    your_command = "abaqus cae script=Exe_1.py"

    process = Popen([your_exe_file_address, your_command], stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()

    # < Other Ways >
    # process = check_output([your_exe_file_address, your_command, your_module_address])
    # process = check_call([your_exe_file_address, your_command, your_module_address], shell=True)
    # process = call([your_exe_file_address, your_command, your_module_address], stdout=PIPE, stderr=PIPE, shell=True)

    print(stdout, stderr)

else:
    print("Invalid Input")

# a = subprocess.Popen(["exit"], shell = True, stdout=subprocess.PIPE)
# a.wait()
# print('--- CMD exit! ---')
# result = p.stdout.read()
# print(result) # 进程返回值



#### Test for exe with input





from time import sleep

# os.chdir(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dassault Systemes SIMULIA Established Products 2021')
#
# os.system("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dassault Systemes SIMULIA Established Products 2021")
# os.system("AbaqusCommand.Ink")


# Python program to explain os.system() method

# importing os module
import os
#### os 给命令不显示也不弹出来 cmd 窗口
# Command to execute
# Using Windows OS command
# cmd = 'date'
# Using os.system() method
# os.system(cmd)
# sleep.()
# os.system('01-25-24')
# os.popen("C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Dassault Systemes SIMULIA Established Products 2021")

# os.system("start /wait cmd /c {command}") #闪退了

# os.system("start cmd /c {command here}")


# # p = subprocess.Popen(["start", "cmd", "/k", "date"], shell = True) # Needs to be shell since start isn't an executable, its a shell cmd
# p = subprocess.Popen(["start", "cmd", "/k", "cd C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Dassault Systemes SIMULIA Established Products 2021"], shell = True)
# Needs to be shell since start isn't an executable, its a shell cmd
# p.wait()    # I can wait until finished (although it too finishes after start finishes)




# import subprocess
# subprocess.Popen( 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Dassault Systemes SIMULIA Established Products 2021\\Abaqus Command.Ink')
# My computer's command is in the dict above

# Import system modules
# import os
# os.system("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Dassault Systemes SIMULIA Established Products 2021\\Abaqus Command.Ink")

# subprocess.Popen
# 可以处理命令的返回值、stdout、stderr。
#
# import subprocess
# p=subprocess.Popen(
# ‘ls .vim*’,# 待执行的命令
# shell=True,# 使用shell
# stderr=subprocess.PIPE,# 执行命令后的报错，送到pipe(默认打印到stderr)
# #可以通过p.stderr访问该pipe内容；
# stdout=subprocess.PIPE,# 执行命令后的输出，送到pipe(默认打印到stdout)
# #可以通过p.stdout访问该pipe内容
# )
#
# 建议使用communicate()等待子进程结束，不会死锁。
# print(p.returncode) # None，表示子进程还未结束
# b_stdout, b_stderr = p.communicate() # 等待子进程结束，返回bytes
# print(p.returncode) # 0，表示子进程正常退出
#
#
# for s_line in b_stdout.decode().strip().split(‘\n’)
# print(s_line)
#
# for s_line in b_stderr.decode().strip().split(‘\n’)
# print(s_line)
#
#
#
#
#
