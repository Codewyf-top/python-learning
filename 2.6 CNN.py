# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/8 18:51
@Auth ： Codewyf
@File ：2.6 CNN.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt
import os

#Hyper Parameters
EPOCH = 1
BATCH_SIZE = 50
LR = 0.001
DOWNLOAD_MNIST = False


if not(os.path.exists('./mnist/')) or not os.listdir('./mnist/'):
    # not mnist dir or mnist is empyt dir
    DOWNLOAD_MNIST = True

train_data = torchvision.datasets.MNIST(
    root='./mnist/',
    train=True,                                     # this is training data
    transform=torchvision.transforms.ToTensor(),    # Converts a PIL.Image or numpy.ndarray to
                                                    # torch.FloatTensor of shape (C x H x W) and normalize in the range [0.0, 1.0]
    #download=DOWNLOAD_MNIST,
)
#plot one example
# print(train_data.train_data.size())
# print(train_data.train_labels.size())
# plt.imshow(train_data.train_data[0].numpy(), cmap='gray')
# plt.title('%i' % train_data.train_labels[0])
# plt.show()

train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)

test_data = torchvision.datasets.MNIST(root= './mnist/', train=False)
test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000]/255.
test_y = test_data.test_labels[:2000]


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(      #(1, 28, 28)channel=1 28,28为图片的高和宽
                in_channels=1,          #input height
                out_channels=16,        #n_filters
                kernel_size=5,          #filter size
                stride=1,               #filter movement/size
                padding=2,              #如果stride=1，如果想要从conv2d输出的图片的长宽没有变化，padding=(kernel_size-1)/2
            ), #->(16,28,28)
            nn.ReLU(),  #->(16,28,28)
            nn.MaxPool2d(kernel_size=2),         #筛选重要信息，取区域最大的值    #->(16,14,14)
        )
        self.conv2 = nn.Sequential( #->(16,14,14)
            nn.Conv2d(16,32,5,1,2), #->(32,14,14)
            nn.ReLU(),              #->(32,14,14)
            nn.MaxPool2d(2),         #->(32,7,7)
        )
        self.out = nn.Linear(32 * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)    #(batch, 32, 7, 7)
        x = x.view(x.size(0), -1) #(batch, 32 * 7 * 7)
        output = self.out(x)
        return output, x


cnn = CNN()
#print((cnn))


optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)   # optimize all cnn parameters
loss_func = nn.CrossEntropyLoss()                       # the target label is not one-hotted

# following function (plot_with_labels) is for visualization, can be ignored if not interested
from matplotlib import cm
try: from sklearn.manifold import TSNE; HAS_SK = True
except: HAS_SK = False; print('Please install sklearn for layer visualization')
def plot_with_labels(lowDWeights, labels):
    plt.cla()
    X, Y = lowDWeights[:, 0], lowDWeights[:, 1]
    for x, y, s in zip(X, Y, labels):
        c = cm.rainbow(int(255 * s / 9)); plt.text(x, y, s, backgroundcolor=c, fontsize=9)
    plt.xlim(X.min(), X.max()); plt.ylim(Y.min(), Y.max()); plt.title('Visualize last layer'); plt.show(); plt.pause(0.01)

plt.ion()
# training and testing
for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(train_loader):   # gives batch data, normalize x when iterate train_loader

        output = cnn(b_x)[0]               # cnn output
        loss = loss_func(output, b_y)   # cross entropy loss
        optimizer.zero_grad()           # clear gradients for this training step
        loss.backward()                 # backpropagation, compute gradients
        optimizer.step()                # apply gradients

        if step % 50 == 0:
            test_output, last_layer = cnn(test_x)
            pred_y = torch.max(test_output, 1)[1].data.numpy()
            accuracy = float((pred_y == test_y.data.numpy()).astype(int).sum()) / float(test_y.size(0))
            print('Epoch: ', epoch, '| train loss: %.4f' % loss.data.numpy(), '| test accuracy: %.2f' % accuracy)
            if HAS_SK:
                # Visualization of trained flatten layer (T-SNE)
                tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
                plot_only = 500
                low_dim_embs = tsne.fit_transform(last_layer.data.numpy()[:plot_only, :])
                labels = test_y.numpy()[:plot_only]
                plot_with_labels(low_dim_embs, labels)
plt.ioff()

# print 10 predictions from test data
test_output, _ = cnn(test_x[:10])
pred_y = torch.max(test_output, 1)[1].data.numpy()
print(pred_y, 'prediction number')
print(test_y[:10].numpy(), 'real number')

# Epoch:  0 | train loss: 2.2895 | test accuracy: 0.11
# Epoch:  0 | train loss: 0.5506 | test accuracy: 0.81
# Epoch:  0 | train loss: 0.3311 | test accuracy: 0.91
# Epoch:  0 | train loss: 0.4317 | test accuracy: 0.90
# Epoch:  0 | train loss: 0.1738 | test accuracy: 0.93
# Epoch:  0 | train loss: 0.3081 | test accuracy: 0.94
# Epoch:  0 | train loss: 0.2965 | test accuracy: 0.95
# Epoch:  0 | train loss: 0.0320 | test accuracy: 0.95
# Epoch:  0 | train loss: 0.0736 | test accuracy: 0.94
# Epoch:  0 | train loss: 0.1082 | test accuracy: 0.95
# Epoch:  0 | train loss: 0.0439 | test accuracy: 0.96
# Epoch:  0 | train loss: 0.1777 | test accuracy: 0.96
# Epoch:  0 | train loss: 0.1089 | test accuracy: 0.96
# Epoch:  0 | train loss: 0.0496 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.2367 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.2066 | test accuracy: 0.96
# Epoch:  0 | train loss: 0.0097 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.1944 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.0880 | test accuracy: 0.98
# Epoch:  0 | train loss: 0.0161 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.0267 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.0440 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.0719 | test accuracy: 0.97
# Epoch:  0 | train loss: 0.0504 | test accuracy: 0.97
# [7 2 1 0 4 1 4 9 5 9] prediction number
# [7 2 1 0 4 1 4 9 5 9] real number
#
# Process finished with exit code 0
