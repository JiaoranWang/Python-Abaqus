'''
@Tutorial Please refer to:
https://abapy.readthedocs.io/en/latest/tutorial.html
'''

# from odbAccess import *
import os
####### find .odb file
folder = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\Results\\'
# make and change the work to folder
# os.makedirs(folder)
os.chdir(folder)
####### in Specific folder, find .odb file
which_ODBfile = input("Please input: which Test Result? (e.g. Test+time+name): ")
# for i,j,k in os.walk((os.path.join(os.getcwd(), "..")) + '\\Results\\'):
for i,j,k in os.walk(os.getcwd()+ '\\' + which_ODBfile):
    for file in k:
        # print(file)
        if file.endswith('.odb'):
            print('The file Path is:  '+ os.path.join(i,file))
            print('The file Path name is:  '+ file)
            pathfile = os.path.join(i,file) + file
        else:
            pass


    # folder = os.path.abspath(os.path.join(os.getcwd(), "..")) + '\\Results\\' + 'Test_' + time + '_' + name
######## Open my odb file

myOdb = openOdb(path='path\myfile.odb')



