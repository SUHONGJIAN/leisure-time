# coding:utf-8
#开发人员   ：Hongjian SU
#开发时间   ：4/28/2019
#开发工具   ：PyCharm

a = -7
c = [1, -3, 6, -2, 4, -7]
b = -a if a > 0 else a ** 2
print(b)

if a not in c:
    print(a, "不属于", c)
else:
    print(a, "属于", c)

if a is not None:
    print(a)
else:
    print("a为None")

j = 0
while j < 2:
    for i in "asdfasdg":
        if i == "d":
            break
        print(i, end=".")
    print("\n")
    j += 1
