#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Medium (42.47%)
# Likes:    2793
# Dislikes: 1859
# Total Accepted:    379.6K
# Total Submissions: 893.6K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# 
# Example 3:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^4
# 
# 
# 
# Follow up: Could you write a solution that works in logarithmic time
# complexity?
# 
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        while n > 0:
            ret += n // 5
            n //= 5
        return ret

# @lc code=end

