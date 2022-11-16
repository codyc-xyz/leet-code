# You are given an integer array nums and an integer k. 
# Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.

# Return the maximum subarray sum of all the subarrays that meet the conditions. 
# If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = windowStart = 0
        
        for windowEnd in range(k, len(nums) + 1):
            if len(set(nums[windowStart:windowEnd])) == k:
                maxSum = max(maxSum, sum(nums[windowStart:windowEnd]))
            
            windowStart += 1
        return maxSum