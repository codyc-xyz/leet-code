# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. 
# In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums)
        maxCount = 0
        for i, n in enumerate(sortedNums):
            diff = []
            diffK = k
            windowStart = 0
            for c in range(len(sortedNums)):
                diff.append(abs(sortedNums[i] - sortedNums[c]))
            sortedDiff = sorted(diff)
            while diffK >= 0 and windowStart < len(sortedDiff):
                diffK -= sortedDiff[windowStart]
                if diffK >= 0:
                    windowStart += 1
            maxCount = max(maxCount, windowStart)
        return maxCount