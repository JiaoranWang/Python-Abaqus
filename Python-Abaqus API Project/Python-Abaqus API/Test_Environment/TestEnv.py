
import subprocess
import sys
import time


get_input = input("Please input: Start the CAE with scripts? Y/N")

if get_input.strip().upper() == "Y":
    # do not need to be trouble go directly to run.bat
    p = subprocess.Popen(["Abaqus_Command.lnk","start runcae.bat"], shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print('--- CMD->.bat opened! sleep 10 second... ---')
    output = p.stdout.readline()
    print('output = ',output)

    # p.wait() # wait for the process to finish
    # p.communicate("cd C:\sa") # input
    time.sleep(10) # wait for 10 seconds
    print('--- CMD process END ---')
    sys.exit(0) # exit

else:
    p = subprocess.Popen(["cmd", "/k","start run.bat"], shell = True, stdout=subprocess.PIPE) # do not need to be trouble go directly to run.bat
