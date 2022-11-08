# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = deque()
        for windowEnd in range(len(arr)):
            if len(closest) < k:
                closest.append(arr[windowEnd])
            elif len(closest) >= k and abs(arr[windowEnd] - x) < abs(closest[0] - x):
                closest.popleft()
                closest.append(arr[windowEnd])
        return closest


