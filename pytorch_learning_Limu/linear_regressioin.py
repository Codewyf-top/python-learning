# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/24 5:38 pm
@Auth ： Codewyf
@File ：linear_regressioin.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""

import random
import torch
from d2l import torch as d2l


def synthethic_data(w, b, num_examples):
    """生成 y = Xw + b + 噪声."""
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))  # -1表示行数由pytorch推断，1表示1列


true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthethic_data(true_w, true_b, 1000)

print('features:', features[0], '\nlabel:', labels[0])

# d2l.set_figsize()
# d2l.plt.scatter(features[:, (1)].asnumpy(), labels.asnumpy(), 1);

def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(indices[i:min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]


batch_size = 10

for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    break

w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)


def linreg(X, w, b):
    """线性回归模型"""
    return torch.matmul(X, w) + b


def squared_loss(y_hat, y): # y_hat -> 预测值
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


def sgd(params, lr, batch_size):
    """小批量随机梯度下降"""
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


# 训练过程
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y) # 'x' 和 'y'的小批量损失
        # 因为'l'形状是('batch_size', 1), 而不是一个标量。 'l'中的所有元素被加到
        # 并以此计算关于['w', 'b']的梯度
        l.sum().backward()
        sgd([w, b], lr, batch_size) # 使用参数的梯度更新
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')


print(f'w的估计误差： {true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差： {true_b - b}')