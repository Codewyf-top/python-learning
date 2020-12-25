# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/25 4:30 pm
@Auth ： Codewyf
@File ：mat_mul.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
from proto.mat import Matrix

def mat_mul(matrix_1: Matrix, matrix_2: Matrix):
    assert matrix_1.m == matrix_2.n
    n, m, s = matrix_1.n, matrix_1.m, matrix_2.m
    result = [[0 for _ in range(n)]for _ in range(s)]
    for i in range(n):
        for j in range(s):
            for k in range(m):
                result[i][k] += matrix_1.data[i][j] * matrix_2.data[j][k]

    return Matrix(result)