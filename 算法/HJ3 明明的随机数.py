# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/11 5:06 下午
@Auth ： Codewyf
@File ：HJ3 明明的随机数.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
while True:
    try:
        n = int(input())
        set1 = set({})
        for i in range(n):
            set1.add(int(input()))

        nums = list(set1)
        nums.sort()
        for i in nums:
            print(i)
    except:
        break
