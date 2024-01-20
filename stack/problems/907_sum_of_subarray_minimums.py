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
        ans = 0
        MOD = 10**9+7
        for i in range(len(arr)):
            currMin = arr[i]
            ans += currMin
            for j in range(i + 1, len(arr)):
                if arr[j] < currMin:
                    currMin = arr[j]
                ans += currMin
        return ans % MOD


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
    

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        N = len(arr)
        MOD = 10**9+7
        stack = []
        for i in range(len(arr)):
            while stack and stack[-1][0] > arr[i]:
                val, idx = stack.pop()
                left = idx - (stack[-1][1] if stack else -1)
                right = i - idx
                ans += val * left * right
            stack.append([arr[i], i])

        while stack:
            val, idx = stack.pop()
            left = idx - (stack[-1][1] if stack else -1)
            right = N - idx
            ans += val * left * right
        return ans % MOD
