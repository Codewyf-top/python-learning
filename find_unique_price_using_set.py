# -*- coding: utf-8 -*-
"""
@Time:2020/8/6 17:05
@Auth:Codewyf
@File:find_unique_price_using_set.py
@IDE:PyCharm
@Motto: Go Ahead Instead Of Heasitating
"""
#但如果我们选择使用集合这个数据结构，由于集合是高度优化的哈希表，里面元素不能重复，并且其添加和查找操作只需 O(1) 的复杂度，那么，总的时间复杂度就只有 O(n)。
def find_unique_price_using_set(products):
    unique_price_set = []
    for _, price in products:
        unique_price_set.append(price)
    return len(unique_price_set)

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
             ]

print('number of unique price is :{}'.format(find_unique_price_using_set(products)))