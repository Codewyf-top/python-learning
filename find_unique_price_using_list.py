# -*- coding: utf-8 -*-
"""
@Time:2020/8/6 16:42
@Auth:Codewyf
@File:find_unique_price_using_list.py
@IDE:PyCharm
@Motto: Go Ahead Instead Of Hesitating
"""
#如果还是选择使用列表，对应的代码如下，其中，A 和 B 是两层循环。同样假设原始列表有 n 个元素，那么，在最差情况下，需要 O(n^2) 的时间复杂度。
#list version

def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products: #A
        if price not in unique_price_list: #B
            unique_price_list.append(price)
    return len(unique_price_list)

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
             ]

print('number of unique price is :{}'.format(find_unique_price_using_list(products)))

