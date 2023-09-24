#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (72.95%)
# Likes:    18720
# Dislikes: 755
# Total Accepted:    1.5M
# Total Submissions: 2M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(str, l, r):
            if l > r: return
            if l == 0 and r == 0:
                result.append(str)
                return
            if l: dfs(str + "(", l - 1, r)
            if r: dfs(str + ")", l, r - 1)
        dfs("", n, n)
        return result
# @lc code=end

