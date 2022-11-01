# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        maxAverage = res / k
        for i in range(len(nums) - k):
            res -= nums[i]
            res += nums[i + k]
            maxAverage = max(maxAverage, res / k)            
        return maxAverage
                  

