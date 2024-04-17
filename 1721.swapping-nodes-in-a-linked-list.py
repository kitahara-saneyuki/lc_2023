#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
#
# algorithms
# Medium (68.02%)
# Likes:    5254
# Dislikes: 176
# Total Accepted:    324.9K
# Total Submissions: 477.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# You are given the head of a linked list, and an integer k.
# 
# Return the head of the linked list after swapping the values of the k^th node
# from the beginning and the k^th node from the end (the list is 1-indexed).
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= k <= n <= 10^5
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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        cur1, cur2, cur2_lead = head, head, head
        for i in range(0, k - 1):
            cur1, cur2_lead = cur1.next, cur2_lead.next
        while cur2_lead.next != None:
            cur2, cur2_lead = cur2.next, cur2_lead.next
        cur1.val, cur2.val = cur2.val, cur1.val
        return head
        
# @lc code=end

