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

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = windowStart = windowEnd = 0
        minLen = float("inf")
        while windowEnd < len(nums):
            res += nums[windowEnd]
            while windowEnd < len(nums) and res < target:
                windowEnd += 1
                if windowEnd < len(nums):
                    res += nums[windowEnd]
        
            while windowStart <= windowEnd and res >= target:
                minLen = min(minLen, windowEnd - windowStart + 1)
                res -= nums[windowStart]
                windowStart += 1
            windowEnd += 1
        
        if minLen != float("inf"):
            return minLen
        else:
            return 0
        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
        currSum = 0
        minLen = float('inf')
        windowStart = windowEnd = 0

        while windowEnd < len(nums):
            currSum += nums[windowEnd]
            if currSum >= target:
                while windowStart < windowEnd and currSum - nums[windowStart] >= target:
                    currSum -= nums[windowStart]
                    windowStart += 1
                minLen = min(minLen, windowEnd - windowStart + 1)
            windowEnd += 1

        return minLen if minLen != float('inf') else 0
            