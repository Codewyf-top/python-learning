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
    transform=trans, download=False
)
mnist_test = torchvision.datasets.FashionMNIST(
    root="../data", train=False,
    transform=trans, download=False
)

print(len(mnist_train))
print(len(mnist_test))

print(mnist_train[0][0].shape)


def get_fashion_mnist_labels(labels):
    """返回Fashion-MNIST数据集的文本标签"""
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt',
        'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]


def show_images(imgs, num_rows, num_cols, titles=None, scale=0.5):
    """Plot a list of images"""
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            # 图片张量
            ax.imshow(img.numpy())
        else:
            # PIL图片
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes


X, y = next(iter(data.DataLoader(mnist_train, batch_size=18)))
# show_images(X.reshape(18, 28, 28), 2, 9, titles=get_fashion_mnist_labels(y));


batch_size = 256


def get_dataloader_workers():
    """Use 4 processes to read the data."""
    return 0


train_iter = data.DataLoader(mnist_train, batch_size, shuffle=True,
                             num_workers=get_dataloader_workers())


# Put all things together
def load_data_fashion_mnist(batch_size, resize=None):
    """Download the Fashion-MNIST dataset and then load it into memory"""
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(root="../data", train=True,
                                                    download=False, transform=trans)
    mnist_test = torchvision.datasets.FashionMNIST(root="../data", train=False,
                                                   download=False, transform=trans)
    return (data.DataLoader(mnist_train, batch_size,
                             shuffle=True, num_workers=get_dataloader_workers()),
             data.DataLoader(mnist_test, batch_size, shuffle=False,
                             num_workers=get_dataloader_workers())
             )