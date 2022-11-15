# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. 
# In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.


  class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums)
        windowStart = 0
        for windowEnd in range(len(sortedNums)):
            k += sortedNums[windowEnd]
            if k < sortedNums[windowEnd] * (windowEnd - windowStart + 1):
                k -= sortedNums[windowStart]
                windowStart += 1
                
        return windowEnd - windowStart + 1