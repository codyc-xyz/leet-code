# Given an array of integers nums and an integer k. 
# A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            windowStart = 0
            for windowEnd in range(len(nums) - i):
                if nums[windowEnd + i] % 2 != 0:
                    k -= 1
                if k == 0:
                    count += 1
                if 0 > k:
                    if nums[windowStart + i] % 2 != 0:
                        k += 1
                    windowStart += 1
        return count

