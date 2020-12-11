# -*- coding: utf-8 -*-
"""
@Time ： 11/12/2020 15:07
@Auth ： Codewyf
@File ：4. 寻找两个正序数组的中位数.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
def helper(nums1,nums2,k):
    if(len(nums1) <len(nums2) ):
        nums1, nums2 = nums2 , nums1 #保持nums1比较长
    if(len(nums2)==0):
        return nums1[k-1] # 短数组空，直接返回
    if(k==1):
        return min(nums1[0],nums2[0])  #找最小数，比较数组首位
    t = min(k//2,len(nums2)) # 保证不上溢
    if( nums1[t-1]>=nums2[t-1] ):
        return helper(nums1 , nums2[t:],k-t)
    else:
        return helper(nums1[t:],nums2,k-t)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = ( len(nums1) + len(nums2) + 1 ) // 2
        k2 = ( len(nums1) + len(nums2) + 2 ) // 2
        def helper(nums1,nums2,k): #本质上是找第k小的数
            if(len(nums1) <len(nums2) ):
                nums1, nums2 = nums2 , nums1 #保持nums1比较长
            if(len(nums2)==0):
                return nums1[k-1] # 短数组空，直接返回
            if(k==1):
                return min(nums1[0],nums2[0])  #找最小数，比较数组首位
            t = min(k//2,len(nums2)) # 保证不上溢
            if( nums1[t-1]>=nums2[t-1] ):
                return helper(nums1 , nums2[t:],k-t)
            else:
                return helper(nums1[t:],nums2,k-t)
        return ( helper(nums1,nums2,k1) + helper(nums1,nums2,k2) ) /2
