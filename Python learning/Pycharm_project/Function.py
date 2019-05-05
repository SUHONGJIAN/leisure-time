# coding:utf-8
# 开发人员   ：Hongjian SU
# 开发时间   ：4/28/2019
# 开发工具   ：PyCharm

print("欢迎使用Function库：")


def su(shj="shj"):
    print(shj.upper())


def hong():
    pass


su("gqgdasf")
su()
hong()
hong()

r = 2
q = 3
result = lambda m, n: m ** n
print(result(r, q))
