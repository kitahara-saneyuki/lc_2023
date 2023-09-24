#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (54.21%)
# Likes:    13145
# Dislikes: 292
# Total Accepted:    1.6M
# Total Submissions: 3M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,null,3,null,3]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isTreeSymmetric(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot: return True
        if not leftRoot or not rightRoot: return False
        if leftRoot.val != rightRoot.val: return False
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right) and self.isTreeSymmetric(leftRoot.right, rightRoot.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isTreeSymmetric(root.left, root.right)
# @lc code=end

