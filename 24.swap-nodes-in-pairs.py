#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (64.21%)
# Likes:    11780
# Dislikes: 434
# Total Accepted:    1.3M
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# 
# 
# Example 2:
# 
# 
# Input: head = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(0, head)
        prev, curr = dummy, dummy.next
        while curr and curr.next:
            next = curr.next
            prev.next = next
            curr.next = next.next
            next.next = curr
            # 考点：指针向下推进到哪个节点？
            prev, curr = curr, curr.next
        return dummy.next
# @lc code=end

