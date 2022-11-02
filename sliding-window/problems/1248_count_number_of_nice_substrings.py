# Given an array of integers nums and an integer k. 
# A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = res = 0
        windowStart = 0
        
        for windowEnd in range(len(nums)):
            if nums[windowEnd] % 2 != 0:
                k -= 1
                count = 0
            while k == 0:
                count += 1
                if nums[windowStart] % 2 != 0:
                    k += 1
                windowStart += 1
            res += count
        
        return res

