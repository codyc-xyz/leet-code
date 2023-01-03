# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        dq = deque()
        for i, n in enumerate(arr):
            if len(dq) < k:
                dq.append(n)
            elif abs(n - x) < abs(dq[0] - x):
                dq.popleft()
                dq.append(n)
        return dq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if len(arr) <= k:
            return arr
        windowStart, windowEnd = 0, k - 1
        while windowEnd < len(arr) - 1:
            if abs(x - arr[windowStart]) < abs(x - arr[windowEnd + 1]) or (abs(x - arr[windowStart]) == abs(x - arr[windowEnd + 1]) and arr[windowStart] < arr[windowEnd + 1]):
                return arr[windowStart:windowEnd + 1]
            windowStart += 1
            windowEnd += 1
        return arr[windowStart:windowEnd + 1]