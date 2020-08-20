# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/19 2:20 下午
@Auth ： Codewyf
@File ：slice list.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

list1 = ['钢铁侠', '蜘蛛侠', '蝙蝠侠', '绿灯侠', '神奇女侠']
list2 = []
for i in range(-2,0):
    list2.append(list1[i])
print(list2)

list3 = []
list3 = list1[2:5] #左闭右开
list4 = list1[::-2]
print(list3)
print(list4)
