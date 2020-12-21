# -*- coding: utf-8 -*-
"""
@Time ： 21/12/2020 14:48
@Auth ： Codewyf
@File ：08异常处理.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Hesitating

"""

try:
    s = input('please enter two numbers separated by comma:')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except (ValueError, IndexError) as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error:{}'.format(err))
# except:
#     print('Other error')
print('continue')
...