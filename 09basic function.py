# -*- coding: utf-8 -*-
"""
@Time ： 21/12/2020 22:07
@Auth ： Codewyf
@File ：09basic function.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""
def my_func(message):
    print('Got a message: {}'.format(message))

my_func('Hello World!')

def get_sum(a,b):
    return a+b

result = get_sum(1,2)
print(result)

def find_largest_element(l):
    if not isinstance(l,list):
        print('input is not type of list')
        return
    if len(l) == 0:
        print('empty input')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest element is: {}'.format(largest_element))

find_largest_element([8,1,-3,2,0,100])
print(get_sum([1,2],[3,4]))
print('Hello','Yunfei')

def f1():
    print('f1: Hello ')
    def f2():
        print('     f2: world ')
    f2()
f1()

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner: ', x)
    inner()
    print('outter: ', x)
outer()

# 闭包 closure
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是exponent_of函数

square = nth_power(2)
cube = nth_power(3)
square
cube
print(square(2)) # 计算2的平方
print(cube(4))   # 计算4的立方