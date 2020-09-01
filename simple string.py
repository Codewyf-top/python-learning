# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/1 2:29 下午
@Auth ： Codewyf
@File ：simple string.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
"""Python 中字符串的改变，通常只能通过创建新的字符串来完成。
想把'hello'的第一个字符'h'，改为大写的'H'，我们可以采用下面的做法：
第一种方法，是直接用大写的'H'，通过加号'+'操作符，
与原字符串切片操作的子字符串拼接而成新的字符串。
第二种方法，是直接扫描原字符串，把小写的'h'替换成大写的'H'，得到新的字符串
"""
s = 'hello'
s = 'H' + s[1:]
print(s)
m = s.replace('h', 'H')
print(m)

#str1 += str2 #表示str1 = str1 + str2

#字符串拼接 时间复杂度为O(n)
s = ''
for n in range(0,100000):
    s += str(n)

l=[]
for n in range(0,100000):
    l.append(str(n))
l = ' '.join(l)
"""
string.strip(str)#，表示去掉首尾的 str 字符串；
string.lstrip(str)#，表示只去掉开头的 str 字符串；
string.rstrip(str)#，表示只去掉尾部的 str 字符串。"""

s = ' my name is jason '
s.strip()
'my name is jason'

name = 'jason'
id = 123
print('no data available for person with id: {}, name: {}'.format(id, name))
#.format()是所谓的格式化函数，{}是所谓的格式符，用来为后面的真实值————变量name预留位置。

#不过要注意，string.format() 是最新的字符串格式函数与规范。
# 自然，我们还有其他的表示方法，比如在 Python 之前版本中，字符串格式化通常用 % 来表示，
# 那么上述的例子，就可以写成下面这样：
print('no data available for person with id: %s, name: %s' % (id, name))

stu_name = 'codewyf'
stu_id = 16011524
print('The excellent students name:{},stu_id:{}'.format(stu_name,stu_id))
