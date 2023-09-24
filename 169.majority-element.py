#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (63.87%)
# Likes:    15704
# Dislikes: 458
# Total Accepted:    1.9M
# Total Submissions: 2.9M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
# 
# 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        max_freq, max_freq_val = 0, 0
        for n in freq:
            if freq[n] > max_freq:
                max_freq = freq[n]
                max_freq_val = n
        return max_freq_val

# @lc code=end

