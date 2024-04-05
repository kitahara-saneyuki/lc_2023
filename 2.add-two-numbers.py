#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (42.62%)
# Likes:    30315
# Dislikes: 5981
# Total Accepted:    4.5M
# Total Submissions: 10.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur, carry = dummy, 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1: cur.next = l1
        else: cur.next = l2
        if cur.next:
            # 考点：可以无限进位
            while carry and cur.next:
                val = cur.next.val + carry
                cur.next.val = val % 10
                carry = val // 10
                cur = cur.next
        # 由于我们已经考虑过了无限进位，在这里只考虑位数不够的情况
        if carry: cur.next = ListNode(carry)
        return dummy.next
# @lc code=end

