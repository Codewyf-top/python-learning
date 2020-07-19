# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/19 3:25 下午
@Auth ： Codewyf
@File ：in or not in.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
old_list = ['西班牙', '葡萄牙', '葡萄牙', '牙买加', '匈牙利']
new_list = []
for each in old_list:
    if each not in new_list:
        new_list.append(each)
print(new_list)