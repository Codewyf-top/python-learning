# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/5 7:43 下午
@Auth ： Codewyf
@File ：def add_layer().py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import tensorflow as tf

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.randow_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([out_size, 1]) + 0.1) #因为biases初始值不为0所以初始值随便加上一个0.1
    Wx_plus_b = tf.matmul(inputs, Weights) + biases #Wx_plus_b = Weights * x + b iases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
