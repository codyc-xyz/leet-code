# You are given an integer array nums and an integer k. 
# Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.

# Return the maximum subarray sum of all the subarrays that meet the conditions. 
# If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.Counter(nums[:k])
        currSum = sum(nums[:k])
        windowStart = 0
        
        if len(seen) == k:
            maxSum = currSum
        else:
            maxSum = 0
        
        for windowEnd in range(k, len(nums)):
            currSum += nums[windowEnd] - nums[windowStart]
            seen[nums[windowEnd]] += 1
            seen[nums[windowStart]] -= 1
            if seen[nums[windowStart]] == 0:
                del seen[nums[windowStart]]
            if len(seen) == k:
                maxSum = max(maxSum, currSum)
            windowStart += 1
        return maxSum