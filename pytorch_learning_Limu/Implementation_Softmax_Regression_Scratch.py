# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/26 7:53 pm
@Auth ： Codewyf
@File ：Implementation_Softmax_Regression_Scratch.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""

import torch
from IPython import display
from d2l import torch as d2l
import warnings

warnings.filterwarnings('ignore')
batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

num_inputs = 784
num_outputs = 10

W = torch.normal(0, 0.01, size=(num_inputs, num_outputs), requires_grad=True)
b = torch.zeros(num_outputs, requires_grad=True)


def softmax(X):
    X_exp = torch.exp(X)
    partition = X_exp.sum(1, keepdim=True)
    return X_exp / partition # The boardcasting mechanism is applied here


X = torch.normal(0, 1, (2, 5))
X_prob = softmax(X)
print(X_prob)
print(X_prob.sum(1))


def net(X):
    return softmax(torch.matmul(X.reshape((-1, W.shape[0])), W) + b)


y = torch.tensor([0, 2])
y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
print(y_hat[[0, 1], y])


def cross_entropy(y_hat, y):
    return -torch.log(y_hat[range(len(y_hat)), y])


print(f' cross_entropy:  {cross_entropy(y_hat, y)}')


def accuracy(y_hat, y):
    """Compute the number of correct predictions"""
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())


print(f'accuracy {accuracy(y_hat, y) / len(y)}')


def evaluate_accuracy(net, data_iter):
    """Compute the accuracy for a model on a dataset."""
    if isinstance(net, torch.nn.Module):
        net.eval() # Set the model to evaluation mode
    metric = Accumulator(2) # No. of correct predictions, no. of predictions

    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.numel())

    return metric[0] / metric[1]


class Accumulator:
    """For accumulating sums over `n` variables."""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


print(f'evaluate_accuracy {evaluate_accuracy(net, test_iter)}')


def train_epoch_ch3(net, train_iter, loss, updater):
    """The training loop defined in Chapter 3"""
    # Set the model to training mode
    if isinstance(net, torch.nn.Module):
        net.train()
    # Sum of training loss, sum of training accuracy, no. of examples
    metric = Accumulator(3)
    for X, y in train_iter:
        # Compute gradients and update parameters
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            # Using PyTorch in-built optimizer & loss criterion
            updater.zero_grad()
            l.backward()
            updater.step()
            metric.add(float(l) * len(y), accuracy(y_hat, y), y.numel())
        else:
            # Using custom built optimizer & loss criterion
            l.sum().backward()
            updater(X.shape[0])
            metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
    # Return training loss and training accuracy
    return metric[0] / metric[2], metric[1] / metric[2]


class Animator:
    """For plotting data in animation"""
    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-', 'r:'), nrows=1, ncols=1,
                 figsize=(3.5, 2.5)):
        # Incrementally plot multiple lines
        if legend is None:
            legend = []
        d2l.use_svg_display()
        self.fig, self.axes = d2l.plt.subplots(nrows, ncols, figsize=figsize)
        if nrows * ncols == 1:
            self.axes = [self.axes,]
        # Use a lambda function to capture arguments
        self.config_axes = lambda: d2l.set_axes(self.axes[0],
                                                xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        self.X, self.Y, self.fmts = None, None, fmts


    def add(self, x, y):
        # Add multiple data points into the figure
        if not hasattr(y, "__len__"):
            y = [y]
        n = len(y)
        if not hasattr(x, "__len__"):
            x = [x] * n
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].cla()
        for x, y, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x, y, fmt)
        self.config_axes()
        display.display(self.fig)
        display.clear_output(wait=True)


def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):
    """Train a model (defined in Chapter 3)."""
    # animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
    #                    legend=['train loss', 'train acc', 'test acc'])
    for epoch in range(num_epochs):
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        # animator.add(epoch + 1,train_metrics + (test_acc,))
    train_loss, train_acc = train_metrics
    if train_loss < 0.5:
        print(f'train acc: {train_loss}')
    if train_acc <= 1 and train_acc > 0.7:
        print(f'train acc: {train_acc}')
    if test_acc <= 1 and test_acc > 0.7:
        print(f'train acc: {test_acc}')


lr = 0.1


def updater(batch_size):
    return d2l.sgd([W, b], lr, batch_size)


num_epochs = 10
train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs, updater)

"""
tensor([[0.2014, 0.1825, 0.2659, 0.3021, 0.0482],
        [0.3237, 0.0576, 0.1241, 0.3381, 0.1565]])
tensor([1.0000, 1.0000])
tensor([0.1000, 0.5000])
 cross_entropy:  tensor([2.3026, 0.6931])
accuracy 0.5
evaluate_accuracy 0.1385
train acc: 0.44718285611470543
train acc: 0.8478166666666667
train acc: 0.8349
"""