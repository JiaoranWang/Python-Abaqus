'''###  Open Abaqus Command window then Run Python Script ###'''

'''
@Tutorial Please refer to:
https://abapy.readthedocs.io/en/latest/tutorial.html
'''

import subprocess
import sys
import time
import os


get_input = input("Please input: Start the CAE with scripts? Y/N: ")
if get_input.strip().upper() == "Y":
    ## Please also set which execute script you want to run(e.g. (default) Exe_1.py)
    exe_script = input("Please input: which execute script? (e.g. Exe_1.py): ")
    ## rewrite the runcae.bat with input execute script:
    with open("runcae.bat", "rt") as bat_file:
        text = bat_file.readlines()
    new_text = []
    for line in text:
        if "abaqus cae script=" in line:
            # Slicing then replacing the string:
            a = line.find('=')
            b = line[a + 1:]
            new_text.append(line.replace(b, exe_script))
        else:
            new_text.append(line)
    with open("runcae.bat", "wt") as bat_file:
        for line in new_text:
            bat_file.write(line)
    ## Start to open and run the execute scripts in Abaqus_Command.lnk
    p = subprocess.Popen(["Abaqus_Command.lnk", "start runcae.bat"], shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    print('--- CMD->.bat opened! sleep 10 second... ---')
    output = p.stdout.readline()
    print('output = ', output)

    # p.wait() # wait for the process to finish
    # p.communicate("cd C:\sa") # input
    time.sleep(10)  # wait for 10 seconds
    print('--- CMD process END ---')
    sys.exit(0)  # exit
else:
    # do not need to be trouble go directly to run.bat
    p = subprocess.Popen(["cmd", "/k", "start run.bat"], shell=True,
                         stdout=subprocess.PIPE)  # do not need to be trouble go directly to run.bat
