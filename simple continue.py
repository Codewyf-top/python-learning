# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/16 1:43 下午
@Auth ： Codewyf
@File ：simple continue.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

for year in range(2018, 2050):
    if (year % 4 ==0) and (year % 100 != 100)or (year % 400 == 0):
        print(year)
        continue
