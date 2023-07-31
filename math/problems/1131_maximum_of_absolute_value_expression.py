# Given two arrays of integers with equal lengths, return the maximum value of:

# |arr1[i] - arr1[j] | + | arr2[i] - arr2[j] | + | i - j|

# where the maximum is taken over all 0 <= i, j < arr1.length.

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = float('-inf')
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                ans = max(ans, abs(arr1[i] - arr1[j]) +
                          abs(arr2[i] - arr2[j] + abs(i - j)))
        return ans
