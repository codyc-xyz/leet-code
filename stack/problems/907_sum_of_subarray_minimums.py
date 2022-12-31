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

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arrSums = 0
        stack = []
        mod = 10**9+7
        for i in range(len(arr) + 1):
            
            while stack and (i == len(arr) or arr[i] <= stack[-1][1]):
                mid, val = stack.pop()
                
                if stack:
                    left = stack[-1][0]
                else:
                    left = -1
                right = i
                
                width = (mid - left) * (right - mid)
                arrSums += (width * val)
            if i < len(arr):
                stack.append([i, arr[i]])
        return arrSums%mod