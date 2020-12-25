# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/25 3:30 pm
@Auth ： Codewyf
@File ：13_main.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
from utils_13 import get_sum
from class_utils_13 import *

print(get_sum(1,2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))