# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength, windowStart = float("inf"), 0
        for windowEnd in range(len(nums)):
            target -= nums[windowEnd]
            
            while target <= 0:
                minLength = min(minLength, windowEnd - windowStart + 1)
                target += nums[windowStart]
                windowStart += 1
        if minLength != float("inf"):
            return minLength
        else:
            return 0