# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/11 11:26 上午
@Auth ： Codewyf
@File ：HJ1 字符串最后一个单词的长度.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
while True:
    try:
        in_str = input()
        if len(in_str) > 5000 or len(in_str) == 0:
            raise Exception

        last = in_str.strip().split(" ")[-1]
        leng = len(last)
        print(leng)
        break
    except Exception:
        print("字符串为空或长度大于5000，请重新输入：")