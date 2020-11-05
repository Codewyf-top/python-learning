# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/5 4:47 下午
@Auth ： Codewyf
@File ：session control.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import tensorflow as tf


matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])

product = tf.matmul(matrix1, matrix2)   #ma trix multiply

# #method 1
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()

#method 2
#好处是不用使用sess.close() 用with的话可以自动关不session
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
    #运行结束后会自动close