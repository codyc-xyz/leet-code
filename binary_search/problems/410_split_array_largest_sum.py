# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if self.splitSuccess(nums, m, k - 1):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans

    def splitSuccess(self, nums, m, k):
        curr = m
        for n in nums:
            curr -= n
            if curr < 0:
                k -= 1
                curr = m - n
        return k >= 0