class Students():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My name is %s and come from %s "%(name,city))
    def speak(self):
        print("我在慢慢学Python")
# stu1=Students("mary","上海")
# stu1.speak()
## from this directory
from test_1 import Students          #在同一个目录下调用模块和类；Student为模块，Students为类
name=Students("张三","郑州")
##from other directory
import os
os.chdir(r"/[Python-Abaqus API Project]/Python-Abaqus API")
from Test_Environment import Students  # School是文件名称，Students为模块名称，Student为类名称
stu1 = Student("张三", "云南")  # 传入参数
stu1.speak()  # 调用方法

