# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/16 3:36 下午
@Auth ： Codewyf
@File ：两数之和 字典.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
nums = [2, 7, 11, 15]
target = 0
class Solution:
    def twoSum(self, nums, target):
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d :
                return d[target-nums[x]],x
            else:
                d[nums[x]] = x