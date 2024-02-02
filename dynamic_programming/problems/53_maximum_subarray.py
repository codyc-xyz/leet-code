# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0 for _ in range(len(nums))]
        res = 0
        for i, n in enumerate(nums):
            if i > 0:
                res = max(res + n, n)
            else:
                res = n
            dp[i] = res
        return max(dp)

