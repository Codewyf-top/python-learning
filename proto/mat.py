# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/25 4:30 pm
@Auth ： Codewyf
@File ：mat.py.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
class Matrix(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])
