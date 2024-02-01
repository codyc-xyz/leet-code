# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        dp = []
        i = 0
        for i, n1 in enumerate(nums):
            dp.append([n1])
            ans = max(ans, dp[i][-1])
            for j in range(i+1, len(nums)):
                dp[i].append(dp[i][-1]*nums[j])
                ans = max(ans, dp[i][-1])
            i += 1
        return ans

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        currMax, currMin = 1, 1
        for i, n1 in enumerate(nums):
            candidates = (n1, currMax * n1, currMin * n1)
            currMax = max(candidates)
            currMin = min(candidates)
            ans = max(ans, currMax)
        return ans
