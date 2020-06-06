# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/6 1:46 下午
@Auth ： Codewyf
@File ：2.4 mini batch training.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import torch
import torch.utils.data as Data

BATCH_SIZE = 5

x = torch.linspace(1, 10, 10)
y = torch.linspace(10, 1, 10)

torch_dataset = Data.TensorDataset(x, y) #转换成torch能识别的Dataset

#将dataset放入Dataloader
loader = Data.DataLoader(
    dataset=torch_dataset,           # torch TensorDataset format
    batch_size=BATCH_SIZE,           # mini batch size
    shuffle=True,                    #是否需要打乱数据（打乱比较好）
    num_workers=2,                   #多线程来读数据

)

for epoch in range(3):                                      # 训练所有!整套!数据 3 次
    for step, (batch_x, batch_y) in enumerate(loader):      # 每一步 loader 释放一小批数据用来学习
        #training...
        print('Epoch: ', epoch, '| Step: ', step, '| batch x: ', batch_x.numpy(), '| batch y: ', batch_y.numpy())
#
# Epoch:  0 | Step:  0 | batch x:  [ 9. 10.  6.  5.  1.] | batch y:  [ 2.  1.  5.  6. 10.]
# Epoch:  0 | Step:  1 | batch x:  [2. 3. 7. 4. 8.] | batch y:  [9. 8. 4. 7. 3.]
# Epoch:  1 | Step:  0 | batch x:  [5. 4. 9. 8. 6.] | batch y:  [6. 7. 2. 3. 5.]
# Epoch:  1 | Step:  1 | batch x:  [10.  2.  7.  3.  1.] | batch y:  [ 1.  9.  4.  8. 10.]
# Epoch:  2 | Step:  0 | batch x:  [2. 8. 6. 5. 4.] | batch y:  [9. 3. 5. 6. 7.]
# Epoch:  2 | Step:  1 | batch x:  [ 7. 10.  9.  1.  3.] | batch y:  [ 4.  1.  2. 10.  8.]