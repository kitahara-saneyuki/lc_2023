#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.28%)
# Likes:    18652
# Dislikes: 1077
# Total Accepted:    3.1M
# Total Submissions: 7.8M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            # push stack on left brackets
            if char in ["(", "[", "{"]: stk.append(char)
            else:
                # corner case: stack empty
                if not stk: return False
                elif char == ")":
                    # popping stack
                    if stk[-1] == "(": stk.pop()
                    else: return False
                elif char == "]":
                    if stk[-1] == "[": stk.pop()
                    else: return False
                elif char == "}":
                    if stk[-1] == "{": stk.pop()
                    else: return False
        # corner case: check stack empty
        if stk:
            return False
        return True

# @lc code=end

