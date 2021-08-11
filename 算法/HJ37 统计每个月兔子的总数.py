# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/11 6:21 下午
@Auth ： Codewyf
@File ：HJ37 统计每个月兔子的总数.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
while True:
    try:
        month = int(input())
        n = month - 1
        def func(n):
            if n<2:
                return 1
            else:
                return func(n-1) + func(n-2)
        print(func(n))
    except:
        break
