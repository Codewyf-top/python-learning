# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/1 4:50 下午
@Auth ： Codewyf
@File ：python balckbox: input and output.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
"""
name =  input('your name:')
gender = input('you are a boy?(y/n)')

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {
    'prefix':'Mr.' if gender =='y' else 'Mrs.',
    'name' : name
}
print('authorizing...')
print(welcome_str.format(**welcome_dic))
"""

a = input()
b = input()
print('a+b = {}'.format((a+b)))
print('type of a is {}, type of b is {}'.format(type(a),type(b)))
print('a+b = {}'.format(int(a) + int(b)))
"""
1
2
a+b = 12"""