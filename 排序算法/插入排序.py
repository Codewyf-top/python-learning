# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/8 4:26 下午
@Auth ： Codewyf
@File ：插入排序.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])