#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (50.60%)
# Likes:    3645
# Dislikes: 2524
# Total Accepted:    546K
# Total Submissions: 1.1M
# Testcase Example:  '"hello"'
#
# Given a string s, reverse only all the vowels in the string and return it.
# 
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases, more than once.
# 
# 
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        ls_str = list(s)
        vowel_ls, vowel_i = "", []
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_ls += s[i]
                vowel_i.append(i)
        vowel_ls = vowel_ls[::-1]
        j = 0
        for i in vowel_i:
            ls_str[i] = vowel_ls[j]
            j += 1
        return "".join(ls_str)

# @lc code=end

