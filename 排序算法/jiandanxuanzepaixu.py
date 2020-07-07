# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/30 10:48 上午
@Auth ： Codewyf
@File ：jiandanxuanzepaixu.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
arr = [1, 5, 9, 7, 3, 4, 6, 2, 8]

print(arr)

for i in range(len(arr) - 1):
    max = i
    for j in range(i + 1 , len(arr)):
       if arr[j] < arr[max]:
           max = j
    if max != i:
         temp = arr[i]
         arr[i] = arr[max]
         arr[max] = temp
print (arr)
