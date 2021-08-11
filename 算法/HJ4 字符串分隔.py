# -*- coding: utf-8 -*-
"""
@Time ： 2021/8/11 5:34 下午
@Auth ： Codewyf
@File ：HJ4 字符串分隔.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
while True:
    try:
        inpt = input()
        if len(inpt) < 8:
            res = inpt + '0' * (8 - len(inpt))
            print(res)
        else:
            time = int(len(inpt) // 8)
            if len(inpt) % 8 == 0:
                for i in range(time):
                    print(inpt[i*8: i*8+8])
            else:
                for i in range(time):
                    print(inpt[i*8: i*8+8])
                print(inpt[time*8:] + '0' * (8 - len(inpt[time*8:])))
    except:
        break
