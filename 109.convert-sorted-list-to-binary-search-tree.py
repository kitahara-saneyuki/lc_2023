#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (60.19%)
# Likes:    6732
# Dislikes: 145
# Total Accepted:    471.1K
# Total Submissions: 782.7K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height-balanced binary search tree.
# 
# 
# Example 1:
# 
# 
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
# 
# 
# Example 2:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.listToBST(head, None)

    def listToBST(self, head, tail):
        if head == tail: return None
        else:
            slow, fast = head, head
            while fast != tail and fast.next != tail:
                slow, fast = slow.next, fast.next.next
            root = TreeNode(slow.val)
            root.left = self.listToBST(head, slow)
            root.right = self.listToBST(slow.next, tail)
            return root

# @lc code=end

