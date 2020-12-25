# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/25 3:29 pm
@Auth ： Codewyf
@File ：class_utils_13.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
class Encoder(object):
    def encode(selfs, s):
        return s[::-1]

class Decoder(object):
    def decode(self, s):
        return ''.join(reversed(list(s)))