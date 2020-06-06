# python-learning
1.0-1.7为python的一些语法的小练习的example

1.8的Variable在如今的PyTorh的版本中几乎已经不使用了

SGD == Stochastic Gradient Descent

1.9 激活函数

2.0&2.1采用了传统搭建网络的方式

2.2 采用快速搭建网络的方式:torch.nn.Sequential(

    torch.nn.Linear(2,10),
    
    torch.nn.ReLU(),#此处的ReLU大写与上面的funcitional中的不一样的写法是因为此处的ReLU是一个class，是当作一个类来使用的
    
    torch.nn.Linear(10,2),)
    
2.3 如何保存模型和读取模型（包含完整保存模型与仅保存模型参数）
