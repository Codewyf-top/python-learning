# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/4 1:21 am
@Auth ： Codewyf
@File ：model_construction.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
import torch
from torch import nn
from torch.nn import functional as F

net = nn.Sequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))

X = torch.rand(2, 20)
net(X)


class MLP(nn.Module):
    # Declare a layer with model parameters. Here, we declare two fully
    # connected layers
    def __init__(self):
        # Call the constructor of the 'MLP' parent class 'Module' to perform
        # the necessary initialization. In this way, other function arguments
        # can also be specified during class instantiation, such as the model
        # parameters, 'params' (to be described later)
        super().__init__()
        self.hidden = nn.Linear(20, 256) # hidden layer
        self.out = nn.Linear(256, 10) # output layer

    # Define the forward propagation of the model, that is, how to return
    # required model output based on the input 'X'
    def forward(self, X):
        # Note here we use the functional version of the ReLU defined in the
        # nn.functional module
        return self.out(F.relu(self.hidden(X)))


net = MLP()
print(f'MLP:{net(X)}')


class MySequential(nn.Module):
    def __init__(self, *args):
        super().__init__()
        for block in args:
            self._modules[block] = block

    def forward(self, X):
        # OrderedDict guarantees that memeber will be traversed in the order
        # they were added
        for block in self._modules.values():
            X = block(X)
        return X


net = MySequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
print(f'MySequential: {net(X)}')


class FixedHiddenMLP(nn.Module):
    def __init__(self):
        super().__init__()
        # Random weight parameters that will not compute gradients and
        # therefore keep constant during training
        self.rand_weight = torch.rand((20, 20), requires_grad=False)
        self.linear = nn.Linear(20, 20)

    def forward(self, X):
        X = self.linear(X)
        # Use the created constant parameters, as well as the 'relu' and 'mm' functions
        X = F.relu(torch.mm(X, self.rand_weight) + 1)
        # Reuse the fully-connected layer. This is equivalent to sharing
        # parameters with two fully-connected layers
        X = self.linear(X)
        # Control flow
        while X.abs().sum() > 1:
            X /= 2
        return X.sum()


net = FixedHiddenMLP()
print(f'FixedHiddenMLP: {net(X)}')


class NestMLP(nn.Module):
    def __init__(self):
        super(NestMLP, self).__init__()
        self.net = nn.Sequential(nn.Linear(20, 64), nn.ReLU(),
                                 nn.Linear(64, 32), nn.ReLU())
        self.linear = nn.Linear(32, 16)

    def forward(self, X):
        return self.linear(self.net(X))


chimera = nn.Sequential(NestMLP(), nn.Linear(16, 20), FixedHiddenMLP())
print(f'chimera {chimera(X)}')