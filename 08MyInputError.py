# -*- coding: utf-8 -*-
"""
@Time ： 21/12/2020 20:39
@Auth ： Codewyf
@File ：08MyInputError.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
class MyInputError(Exception):
    """
    Exception Raised when there're errors in input
    """
    def __init__(self,value): # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的String表达形式
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise MyInputError(1) # 抛出MyInputError这个异常
except MyInputError as err:
    print("error: {}".format(err))