# The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.
# For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.

# Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

# Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

# A subarray is a contiguous part of an array.

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        maxProduct = 0
        mod = 10**9+7
        for i, n in enumerate(nums):
            arr = []
            j = i 
            while j < len(nums):
                arr.append(nums[j])
                maxProduct = max(maxProduct, sum(arr) * min(arr))
                j += 1
        return maxProduct%mod