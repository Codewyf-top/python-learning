# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/8 2:39 下午
@Auth ： Codewyf
@File ：冒泡排序.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

l1 = [1, 4, 5, 9, 76, 5, 43, 21]

for i in range (0, len(l1)-1):
    for j in range(0, len(l1)-i-1):
        if l1[j] > l1[j+1]:
            temp = l1[j]
            l1[j] = l1[j+1]
            l1[j+1] = temp
            #l1[j], l1[j+1] = l1[j+1], l1[j]

print(l1)