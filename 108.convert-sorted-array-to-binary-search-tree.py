#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (69.83%)
# Likes:    9328
# Dislikes: 465
# Total Accepted:    971.2K
# Total Submissions: 1.4M
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        else:
            l = len(nums)
            mid = l // 2
            return TreeNode(
                val=nums[mid],
                left=self.sortedArrayToBST(nums[:mid]),
                right=self.sortedArrayToBST(nums[mid+1:])
            )

# @lc code=end

