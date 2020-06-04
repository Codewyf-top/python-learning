import torch
#from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)

# 画图
# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()

class Net(torch.nn.Module): #继承torch的Module
    def __init__(self,n_feature,n_hidden,n_output):
        super(Net,self).__init__() #继承__init__()功能
        self.hidden = torch.nn.Linear(n_feature,n_hidden) #隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden,n_output)  #输出层线性输出

    def forward(self,x) :  #Module中的forward功能
        #正向传播输入值，神经网络分析出输出值
        x = F.relu(self.hidden(x))   #activation function (隐藏层的线性值)
        x = self.predict(x)          #输出值
        return x

net = Net(1, 10, 1)
print(net)  #打印网络的结构
# Net(
#   (hidden): Linear(in_features=1, out_features=10, bias=True)
#   (predict): Linear(in_features=10, out_features=1, bias=True)
# )
#Stochastic Gradient Descent（SGD）
#optimizer是训练的工具
optimizer = torch.optim.SGD(net.parameters(),lr=0.2) #传入net 的所有参数，学习率learning rate
loss_func = torch.nn.MSELoss()                       #预测值和真实值的误差计算公式（均方差）Mean Square Error(MSE)

#可视化过程
plt.ion()#画图，matlab实时打印
plt.show()
plt.pause(0.1)
for t in range(100):
    prediction = net(x)  #给net训练数据x， 输出预测值
    loss = loss_func(prediction,y)

    optimizer.zero_grad() #清空上一步的残余更新参数值
    loss.backward()       #误差反向传播，计算参数更新值
    optimizer.step()      #将参数更新值施加到 net 的 parameters 上

    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)