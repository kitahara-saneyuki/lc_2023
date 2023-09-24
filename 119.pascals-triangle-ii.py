#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (60.72%)
# Likes:    3655
# Dislikes: 296
# Total Accepted:    662.8K
# Total Submissions: 1.1M
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
# Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
# 
# 
# Constraints:
# 
# 
# 0 <= rowIndex <= 33
# 
# 
# 
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
# space?
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        else:
            lastPascal = self.getRow(rowIndex - 1)
            currPascal = [1]
            for p in range(1, len(lastPascal)):
                currPascal.append(lastPascal[p - 1] + lastPascal[p])
            currPascal.append(1)
            return currPascal

# @lc code=end

