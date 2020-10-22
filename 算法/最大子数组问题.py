# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/8 3:53 下午
@Auth ： Codewyf
@File ：最大子数组问题.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
#分治法
def find_max_subarray(A,low,high):
    '''

    :param A: 包含附属的列表
    :param low: 代表A的最小下标
    :param high: 代表A的最大下标
    :return:
    '''
    if low==high:
        return (low,high,A[low])
    else:
        mid = (low+high)/2
        (leftlow,lefthigh,leftsum) = find_max_subarray(A,low,mid)
        (rightlow,righthigh,rightsum) = find_max_subarray(A,mid+1,high)
        (crosslow,crosshigh,crosssum) = find_max_subarray(A,low,mid,high)
        if leftsum >= rightsum and leftsum >= corsssum:
            return (leftlow,lefthigh,leftsum)
        elif rightsum >= leftsum and rightsum >= crosssum:
            return (rightlow,righthigh,rightsum)
        else:
            return (crosslow,crosshigh,corsssum)
A=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(A)
low,high,sum=find_max_subarray(A,0,len(A)-1)
print(low,high,sum)
print(A[low:high+1])

