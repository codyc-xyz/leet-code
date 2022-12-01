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


