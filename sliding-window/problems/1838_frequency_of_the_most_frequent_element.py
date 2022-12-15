# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. 
# In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        windowEnd = windowStart = 0
        while windowEnd < len(nums):
            k += nums[windowEnd]
            if k < nums[windowEnd] * (windowEnd - windowStart + 1):
                k -= nums[windowStart]
                windowStart += 1
            windowEnd += 1
        return windowEnd - windowStart