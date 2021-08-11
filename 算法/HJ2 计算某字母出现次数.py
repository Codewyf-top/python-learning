# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/11 11:50 上午
@Auth ： Codewyf
@File ：HJ2 计算某字母出现次数.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""


def get_num():
    fir_line = input()
    sec_line = input()
    if len(sec_line) == 0 or len(sec_line) > 1:
        return "第二行填入一个字符"
    leng = len(fir_line.strip().lower().split(sec_line.strip().lower())) - 1

    return leng


print(get_num())