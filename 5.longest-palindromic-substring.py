#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (32.50%)
# Likes:    26139
# Dislikes: 1542
# Total Accepted:    2.5M
# Total Submissions: 7.7M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = s[i:j] is palindrome
        l = len(s)
        dp = [[False] * len(s) for _ in range(len(s))]
        # base case
        # dp[i][i] = True
        for i in range(l):
            dp[i][i] = True
        ret = s[0]
        # inductive case
        # we do it from bottom-up
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > len(ret):
                            ret = s[i: j + 1]
        return ret

# @lc code=end

