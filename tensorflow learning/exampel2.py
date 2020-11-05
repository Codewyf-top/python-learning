# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/5 4:23 下午
@Auth ： Codewyf
@File ：exampel2.py.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import tensorflow as tf
import numpy as np
#create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

###create tensorflow structure start###
Weights = tf.Variable(tf.random.uniform([1],-1.0,1.0))  #random_uniform随机均匀分布[1]是纬度，-1,1是定义的随机数的范围
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data)) #计算预测的y与实际的y的差别
optimizer = tf.train.GradientDescentOptimizer(0.5) #o.5->learning rate
train = optimizer.minimize(loss)

#初始化
init = tf.global_variables_initializer()
###create tensorflow structure start###

sess = tf.Session()
sess.run(init)    #Very important

for step in range(201):
    sess.run(train)
    if step % 20 ==0:
        print(step, sess.run(Weights), sess.run(biases))

