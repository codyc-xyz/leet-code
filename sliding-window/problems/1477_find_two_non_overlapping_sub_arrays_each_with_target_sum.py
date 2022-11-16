# You are given an array of integers arr and an integer target.

# You have to find two non-overlapping sub-arrays of arr each with a sum equal target. 
# There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

# Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        minLen = float("inf")
        testTarget = target
        diffs = []
        windowStart = windowEnd = 0
        repeat = False
        while windowEnd < len(arr):
            testTarget -= arr[windowEnd]
            while windowStart <= windowEnd and testTarget < 0:
                testTarget += arr[windowStart]
                windowStart += 1
            if testTarget == 0 and repeat == False:
                diffs.append(windowEnd - windowStart + 1)
                windowStart = windowEnd
                testTarget = target
                repeat = True
            else:
                repeat = False
                windowEnd += 1
        sortedDiffs = sorted(diffs)
        if len(diffs) > 1:
            return sortedDiffs[1] + sortedDiffs[0]
        else:
            return -1

