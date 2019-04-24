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
print("的降幅较大发阿婆为飞机"
      "安居客都放假哦是放假啊送到就立刻"
      "发我去借钱问题")
print(chr(38))
fp.close()

'''
所以说都是注释惹的祸
中文 VS 英文
'''
