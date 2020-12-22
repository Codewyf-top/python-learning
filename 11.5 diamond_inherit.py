# -*- coding: utf-8 -*-
"""
@Time ： 22/12/2020 21:44
@Auth ： Codewyf
@File ：11.5 diamond_inherit.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
"""

 --->B---
A-      -->D
 --->C---
"""
class A():
    def __init__(self):
        print('enter A')
        print('leave A')

class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')

class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')

class D(B,C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')

D()

"""
第一个问题，面向对象编程四要素是什么？它们的关系又是什么？
答：面向对象编程四要素是类，属性，函数，对象，
       它们关系可以总结为：类是一群具有相同属性和函数的对象的集合。
第二个问题，讲了这么久的继承，继承究竟是什么呢？你能用三个字表达出来吗？
三个字：父与子。儿子可以使用自己的东西，没有的可以使用父亲的东西。

"""
