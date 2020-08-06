# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/27 4:27 下午
@Auth ： Codewyf
@File ：dictionary and set.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

d = {'name': 'jason', 'age': 20}
print(d.get('name'))
#'jason'
print(d.get('location', 'null'))
#'null'

d = {'b':1, 'a':2, 'c':10}
print(d)
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])#根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda  x: x[1])#根据字典值的升序排序
print(d_sorted_by_key)
print(d_sorted_by_value)       #返回排序好的是列表
# [('a', 2), ('b', 1), ('c', 10)]
# [('b', 1), ('a', 2), ('c', 10)]


s = {3, 4, 2, 1}
sorted(s) # 对集合的元素进行升序排序
print(s)