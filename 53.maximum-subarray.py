#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]
        res = dp[0]
        for i in range(1, n):
            dp.append(max(dp[i - 1], 0) + nums[i])
            res = max(dp[i], res)
        return res
# @lc code=end

