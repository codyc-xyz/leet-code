# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.

# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        windowEnd = windowStart = 0
        longest = 1
        
        if len(arr) < 2:
            return len(arr)
        
        while windowEnd < len(arr):
           
            while windowStart < len(arr) -1 and arr[windowStart] == arr[windowStart + 1]:
                windowStart += 1
            while windowEnd < len(arr) -1 and (arr[windowEnd - 1] > arr[windowEnd] < arr[windowEnd + 1] or arr[windowEnd - 1] < arr[windowEnd] > arr[windowEnd + 1]):
                windowEnd += 1
            longest = max(longest, windowEnd - windowStart + 1)
            windowStart = windowEnd
            windowEnd += 1
        return longest

            
            