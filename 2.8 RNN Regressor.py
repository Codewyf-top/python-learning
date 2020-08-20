# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/20 1:46 下午
@Auth ： Codewyf
@File ：2.8 RNN Regressor.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt

#torch.manual_seed(1) #reproducible

#Hyper Parameters
TIME_STEP = 10
INPUT_SIZE = 1
LR = 0.02

#show data
steps = np.linspace(0, np.pi*2, 100, dtype=np.float32)  #float32 for converting torch FLoatTensor
x_np = np.sin(steps)
y_np = np.cos(steps)
plt.plot(steps, y_np, 'r-', label='taget (cos)')
plt.plot(steps, x_np, 'b-', label='input (sin)')
plt.legend(loc='best')
plt.show()


class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.RNN(
            input_size=INPUT_SIZE,
            hidden_size  = 32,
            num_layers = 1,
            batch_first=True,

        )
        self.out = nn.Linear(32,1)

    def forward(self, x, h_state):
        # x (batch, time_step, input_size)
        # h_state (n_layers, batch, hidden_size)
        # r_out (batch, time_step, hidden_size)
        r_out, h_state = self.rnn(x, h_state)

        outs = []
        for time_step in range (r_out.size(1)): #calcuate output for each time step
            outs.append(self.out(r_out[:,time_step,:]))
        return torch.stack(outs, dim=1), h_state
rnn = RNN()
print(rnn)

optimizer = torch.optim.Adam(rnn.parameters(), lr=LR)
loss_func = nn.MSELoss()

h_state = None # for initial hidden state

plt.figure(1, figsize=(12,5))
plt.ion() #continously plot

for step in range (100):
    start, end = step* np.pi, (step+1)*np.pi #time range
    #use sin predicts cos
    steps = np.linspace(start, end, TIME_STEP, dtype=np.float32, endpoint=False) #float 32 for converting  torch FLoatTensor
    x_np = np.sin(steps)
    y_np = np.cos(steps)

    x = torch.from_numpy(x_np[np.newaxis,:,np.newaxis])   # shape (batch, time_step, input_size)增加纬度
    y = torch.from_numpy(y_np[np.newaxis,:, np.newaxis])

    prediction, h_state = rnn(x, h_state)
    # !!next  step is important!!
    h_state = h_state.data #repack the hidden state, break the connection from last iteration

    loss = loss_func(prediction,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


    #plotting

    plt.plot(steps, y_np.flatten(),'r-')
    plt.plot(steps,prediction.data.numpy().flatten(),'b-')
    plt.draw()
    plt.pause(0.5)

plt.ioff()
plt.show()
