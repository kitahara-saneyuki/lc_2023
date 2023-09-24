#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (52.38%)
# Likes:    7778
# Dislikes: 759
# Total Accepted:    1.1M
# Total Submissions: 2.1M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
# 
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, carry, i = "", 0, 0
        l_a, l_b = len(a), len(b)
        while i < l_a or i < l_b:
            a_i = int(a[l_a - i - 1]) if i < l_a else 0
            b_i = int(b[l_b - i - 1]) if i < l_b else 0
            curr = a_i + b_i + carry
            carry = curr // 2
            res = str(curr % 2) + res
            i += 1
        if carry:
            res = str(carry) + res
        return res

# @lc code=end

