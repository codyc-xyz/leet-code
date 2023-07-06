# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
# Return 0 if there is no such subarray.


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        windowStart = 0
        
        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 0:
                k -= 1
            if k < 0:
                if nums[windowStart] == 0:
                    k += 1
                windowStart += 1
        return windowEnd - windowStart
    
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zeros = longest = windowEnd = windowStart = 0
        while windowEnd < len(nums):
            if nums[windowEnd] == 0:
                zeros += 1
            while zeros > 1:
                if nums[windowStart] == 0:
                    zeros -= 1
                windowStart += 1
            longest = max(longest, windowEnd - windowStart)
            windowEnd += 1
        return longest