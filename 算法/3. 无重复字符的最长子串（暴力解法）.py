# -*- coding: utf-8 -*-
"""
@Time ： 04/12/2020 10:03
@Auth ： Codewyf
@File ：3. 无重复字符的最长子串（暴力解法）.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
"""
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        #哈希集合，记录每一个字符是否出现过
        occ = set()
        n = len(s)
        #右指针，初始值为-1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range (n):
            if i != 0:
                #左指针向右移动一格，移除一个字符
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk + 1] not in occ:
                #不断移动右指针
                occ.add(s[rk + 1])
                rk += 1
            #第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        print(ans)
        return ans

if __name__ == '__main__':
    s = ''
    Solution.lengthOfLongestSubstring(s,s='abcabc')