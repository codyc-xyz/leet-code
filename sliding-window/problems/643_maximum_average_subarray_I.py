# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAverage = float("-inf")
        for i in range(len(nums)):
            res = 0
            sub = nums[i:i+k]
            if len(sub) != k:
                break
            for n in range(len(sub)):
                res += sub[n]
            maxAverage = max(maxAverage, res /len(sub))
        return maxAverage
                  

