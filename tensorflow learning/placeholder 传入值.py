# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/5 5:07 下午
@Auth ： Codewyf
@File ：placeholder 传入值.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)
with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1:[7.], input2:[2.0]}))