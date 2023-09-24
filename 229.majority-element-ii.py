#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (46.04%)
# Likes:    7684
# Dislikes: 348
# Total Accepted:    432K
# Total Submissions: 936.7K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,2,3]
# Output: [3]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow up: Could you solve the problem in linear time and in O(1) space?
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq: freq[n] = 1
            else: freq[n] += 1
        return [n for n, f in freq.items() if f > len(nums) // 3]

# @lc code=end

