# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/30 9:39 上午
@Auth ： Codewyf
@File ：2.7 RNN.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import torch
import torchvision.datasets as dsets
from torch import nn
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

#Hyper Parameters
EPOCH = 1
BATCHSIZE = 64
TIME_STEP = 28
INPUT_SIZE = 28
LR = 0.01
DOWNLOAD_MNIST = False

train_data = dsets.MNIST(
    root='./mnist',
    train=True,
    transforms=transforms.ToTensor(),
    download=DOWNLOAD_MNIST
)
train_loader = torch.utils.data.DataLoader(
    dataset=train_data,
    batch_size=BATCHSIZE,
    shuffle=True
)
test_data = dsets.MNIST(root='./mnist', train=False, transforms=transforms.ToTensor())
test_x = test_data.test_data.type(torch.FloatTensor)[:2000]/255.
test_y = test_data.test_labels.numpy().squeeze()[:2000]

class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.LSTM(
            input_size=INPUT_SIZE,
            hidden_size=64,
            num_layers=1,
            batch_first=True,
        )
        self.out = nn.Linear(64, 10)

    def forward(self, x):
        r_out, (h_n, h_c) = self.rnn(x, None)       # x (batch, time_step, input_size


