# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/16 1:13 下午
@Auth ： Codewyf
@File ：simple break II.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

for year in range(2018, 2100):
    if (year %4 ==0) and (year % 100 !=0) or (year % 400 ==0):
        break
print("2018年以后出现的第一个闰年是：",year)