#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (67.72%)
# Likes:    3135
# Dislikes: 95
# Total Accepted:    203.3K
# Total Submissions: 300.3K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level x such that the sum of all the values of nodes at
# level x is maximal.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# Example 2:
# 
# 
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, level, lvl_cnt, lvl_max = -2**31, [root], 1, 0
        while root and level:
            lvl_sum = sum(map(lambda node: node.val, level))
            if lvl_sum > max_sum:
                lvl_max = lvl_cnt
                max_sum = lvl_sum
            level = [kid for node in level for kid in (node.left, node.right) if kid]
            lvl_cnt += 1
        return lvl_max

# @lc code=end

