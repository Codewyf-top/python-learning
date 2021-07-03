# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/2 7:26 pm
@Auth ： Codewyf
@File ：weight_decay.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
import torch
from torch import nn
from d2l import torch as d2l


n_train, n_test, num_inputs, batch_size = 20, 100, 200, 5
true_w, true_b = torch.ones((num_inputs, 1)) * 0.01, 0.05
train_data = d2l.synthetic_data(true_w, true_b, n_train)
train_iter = d2l.load_array(train_data, batch_size)
test_data = d2l.synthetic_data(true_w, true_b, n_test)
test_iter = d2l.load_array(test_data, batch_size, is_train=False)


def init_params():
    w = torch.normal(0, 1, size=(num_inputs, 1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)
    return [w,b]


def l2_penalty(w):
    return torch.sum(w.pow(2)) / 2


def train(lambd):
    w, b = init_params()
    net, loss = lambda X: d2l.linreg(X, w, b), d2l.squared_loss
    num_epochs, lr = 100, 0.003
    for epoch in range(num_epochs):
        for X, y in train_iter:
            # The L2 norm penalty term has been added, and broadcasting
            # makes 'l2_penalty(w)' a vector whose length is 'batch_size'
            l = loss(net(X), y) + lambd * l2_penalty(w)
            l.sum().backward()
            d2l.sgd([w, b], lr, batch_size)
        if (epoch + 1) % 5 == 0:
            print(f'epoch + 1 {d2l.evaluate_loss(net, train_iter, loss)} {d2l.evaluate_loss(net, test_iter, loss)}')
            print('L2 norm of w:', torch.norm(w).item())



# train(lambd=0)
# train(lambd=3)


def train_concise(wd):
    net = nn.Sequential(nn.Linear(num_inputs, 1))
    for param in net.parameters():
        param.data.normal_()
    loss = nn.MSELoss()
    num_epochs, lr = 100, 0.003
    # The bias parameter has not decayed
    trainer = torch.optim.SGD([{
        "params": net[0].weight,
        'weight_decay': wd}, {
        "params": net[0].bias}], lr=lr)
    for epoch in range(num_epochs):
        for X, y in train_iter:
            trainer.zero_grad()
            l = loss(net(X), y)
            l.backward()
            trainer.step()
        if (epoch + 1) % 5 ==0:
            d2l.evaluate_loss(net, train_iter, loss)
            d2l.evaluate_loss(net, test_iter, loss)
    print('L2 norm of w:', net[0].weight.norm().item())


train_concise(0)
train_concise(3)
