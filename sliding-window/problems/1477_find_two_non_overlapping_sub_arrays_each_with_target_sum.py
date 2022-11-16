# You are given an array of integers arr and an integer target.

# You have to find two non-overlapping sub-arrays of arr each with a sum equal target. 
# There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

# Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        best_at_i = [float("inf")] * len(arr)
        best = float("inf")
        windowStart = 0
        
        for windowEnd in range(len(arr)):
            target -= arr[windowEnd]
            
            while target < 0 and windowStart <= windowEnd:
                target += arr[windowStart]
                windowStart += 1
            if target == 0:
                best = min(best, best_at_i[windowStart - 1] + windowEnd - windowStart + 1)
                best_at_i[windowEnd] = min(best_at_i[windowEnd - 1], windowEnd - windowStart + 1)
            else:
                best_at_i[windowEnd] = best_at_i[windowEnd - 1]
        if best != float("inf"):
            return best
        else:
            return -1
