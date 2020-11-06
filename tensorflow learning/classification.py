# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/6 9:54 上午
@Auth ： Codewyf
@File ：classification.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
from __future__ import print_function
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from numpy import array
import os
#for MacOS system
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

learning_rate = 0.5
epoch = 1000

import tensorboard
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    #add one more layer and return the output of this layer
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name+'weights', Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b') #因为biases初始值不为0所以初始值随便加上一个0.1
            tf.summary.histogram(layer_name + 'biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases #Wx_plus_b = Weights * x + b iases
        if activation_function is None:
            outputs = Wx_plus_b
            tf.summary.histogram(layer_name + 'outputs', outputs)
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs:v_xs})
    correct_prediction = tf.equal(tf.arg_max(y_pre, 1), tf.argmax(v_ys, 1))#arg_max用来返回最大数值所在对下标,0表示按列返回，1表示按行返回
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs:v_xs, ys:v_ys})
    return result

#definde placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None,784])#784=28*28是每一张图片有784个像素点
ys = tf.placeholder(tf.float32, [None,10])

#add output layer
prediction = add_layer(xs, 784, 10, n_layer=1, activation_function=tf.nn.softmax)#softmax 一般用来 classification

#the error between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction), reduction_indices=[1])) #loss

train_step = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cross_entropy)

sess = tf.Session()
#important step
init = tf.global_variables_initializer()#初始所有变量
sess.run(init)

for i in range(epoch):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs:batch_xs, ys:batch_ys})
    if i % 50 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))
