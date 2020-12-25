# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/25 3:36 pm
@Auth ： Codewyf
@File ：sub_main.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
"""
├── utils
│      ├── utils.py
│      └── class_utils.py
├── src
│    └── sub_main.py
└── main.py
"""
import sys
sys.path.append("..")

from utils.class_utils import *

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))