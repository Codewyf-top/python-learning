# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/8 2:43 下午
@Auth ： Codewyf
@File ：选择排序.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
a = [1, 8, 3, 9, 4, 43, 21]
for i in range(len(a)-1):
    min  = i
    for j in range (i+1, len(a)):
        if a[min] > a[j]:
            min = j
        if min != i:
            a[min],a[i] = a[i], a[min]

print(a)