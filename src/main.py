# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/25 4:31 pm
@Auth ： Codewyf
@File ：main.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
from proto.mat import Matrix
from utils.mat_mul import mat_mul

a = Matrix([[1,2], [3,4]])
b = Matrix([[5,6], [7,8]])

print(mat_mul(a, b).data)