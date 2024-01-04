'''### Run Python Script ###'''

'''
@Tutorial Please refer to:
https://abapy.readthedocs.io/en/latest/tutorial.html
'''

import subprocess
import sys
import time
import os

### Define main variables:

var_1 = []

var_2 = {
    'var_2_1': [1, 2, 3],
    'var_2_2': [1, 2, 3],
}


class Testing_1():
    def def_1(self):
        print('Hello_1')

    def def_2(self):
        print('Hello_2')
        var = var_2['var_2_1'][0]
        #### if var can be not existing, set 'None'
        var_4 = var_2.get('var_2_1', None)
        print(var_4)
        print(f'Hello_2 print{var}')


class Testing_2():
    def __init__(self):
        self.def_x = Testing_1()

    def def_3(self):
        self.def_x.def_2()


class Run_script_Processing_odbFile():
    ####
    def Run_script(self):
        """
        :return:
        """
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

    def Processing_odbFile(self):
        """

        :return:
        """
        folder = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\Results\\'
        os.chdir(folder)
        ####### in Specific folder, find .odb file
        which_ODBfile = input("Please input: which Test Result? (e.g. Test+time+name): ")
        # for i,j,k in os.walk((os.path.join(os.getcwd(), "..")) + '\\Results\\'):
        for i, j, k in os.walk(os.getcwd() + '\\' + which_ODBfile):
            for file in k:
                # print(file)
                if file.endswith('.odb'):
                    print('The file Path is:  ' + os.path.join(i, file))
                    print('The file Path name is:  ' + file)
                    pathfile = os.path.join(i, file) + file
                else:
                    pass

            # folder = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\Results\\' + 'Test_' + time + '_' + name
        ######## Open my odb file

        # myOdb = openOdb(path='pathfile')


if __name__ == "__main__":
    # Run_script_Processing_odbFile().Run_script()
    Testing_2().def_3()
