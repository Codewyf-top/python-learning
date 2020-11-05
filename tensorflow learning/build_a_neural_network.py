# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/5 7:52 下午
@Auth ： Codewyf
@File ：build_a_neural_network.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
#for MacOS system
os.environ['KMP_DUPLICATE_LIB_OK']='True'
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1) #因为biases初始值不为0所以初始值随便加上一个0.1
    Wx_plus_b = tf.matmul(inputs, Weights) + biases #Wx_plus_b = Weights * x + b iases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300, dtype=np.float32)[:,np.newaxis] #300行一个特性，np.newaxis是用来增加一个维度 不加维度就不是矩阵了
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1])#None表示无论你给多少例子都ok，1代表一个属性; 行数不限制，列只能有一列
ys = tf.placeholder(tf.float32, [None, 1])
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
#hidden layer
prediction = add_layer(l1, 10, 1, activation_function=None) #in_size=10是l1的outsize 1是y_data的size 如果activation function=None, 就为线性函数

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1])) #reduce_sum是对每一个例子进行求和 reduce_mean对所有和求一个平均值
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss) #learning rate 这里的train_step相当于optimizer
#important step
init = tf.global_variables_initializer()#初始所有变量
sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()
for i in range(1000):
    sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
    if i % 50 == 0:
        # print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)

        plt.pause(0.1)