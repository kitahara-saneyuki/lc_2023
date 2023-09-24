#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.09%)
# Likes:    9734
# Dislikes: 312
# Total Accepted:    2.4M
# Total Submissions: 3.7M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        chars = {chr(i + ord("a")): 0 for i in range(0, 26)}
        s, t = s.lower(), t.lower()
        for i in range(len(s)):
            chars[s[i]] += 1
            chars[t[i]] -= 1
        return True if not(any(chars.values())) else False

# @lc code=end

