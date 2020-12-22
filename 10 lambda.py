# -*- coding: utf-8 -*-
"""
@Time ： 22/12/2020 10:55
@Auth ： Codewyf
@File ：10 lambda.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
l = [(1,20), (3,0),(9,10),(2,-1)]
l.sort(key=lambda x:x[1]) # 按列表中元组的第二个元素排序
print(l)


squared = map(lambda x: x**2, [1,2,3,4,5,6])
# print('square: {}'.format(squared))

from tkinter import Button, mainloop
button = Button(
    text = 'wyf是不是大帅比',
    command = lambda: print('yes!!!')
)
button.pack()
mainloop()

def mulitply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item*2)
    return new_list

# filter(function, iterable)
l = [1,2,3,4,5]
new_list = filter(lambda x: x % 2 ==0, l)
# filter() 函数表示对 iterable 中的每个元素，都使用 function 判断，并返回 True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。

from functools import reduce
# reduce(function, iterable)
l = [1,2,3,4,5]
product = reduce(lambda x,y: x * y, l)
# 它通常用来对一个集合做一些累积操作。function 同样是一个函数对象，规定它有两个参数，表示对 iterable 中的每个元素以及上一次调用后的结果，运用 function 进行计算，所以最后返回的是一个单独的数值。
# 1*2*3*4*5 = 120

d = {'mike': 10, 'lucy': 2, 'ben': 30}
sorted_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(sorted_list)
