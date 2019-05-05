# coding:utf-8
# 开发人员   ：Hongjian SU
# 开发时间   ：4/29/2019
# 开发工具   ：PyCharm

import math
import time
import datetime


def wrap():
    print()


wrap()
print(time.ctime())
print(datetime.datetime.now())
wrap()


class Hongjian:
    s = "I'm Hongjian SU"
    _h = "123"
    __j = "456"

    def __init__(self, message="default", r=6):
        print(message)
        self.r = r

    @property
    def area(self):
        return math.pi * self.r ** 2

    # @property
    # def rs(self):
    #     return self.r


# SU = Hongjian("Who am I???", 3)
# print(SU.s)
# print(SU._h)
# # print(SU.__j)
# print(SU._Hongjian__j)
# print(SU.area)
# SU.rs = 1
# print(SU.rs)


'''
Inherit
'''


class HJ(Hongjian):
    @property
    def area(self):
        return 4 * self.r


# jk = HJ()
# print(jk.area)
