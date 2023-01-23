# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def splitSuccessful(m, K):
            M = m
            for n in nums:
                if M - n < 0:
                    K -= 1
                    M = m 
                M -= n
            if M < 0:
                K -= 1
            return K >= 0
        
        l, r = max(nums), sum(nums)
        while l <= r:
            m = (l + r) // 2
            K = k - 1
            if splitSuccessful(m, K):
                r = m - 1
            else:
                l = m + 1
        return l