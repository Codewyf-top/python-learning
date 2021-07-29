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

mydict = {'x': x, 'y': y}
torch.save(mydict, 'mydict')
mydict2 = torch.load('mydict')
print(f'mydict2: {mydict2}')


class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(20, 256)
        self.output = nn.Linear(256, 10)

    def forward(self, x):
        return self.output(F.relu(self.hidden(x)))


net = MLP()
X = torch.randn(size=(2, 20))
Y = net(X)
# save parameters
torch.save(net.state_dict(), 'mlp.params')

clone = MLP()
clone.load_state_dict(torch.load('mlp.params'))
clone.eval()
print(f'clone: {clone}')

Y_clone = clone(X)
print(Y_clone == Y)
