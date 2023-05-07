# Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        pSum = {0: 0}
        currSum = 0
        ans = 0
        for i, n in enumerate(nums):
            currSum += n
            if currSum - target in pSum:
                ans += 1
                pSum = {}
            pSum[currSum] = i + 1
        return ans
                

        