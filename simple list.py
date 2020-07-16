# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/16 1:56 下午
@Auth ： Codewyf
@File ：simple list.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

number = [1,2,3,4,5,6,7,8]
print(type(number))
for each in number :
    print(each)

mix = [520, "codewyf", 3.14, [1,2,3]]

mix.append('blyat')
print(mix)

mix.extend([90,86])
print(mix)

mix.insert(0,0)
print(mix)

mix.insert(-1,888)
print(mix)

print(mix[5])
print(mix[len(mix)-1])
print(mix[-1])
print(mix[-2])
temp = mix[0]
mix[0] = mix[-1]
mix[-1]

import random
print('随机抽取',random.choice(mix))