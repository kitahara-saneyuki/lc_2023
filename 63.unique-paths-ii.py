#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (39.66%)
# Likes:    7254
# Dislikes: 444
# Total Accepted:    709.1K
# Total Submissions: 1.8M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# You are given an m x n integer array grid. There is a robot initially located
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
# 
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that
# the robot takes cannot include any square that is an obstacle.
# 
# Return the number of possible unique paths that the robot can take to reach
# the bottom-right corner.
# 
# The testcases are generated so that the answer will be less than or equal to
# 2 * 10^9.
# 
# 
# Example 1:
# 
# 
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        grid = [[-square for square in row] for row in obstacleGrid]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] != -1: grid[i][0] = 1
            else: break
        for j in range(n):
            if grid[0][j] != -1: grid[0][j] = 1
            else: break
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] != -1:
                    a = grid[i][j - 1] if grid[i][j - 1] > 0 else 0
                    b = grid[i - 1][j] if grid[i - 1][j] > 0 else 0
                    grid[i][j] = a + b
        return grid[m - 1][n - 1] if grid[m - 1][n - 1] != -1 else 0

# @lc code=end

