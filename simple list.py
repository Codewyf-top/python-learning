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
print('随机抽取:',random.choice(mix))

mix.remove("codewyf")#使用remove（）删除元素，并不知道这个元素在列表中的具体位置。但是如果制定的元素不存在与列表中，会报错
print(mix)

mix.pop(0)#pop需要一个索引值，取出并删除该元素
print(mix)

mix.pop()#如果不带参数，默认弹出列表最后一个元素
print(mix)

del mix[0]
print(mix)
