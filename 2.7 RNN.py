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
TIME_STEP = 28 #rnn time step / image height
INPUT_SIZE = 28 #rnn input size / image width
LR = 0.01
DOWNLOAD_MNIST = False

train_data = dsets.MNIST(
    root='./mnist',
    train=True,
    transform=transforms.ToTensor(),
    download=DOWNLOAD_MNIST
)
train_loader = torch.utils.data.DataLoader( #train_loader 这个data_loader 每次一批一批训练会比较有效率
    dataset=train_data,
    batch_size=BATCHSIZE,
    shuffle=True
)
test_data = dsets.MNIST(root='./mnist', train=False, transform=transforms.ToTensor())
test_x = test_data.test_data.type(torch.FloatTensor)[:2000]/255.
test_y = test_data.test_labels.numpy().squeeze()[:2000]

class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.LSTM( # 如果采用nn.RNN的形式，准确率没有LSTM那么高
            input_size=INPUT_SIZE,
            hidden_size=64,
            num_layers=1,
            batch_first=True,
        )
        self.out = nn.Linear(64, 10)

    def forward(self, x):
        r_out, (h_n, h_c) = self.rnn(x, None)       # x (batch, time_step, input_size) h_n, h_c 分别是一个分线程和一个主线程的hidden state
        out = self.out(r_out[:, -1, :])#(batch, time_step, input)  为了得到这一批图片的最后一个时间点的output
        return out

rnn = RNN()
print(rnn)


optimizer = torch.optim.Adam(rnn.parameters(), lr=LR)                 #optimize all rnn parameters
loss_func = nn.CrossEntropyLoss()

#training and testing
for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate (train_loader):             #give batch data
        b_x = b_x.view(-1,28,28)            #reshape x to (batch, time_step, input_size)      -1表示自动判断
        
        output = rnn(b_x)                    #run output
        loss = loss_func(output, b_y)        #cross entropy loss
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()                     #optimizer 的优化

        if step % 50 == 0:      #每50步，看一下训练的误差
            test_output = rnn(test_x)                  #(samples, time_step, input_size)
            pred_y = torch.max(test_output,1)[1].data.numpy()
            accuracy = float((pred_y == test_y).astype(int).sum())/float(test_y.size)
            print('EPOCH:', epoch, '|train loss : %4f' % loss.data.numpy(), '|test accuracy : %2f' % accuracy)

test_output = rnn(test_x[:10].view(-1,28,28))
pred_y = torch.max(test_output,1)[1].data.numpy()
print('prediction number:',pred_y)
print('real number:      ',test_y[:10])
            
            
        