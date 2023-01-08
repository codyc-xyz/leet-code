# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, n in enumerate(nums):
            j = i
            res = 0
            while j < len(nums):
                res += nums[j]
                if res == k:
                    ans += 1
                j += 1
       
        return ans