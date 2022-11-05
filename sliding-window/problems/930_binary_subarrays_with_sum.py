# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

class Solution:
     
    def atmost(self, nums, goal):
        res = count = windowStart = 0
        for windowEnd in range(len(nums)):
            if goal < 0:
                return 0
            goal -= nums[windowEnd]
            while goal < 0:
                goal += nums[windowStart]
                windowStart += 1
            res += windowEnd - windowStart + 1
        return res
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
         
        return self.atmost(nums, goal) - self.atmost(nums, goal - 1)
     