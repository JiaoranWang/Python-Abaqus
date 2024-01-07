'''
@Tutorial Please refer to:
https://abapy.readthedocs.io/en/latest/tutorial.html
https://www.bilibili.com/read/cv22522234/?spm_id_from=333.999.0.0
@using 'ctrl+alt+l' to sort the format
@Introduction:
This Processing_odbFile.py is providing basic commands for running.odb results
using python
****@API Tutorial Please refer to:[Setion 3.2]
http://130.149.89.49:2080/v6.14/books/cmd/default.htm?startat=pt01ch01.html
'''

# from odbAccess import *
import os
from odbAccess import openOdb
# from textRepr import *

####### find .odb file

folder = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\Results\\'
# make and change the work to folder
# os.makedirs(folder)
os.chdir(folder)
####### in Specific folder, find .odb file
which_ODBfile = input("Please input: which Test Result? (e.g. Test+time+name): ")
# for i,j,k in os.walk((os.path.join(os.getcwd(), "..")) + '\\Results\\'):
for i, j, k in os.walk(os.getcwd() + '\\' + which_ODBfile):
    for file in k:
        # print(file)
        if file.endswith('.odb'):
            file_path = os.path.join(i, file)
            print('The file_Path is:  ' + file_path)
            print('The file_Path name is:  ' + file)
            # pathfile = os.path.join(i, file) + file
        else:
            print('No pathfile')
            pass

    # folder = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\Results\\' + 'Test_' + time + '_' + name
######## Open my odb file
myOdb = openOdb(file_path)
## the path canbe myOdb = openOdb(r'C:\Users\jiaor\Abaqus_workdict\CFRP_Tube_1.odb')
### The following you can use in Abaqus prompt to see the data structure:
## To save the output:

dir(myOdb)
# OK let's have a look inside jobData
print(myOdb.jobData)
print(myOdb.diagnosticData)
print(myOdb.diagnosticData.jobStatus)
# Now we know that the simulation was successful Let's now have a look to history outputs
print(myOdb.steps)
print(myOdb.steps['LOADING'])
print(myOdb.steps['LOADING'].frames[-1])
print(myOdb.steps['LOADING'].historyRegions['Assembly ASSEMBLY'])
# And then to field outputs
print(myOdb.steps['LOADING'].frames[-1].fieldOutputs['U'].values[0])
# ({'baseElementType': '', 'conjugateData': None, 'conjugateDataDouble': 'unknown', 'data': array([-2.51322398980847

# Example_1
# odb object
my_odb = openOdb(r"D:\SIMULIA2020\script_learning\case3\ODBandOtherRealtingFiles\Job-1.odb") #改为你自己ODB文件所在地址
step = my_odb.steps['Step-1'] #which step
frame = step.frames[-1] #which frame?(-1 means last step)
# Get the global displacement field variable
dis_field = frame.fieldOutputs['U']

# *****************************************************
# 指定想要获取的节点编号
node_Labels = (55,56,57,58) #改为你想提取的节点编号
# 在PART-1-1中定义名称为set_for_datas的集合，包含node_Labels节点编号，并将其赋予给变量node_set
node_set = my_odb.rootAssembly.instances['PART-1-1'].NodeSetFromNodeLabels(name='set_for_datas',nodeLabels=node_Labels)
# 在前述全局位移场变量的基础上提取局部位移场
local_dis_values = dis_field.getSubset(region=node_set)
# *****************************************************
# 生成txt文件，并将提取的结果写入
with open('data.txt','w') as f:  #可修改路径为绝对路径
	f.write("NodeLabel, NodeDis\n")
	for node_value in local_dis_values.values:
		txt_line = "{}, {}\n".format(node_value.nodeLabel, node_value.magnitude)

#Example_2


