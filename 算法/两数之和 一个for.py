# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/16 3:33 下午
@Auth ： Codewyf
@File ：两数之和 一个for.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
nums = [2, 7 , 11, 15]
target = 9
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for x in range(n):
            a = target - nums[x]
            if a in nums:
                y = nums.index(a)
                if x == y:
                    continue
                else:
                    return x,y
                    break
            else:
                continue