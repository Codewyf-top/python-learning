# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/24 7:33 pm
@Auth ： Codewyf
@File ：linear_regression_simple.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating
https://zh-v2.d2l.ai/chapter_linear-networks/linear-regression-concise.html
"""
import numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = d2l.synthetic_data(true_w, true_b, 1000)


def load_array(data_arrays, batch_size, is_train=True):
    """构造一个PyTorch数据迭代器"""
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)


batch_size = 10
data_iter = load_array((features, labels), batch_size)

next(iter(data_iter))

# nn 是神经网络的缩写 neural network
from torch import nn

net = nn.Sequential(nn.Linear(2, 1))

# 初始化模型参数
net[0].weight.data.normal_(0, 0.01)
net[0].bias.data.fill_(0)

# 计算均方差使用的是MSELoss类，也称为平方L2范数。默认情况下，返回所有样本损失的平均值
loss = nn.MSELoss()

trainer = torch.optim.SGD(net.parameters(), lr=0.03)

num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X), y)
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l:f}')