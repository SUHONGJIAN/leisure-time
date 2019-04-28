# coding:utf-8
#开发人员   ：Hongjian SU
#开发时间   ：4/28/2019
#开发工具   ：PyCharm

dictionary_new = {1:"su", 2:"hong", 3:"jian"}
dic_key = [2, 5, 3, 8]
dic_key1 = (3, 7, 9, 0)
dic_value = ["sd", "ga", "sdf", "wt"]
a = dict(zip(dic_key, dic_value))
b = {dic_key1: dic_value}

print(dictionary_new)
print(dictionary_new.get(2, "default"))

for item in a.items():
    print(item)
if 2 in dictionary_new:
    print(2, dictionary_new[2])

print(a)
print(b)
print(a.get(3))

shj = set(["苏", "洪", "舰"])
jhs = set(["舰", "su", "hong"])
shj.add("hhhh")
shj.remove("苏")
#shj.clear()
print(shj, "\n")

print(shj & jhs)
print(shj | jhs)
print(shj - jhs)
