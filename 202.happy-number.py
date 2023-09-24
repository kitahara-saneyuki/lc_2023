#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (55.04%)
# Likes:    9045
# Dislikes: 1179
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
# 
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# 
# 
# Return true if n is a happy number, and false if not.
# 
# 
# Example 1:
# 
# 
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1:
            s = str(n)
            st.add(n)
            n = sum(map(lambda i: int(i) ** 2, [i for i in s]))
            if n in st: return False
        return True

# @lc code=end

