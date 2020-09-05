# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/2 4:19 下午
@Auth ： Codewyf
@File ：JSON DEMO.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
"""
JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，
它的设计意图是把所有事情都用设计的字符串来表示，这样既方便在互联网上传递信息，
也方便人进行阅读（相比一些 binary 的协议）。JSON 在当今互联网中应用非常广泛，
也是每一个用 Python 程序员应当熟练掌握的技能点。设想一个情景，
你要向交易所购买一定数额的股票。那么，你需要提交股票代码、方向（买入 / 卖出）、订单类型（市价 / 限价）、价格（如果是限价单）、数量等一系列参数，
而这些数据里，有字符串，有整数，有浮点数，甚至还有布尔型变量，全部混在一起并不方便交易所解包。那该怎么办呢？
其实，我们要讲的 JSON ，正能解决这个场景。你可以把它简单地理解为两种黑箱：
第一种，输入这些杂七杂八的信息，比如 Python 字典，输出一个字符串；
第二种，输入这个字符串，可以输出包含原始信息的 Python 字典。

"""
import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

params_str = json.dumps(params)

print('after json serialization')
print('type of params_str = {}, params_srt = {}'.format(type(params_str), params))

original_params = json.loads(params_str)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))