# Given an array of integers nums and an integer limit, 
# return the size of the longest non-empty subarray such that the absolute difference 
# between any two elements of this subarray is less than or equal to limit.

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longestSub = 0
        sub = []
        for windowEnd in range(len(nums)):
            sub.append(nums[windowEnd])
            if max(sub) - min(sub) <= limit:
                longestSub = max(longestSub, len(sub))
            while max(sub) - min(sub) > limit:
                sub.pop(0)
        return longestSub
    