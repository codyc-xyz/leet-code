# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

class Solution:
     
    def atMost(self, nums, goal):
        res = windowStart = 0
        for windowEnd in range(len(nums)):
            goal -= nums[windowEnd]
            while goal < 0 and windowEnd >= windowStart:
                goal += nums[windowStart]
                windowStart += 1
            res += windowEnd - windowStart + 1
        return res
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
         
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
     
            