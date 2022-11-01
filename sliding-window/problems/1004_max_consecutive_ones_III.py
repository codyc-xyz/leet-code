# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0
        maxLen = 0
        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 0:
                k -= 1
            if k < 0:
                if nums[windowStart] == 0:
                    k += 1
                windowStart += 1
            maxLen = max(maxLen, windowEnd - windowStart + 1)
                
        return maxLen
        