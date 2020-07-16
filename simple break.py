# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/16 10:33 上午
@Auth ： Codewyf
@File ：simple break.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

bingo = '清蒸'
answer = input('小甲鱼是清蒸好吃还是炖了好吃?')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入（答案正确才能退出游戏）')
print('对嘛，只有清蒸才能原汁原味!')