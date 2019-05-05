# coding:utf-8
#开发人员   ：Hongjian SU
#开发时间   ：5/5/2019
#开发工具   ：PyCharm

import os

#file1 = open("Test_internal1.txt", 'a+')
file2 = open("dog.jpg", "rb")

with open("Test_internal1.txt", 'a+') as file1:
    file1.write("6"*6 + "\n")
    file1.seek(0)
    print(file1.read())
    file1.seek(0)
    print(file1.readlines())
    print()

file2.close()

if os.name == "nt":
    print(os.name + ":是Windows系统啊" + os.linesep + os.sep)
else:
    print(os.name)

print(os.getcwd())
print(os.path.abspath("Test_internal1.txt"))
print(os.path.exists("Test_internal1.txt"))
print(os.path.exists("Test_internal2.txt"))
print(os.stat("Test_internal1.txt"))
