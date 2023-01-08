# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0: 1}
        prefix = 0
        ans = 0
        for n in nums:
            prefix += n
            if prefix - k in hm:
                ans += hm[prefix - k]
            hm[prefix] = 1 + hm.get(prefix, 0) 
        return ans