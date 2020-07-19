# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/16 4:45 下午
@Auth ： Codewyf
@File ：两数相加.py
@IDE ：PyCharm
@Motto：Go Ahead Instead of Heasitating

"""
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):

#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None) # 保存头节点，返回结果
        s = 0 #每一步的求和暂存量
        while l1 or l2 or s:  #循环条件：l1 或者l2（没有遍历完成），s(进位)不为0
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)    #构建新的list存储结果，其实用较长的加数链表存也可以，%10：求个位
            p = p.next
            s //= 10     #求进位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next