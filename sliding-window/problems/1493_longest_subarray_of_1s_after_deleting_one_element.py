# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
# Return 0 if there is no such subarray.


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        windowStart = maxLen = 0
        k = 1
        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 0:
                k -= 1
            if k < 0:
                if nums[windowStart] == 0:
                    k += 1
                windowStart += 1
            maxLen = max(maxLen, windowEnd - windowStart)
        return maxLen