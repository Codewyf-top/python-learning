# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/26 4:18 pm
@Auth ： Codewyf
@File ：minst_classification.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""


# Fashion_MNIST

import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l

d2l.use_svg_display()

trans = transforms.ToTensor()
mnist_train = torchvision.datasets.FashionMNIST(
    root="../data", train=True,
    transform=trans, download=True
)
mnist_test = torchvision.datasets.FashionMNIST(
    root="../data", train=False,
    transform=trans, download=True
)