# coding:utf-8
#开发人员   ：Hongjian SU
#开发时间   ：5/6/2019
#开发工具   ：PyCharm

import sqlite3

shj = sqlite3.connect('suhj.db')
curs = shj.cursor()

#curs.execute('create table user (id int(10) primary key, name varchar(20))')
curs.execute('insert into user(id, name) values ("1", "Ericsson")')
curs.execute('insert into user(id, name) values ("2", "suhongjian")')
curs.execute('insert into user(id, name) values ("3", "苏洪舰")')

curs.execute('select * from user')
result = curs.fetchall()

curs.close()
shj.close()

print(result)
