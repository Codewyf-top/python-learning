# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/6 3:09 下午
@Auth ： Codewyf
@File ：2.5 Optimizer 优化器.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import torch
import torch.nn.functional as F
import torch.utils.data as Data
import matplotlib.pyplot as plt
from torch.autograd import Variable

# hyper parameters
LR = 0.01
BATCH_SIZE = 32
EPOCH = 12

x = torch.unsqueeze(torch.linspace(-1, 1, 1000), dim=1)
y = x.pow(2) + 0.1*torch.normal(torch.zeros(*x.size()))
#
# plt.scatter(x.numpy(), y.numpy())
# plt.show()
#
# optimizer = torch.optim.SGD()

torch_dataset = Data.TensorDataset(x,y)
loader = Data.DataLoader(dataset=torch_dataset, batch_size=BATCH_SIZE, shuffle=True,num_workers=2)

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(1,20)
        self.predict = torch.nn.Linear(20,1)

    def forward(self, x):
        x = F.relu((self.hidden(x)))
        x = self.predict(x)
        return x

# different nets
net_SGD = Net()
net_Momentum = Net()
net_RMSprop = Net()
net_Adam = Net()
nets = [net_SGD, net_Momentum, net_RMSprop, net_Adam]

opt_SGD = torch.optim.SGD(net_SGD.parameters(), lr = LR)
opt_Momentum = torch.optim.SGD(net_Momentum.parameters(), lr = LR, momentum=0.8)
opt_RMSprop = torch.optim.RMSprop(net_RMSprop.parameters(), lr = LR, alpha = 0.9)
opt_Adam = torch.optim.Adam(net_Adam.parameters(), lr = LR, betas=(0.9, 0.99))
optimizers = [opt_SGD, opt_Momentum, opt_RMSprop, opt_Adam]

loss_func = torch.nn.MSELoss()
losses_his = [[],[],[],[]] #record loss

for epoch in range(EPOCH):
    print('Epoch: ', epoch)
    for step, (b_x, b_y) in enumerate(loader):
        for net, opt, l_his in zip(nets, optimizers, losses_his):
            output = net(b_x)          #get output for every net
            loss = loss_func(output, b_y)   #compute loss for every net
            opt.zero_grad()            #clear gradients for next train
            loss.backward()            #backpropagation, compute gradients
            opt.step()                 #apple gradients
            l_his.append(loss.data.numpy()) #把误差放进losses_his的列表里面
# SGD 是最普通的优化器, 也可以说没有加速效果, 而 Momentum 是 SGD 的改良版, 它加入了动量原则.
# 后面的 RMSprop 又是 Momentum 的升级版. 而 Adam 又是 RMSprop 的升级版. 不过从这个结果中我们看到,
# Adam 的效果似乎比 RMSprop 要差一点. 所以说并不是越先进的优化器, 结果越佳. 我们在自己的试验中可以尝试不同的优化器,
# 找到那个最适合你数据/网络的优化器.

    labels = ['SGD', 'Momentum', 'RMSprop', 'Adam']
    for i, l_his in enumerate(losses_his):
        plt.plot(l_his, label=labels[i])
    plt.legend(loc='best')
    plt.xlabel('Steps')
    plt.ylabel('Loss')
    plt.ylim((0, 0.2))
    plt.show()