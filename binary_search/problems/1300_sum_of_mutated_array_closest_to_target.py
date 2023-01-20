# Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, 
# the sum of the array gets as close as possible (in absolute difference) to target.

# In case of a tie, return the minimum such integer.

# Notice that the answer is not neccesarilly a number from arr.

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        pSum = [arr[0]]
        
        for i in range(1, len(arr)):
            pSum.append(pSum[-1] + arr[i])
            
        l, r = 0, max(arr)
        res = float("inf")
        while l <= r:
            m = (l + r) // 2
            
            right = bisect_right(arr, m)
            n = len(arr) - right
            if right > 0:
                curr = (pSum[right - 1] + (n * m)) 
            else:
                curr = (n * m) 
            if n != 0:
                diff = abs((curr - target) / n)
            else:
                diff = abs(curr - target)
            print(diff, res)
            if diff < res:
                res = diff
                ans = m
            if curr < target:
                l = m + 1
            else:
                r = m - 1
        return ans