#开发人员   ：Hongjian SU
#开发时间   ：4/19/2019
#开发工具   ：PyCharm

import datetime

a = "Ericsson"
b = "Hongjian SU"
c = input("Note: ")
c = "Note: " + c
d = datetime.datetime.now()
fp = open(r'Test_internal.txt', 'a+')
print(a, b, "\n", c, "\n", d, file=fp)
print(chr(38))
fp.close()

'''
就是
添加点
备注
'''
