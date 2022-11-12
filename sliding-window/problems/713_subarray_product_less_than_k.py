# Given an array of integers nums and an integer k, return the number of contiguous subarrays 
# where the product of all the elements in the subarray is strictly less than k.

import numpy

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = windowStart = 0
        dq = deque()
        for windowStart in range(len(nums)):
            windowEnd = windowStart
            while windowEnd < len(nums):
                dq.append(nums[windowEnd])
                if numpy.prod(dq) < k:
                    count += 1
                if windowEnd == len(nums) - 1 or numpy.prod(dq) >= k:
                    dq.clear()
                    break
                windowEnd += 1
        return count
                

