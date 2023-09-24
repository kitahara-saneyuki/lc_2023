#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (62.39%)
# Likes:    11234
# Dislikes: 145
# Total Accepted:    976.5K
# Total Submissions: 1.6M
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: dp[i][j] = grid[i][j]
                elif i == 0: dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0: dp[i][j] = grid[i][j] + dp[i - 1][j]
                else: dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[m - 1][n - 1]

# @lc code=end

