# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/18 3:00 am
@Auth ： Codewyf
@File ：Custom_Layers.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
# 自定义层

import torch
import torch.nn.functional as F
from torch import nn


class CenteredLayer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X - X.mean()


layer = CenteredLayer()
layer(torch.FloatTensor([1, 2, 3, 4, 5]))

net = nn.Sequential(nn.Linear(8, 128), CenteredLayer())

Y = net(torch.rand(4, 8))
print(Y.mean())


class MyLinear(nn.Module):
    def __init__(self, in_units, units):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_units, units))
        self.bias = nn.Parameter(torch.randn(units, ))

    def forward(self, X):
        linear = torch.matmul(X, self.weight.data) + self.bias.data
        return F.relu(linear)


dense = MyLinear(5, 3)
print(f'dense.weight: {dense.weight}')

print(dense(torch.rand(2, 5)))

net = nn.Sequential(MyLinear(64, 8), MyLinear(8, 1))
print(f'net: {net(torch.rand(2, 64))}')
