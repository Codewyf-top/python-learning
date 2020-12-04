# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/6 5:24 下午
@Auth ： Codewyf
@File ：basic.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2
# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red', linewidth=1.0, linestyle='--')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8,-1,1.22,3],
            [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')

#gca = ' get current axis '
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaixs.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1))


plt.show()