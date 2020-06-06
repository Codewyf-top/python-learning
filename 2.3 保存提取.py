# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/6 12:15 下午
@Auth ： Codewyf
@File ：2.3 保存提取.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

# torch.manual_seed(1) #reproducible

#fake data
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1) # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())  # noisy  y data (tensor), shape=(100,1 )

def save():
    #建立网络
    net1 = torch.nn.Sequential(
        torch.nn.Linear(1,10),
        torch.nn.ReLU(),
        torch.nn.Linear(10,1)
    )
    optimizer = torch.optim.SGD(net1.parameters(),lr=0.2)
    loss_func = torch.nn.MSELoss()

    #训练
    for t in range(100):
        prediction = net1(x)
        loss = loss_func(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    #plot result
    plt.figure(1, figsize=(10,3))
    plt.subplot(131)
    plt.title('Net1')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw = 5)

    torch.save(net1, 'net1.pkl')                          # save entire net
    torch.save(net1.state_dict(),'net1_parameters.pkl')  # save parameters (速度快，占用内存小)

def restore_net():
    net2 = torch.load('net1.pkl')
    prediction = net2(x)
    #plot result
    plt.subplot(132)
    plt.title('Net2')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw = 5)


def resotre_params():
    net3 = torch.nn.Sequential(
        torch.nn.Linear(1,10),
        torch.nn.ReLU(),
        torch.nn.Linear(10,1)
    )
    net3.load_state_dict(torch.load('net1_parameters.pkl'))
    prediction = net3(x)
    #plot result
    plt.subplot(133)
    plt.title('Net3')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw = 5)
    plt.show()

save()

restore_net()

resotre_params()