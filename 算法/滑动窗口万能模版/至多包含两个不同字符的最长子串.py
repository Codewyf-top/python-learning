# -*- coding: utf-8 -*-
"""
@Time ： 04/12/2020 10:35
@Auth ： Codewyf
@File ：至多包含两个不同字符的最长子串.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] == 0:
                counter += 1
            lookup[s[end]] += 1
            end +=1
            while counter > 2:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len

