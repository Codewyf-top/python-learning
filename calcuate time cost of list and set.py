# -*- coding: utf-8 -*-
"""
@Time:2020/8/6 17:10
@Auth:Codewyf
@File:calcuate time cost of list and set.py
@IDE:PyCharm
@Motto: Go Ahead Instead Of Heasitating
"""

import time
import find_unique_price_using_set
import find_unique_price_using_list
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))
## 输出
#time elapse using list: 41.61519479751587

# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
# 输出
#time elapse using set: 0.008238077163696289