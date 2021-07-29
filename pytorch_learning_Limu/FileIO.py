# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/18 9:58 am
@Auth ： Codewyf
@File ：FileIO.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
import torch
from torch import nn
from torch.nn import functional as F

x = torch.arange(4)
torch.save(x, 'x-file')

x2 = torch.load('x-file')
print(f'x2: {x2}')


# 我们可以存储一个张量的列表，然后把他们读回内存
y = torch.zeros(4)
torch.save([x, y], 'x-files')
x2, y2 = torch.load('x-files')
print(f'x2:{x2}, y2:{y2}')