# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arrSums = 0
        for i, n in enumerate(arr):
            j = i
            minN = float("inf")
            while j < len(arr):
                minN = min(minN, arr[j])
                arrSums += minN
                j += 1
        return arrSums%(10**9+7)