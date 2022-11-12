# Given an array of integers nums and an integer k, return the number of contiguous subarrays 
# where the product of all the elements in the subarray is strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        windowStart = ans = 0
        res = 1
        if k <= 1:
            return 0
        for windowEnd in range(len(nums)):
            res *= nums[windowEnd]
            while res >= k:
                res /= nums[windowStart]
                windowStart += 1
            ans += windowEnd - windowStart + 1
        return ans
                

